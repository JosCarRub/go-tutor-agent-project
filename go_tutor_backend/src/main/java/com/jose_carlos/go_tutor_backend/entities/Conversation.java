package com.jose_carlos.go_tutor_backend.entities;

import lombok.Data;
import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;

import java.time.LocalDateTime;
import java.util.List;

@Data
@Document(collection = "conversations")
public class Conversation {

    @Id
    private String id;

    private List<Message> messages;

    private LocalDateTime createdAt;

    // Sub-documento para los mensajes. No necesita ser una entidad separada.
    @Data
    public static class Message {
        private String role; // "user" o "agent"
        private String content;
        private LocalDateTime timestamp;
    }
}
