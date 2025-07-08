package com.jose_carlos.go_tutor_backend.service.impl;

import com.jose_carlos.go_tutor_backend.client.GoTutorAgentClient;
import com.jose_carlos.go_tutor_backend.dto.AgentPromptResponseDTO;
import com.jose_carlos.go_tutor_backend.dto.UserPromptRequestDTO;
import com.jose_carlos.go_tutor_backend.entities.Conversation;
import com.jose_carlos.go_tutor_backend.exception.AgentCommunicationException;
import com.jose_carlos.go_tutor_backend.exception.InvalidPromptException;
import com.jose_carlos.go_tutor_backend.repository.ConversationRepository;
import com.jose_carlos.go_tutor_backend.service.TutorAgentService;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.stereotype.Service;

import java.time.LocalDateTime;
import java.util.List;

@Service
@RequiredArgsConstructor
@Slf4j
public class TutorAgentServiceImpl implements TutorAgentService {

    private final GoTutorAgentClient goTutorAgentClient;

    private final ConversationRepository conversationRepository;


    @Override
    public AgentPromptResponseDTO processPrompt(UserPromptRequestDTO requestDTO) {
        log.info("Iniciando procesamiento para el prompt: '{}'", requestDTO.getUserPrompt());

        if (requestDTO.getUserPrompt() == null || requestDTO.getUserPrompt().isBlank()) {
            log.warn("Se recibió un prompt inválido (nulo o en blanco).");
            throw new InvalidPromptException("El prompt no puede ser nulo o estar vacío.");
        }
        String agentRawResponse = communicateWithAgent(requestDTO.getUserPrompt());

        saveConversation(requestDTO.getUserPrompt(), agentRawResponse);

        return new AgentPromptResponseDTO(agentRawResponse);
    }


    private String communicateWithAgent(String prompt) {
        try {
            log.info("Delegando la petición al GoTutorAgentClient.");
            String response = goTutorAgentClient.getResponse(prompt);
            log.info("Respuesta recibida del cliente.");
            return response;
        } catch (Exception e) {
            log.error("Fallo la comunicación con el Go Agent.", e);
            throw new AgentCommunicationException("Error al comunicarse con el agente Go.", e);
        }
    }

    private void saveConversation(String userPrompt, String agentResponse) {
        try {
            log.info("Guardando conversación en la base de datos...");
            Conversation.Message userMessage = new Conversation.Message();
            userMessage.setRole("user");
            userMessage.setContent(userPrompt);
            userMessage.setTimestamp(LocalDateTime.now());

            Conversation.Message agentMessage = new Conversation.Message();
            agentMessage.setRole("agent");
            agentMessage.setContent(agentResponse);
            agentMessage.setTimestamp(LocalDateTime.now());

            Conversation conversation = new Conversation();
            conversation.setMessages(List.of(userMessage, agentMessage));
            conversation.setCreatedAt(LocalDateTime.now());

            conversationRepository.save(conversation);
            log.info("Conversación guardada con éxito.");
        } catch (Exception e) {

            log.error("[ERROR] No se pudo guardar la conversación!", e);
        }
    }
}