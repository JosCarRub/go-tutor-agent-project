package com.jose_carlos.go_tutor_backend.client.impl;

import com.jose_carlos.go_tutor_backend.client.GoTutorAgentClient;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.http.MediaType;
import org.springframework.stereotype.Component;
import org.springframework.web.reactive.function.client.WebClient;

record AgentRequestBody(String message) {}
record AgentResponseBody(String reply) {}

@Slf4j
@Component
@RequiredArgsConstructor
public class HttpGoTutorAgentClient implements GoTutorAgentClient {

    private final WebClient goTutorAgentWebClient;

    @Override
    public String getResponse(String prompt) {
        AgentRequestBody requestBody = new AgentRequestBody(prompt);
        log.info("Enviando petición al agente Go en /api/v1/chat con mensaje: '{}'", prompt);

        AgentResponseBody responseBody = goTutorAgentWebClient.post()
                .uri("/api/v1/chat")
                .contentType(MediaType.APPLICATION_JSON)
                .bodyValue(requestBody)
                .retrieve()
                .bodyToMono(AgentResponseBody.class)
                .block();

        String reply = (responseBody != null) ? responseBody.reply() : "No se recibió respuesta del agente.";
        log.info("Respuesta recibida del agente Go.");
        return reply;
    }
}