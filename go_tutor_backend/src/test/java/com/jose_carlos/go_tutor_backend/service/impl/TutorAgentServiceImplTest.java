package com.jose_carlos.go_tutor_backend.service.impl;

import com.jose_carlos.go_tutor_backend.client.GoTutorAgentClient;
import com.jose_carlos.go_tutor_backend.dto.AgentPromptResponseDTO;
import com.jose_carlos.go_tutor_backend.dto.UserPromptRequestDTO;
import com.jose_carlos.go_tutor_backend.entities.Conversation;
import com.jose_carlos.go_tutor_backend.exception.AgentCommunicationException;
import com.jose_carlos.go_tutor_backend.exception.InvalidPromptException;
import com.jose_carlos.go_tutor_backend.repository.ConversationRepository;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import org.mockito.InjectMocks;
import org.mockito.Mock;
import org.mockito.junit.jupiter.MockitoExtension;

import static org.junit.jupiter.api.Assertions.*;
import static org.mockito.Mockito.*;

import static org.mockito.Mockito.verify;
import static org.mockito.Mockito.when;

@ExtendWith(MockitoExtension.class)
public class TutorAgentServiceImplTest {

    @Mock
    private GoTutorAgentClient mockAgentClient;

    @Mock
    private ConversationRepository mockRepository;

    @InjectMocks
    private TutorAgentServiceImpl tutorAgentService;


    @Test
    @DisplayName("Debería procesar un prompt válido, llamar al cliente, guardar en el repositorio y devolver la respuesta")
    void processPrompt_whenPromptIsValid_shouldSucceed() {

        final String userPrompt = "Explícame las interfaces en Go";
        final String agentResponse = "Una interfaz en Go es un tipo que especifica un conjunto de métodos...";

        UserPromptRequestDTO requestDTO = new UserPromptRequestDTO();
        requestDTO.setUserPrompt(userPrompt);

        when(mockAgentClient.getResponse(userPrompt)).thenReturn(agentResponse);

        when(mockRepository.save(any(Conversation.class))).thenAnswer(invocation -> invocation.getArgument(0));

        AgentPromptResponseDTO actualResponseDTO = tutorAgentService.processPrompt(requestDTO);

        assertNotNull(actualResponseDTO, "La respuesta no debería ser nula.");
        assertEquals(agentResponse, actualResponseDTO.getAgentResponse(), "La respuesta del DTO no coincide con la esperada del agente.");

        verify(mockAgentClient, times(1)).getResponse(userPrompt);

        verify(mockRepository, times(1)).save(any(Conversation.class));

        verifyNoMoreInteractions(mockAgentClient, mockRepository);

    }

    @Test
    @DisplayName("Debería lanzar InvalidPromptException cuando el prompt es nulo")
    void processPrompt_whenPromptIsNull_shouldThrowInvalidPromptException() {


        UserPromptRequestDTO requestWithNullPrompt = new UserPromptRequestDTO();
        requestWithNullPrompt.setUserPrompt(null);


        assertThrows(InvalidPromptException.class, () -> {
            tutorAgentService.processPrompt(requestWithNullPrompt);
        });


        verifyNoInteractions(mockAgentClient, mockRepository);
    }

    @Test
    @DisplayName("Debería lanzar InvalidPromptException cuando el prompt está en blanco")
    void processPrompt_whenPromptIsBlank_shouldThrowInvalidPromptException() {


        UserPromptRequestDTO requestWithBlankPrompt = new UserPromptRequestDTO();
        requestWithBlankPrompt.setUserPrompt("   ");

        assertThrows(InvalidPromptException.class, () -> {
            tutorAgentService.processPrompt(requestWithBlankPrompt);
        });

        verifyNoInteractions(mockAgentClient, mockRepository);
    }

    @Test
    @DisplayName("Debería lanzar AgentCommunicationException cuando el cliente del agente falla")
    void processPrompt_whenAgentClientThrowsException_shouldThrowAgentCommunicationException() {

        final String userPrompt = "Un prompt válido";
        UserPromptRequestDTO requestDTO = new UserPromptRequestDTO(userPrompt);

        when(mockAgentClient.getResponse(userPrompt))
                .thenThrow(new RuntimeException("Error de red simulado"));

        assertThrows(AgentCommunicationException.class, () -> {
            tutorAgentService.processPrompt(requestDTO);
        });

        // a pesar del error, verificame que intentamos llamar al cliente
        verify(mockAgentClient, times(1)).getResponse(userPrompt);

        // verificamos que no intentamos guardar en el repositorio si la llamada al agente falló
        verifyNoInteractions(mockRepository);
    }
}
