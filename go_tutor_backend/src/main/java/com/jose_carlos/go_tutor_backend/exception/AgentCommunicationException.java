package com.jose_carlos.go_tutor_backend.exception;

import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.ResponseStatus;

@ResponseStatus(HttpStatus.SERVICE_UNAVAILABLE)
public class AgentCommunicationException extends RuntimeException {
    public AgentCommunicationException(String message, Throwable cause) {
        super(message, cause);
    }
}
