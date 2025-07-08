package com.jose_carlos.go_tutor_backend.exception;

import lombok.extern.slf4j.Slf4j;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.ControllerAdvice;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.context.request.WebRequest;

import java.time.LocalDateTime;
import java.util.Map;


@ControllerAdvice
@Slf4j
public class GlobalExceptionHandler {


    @ExceptionHandler(InvalidPromptException.class)
    public ResponseEntity<Object> handleInvalidPromptException(InvalidPromptException ex, WebRequest request) {
        log.warn("Manejando InvalidPromptException: {}", ex.getMessage());
        return buildErrorResponse(ex, HttpStatus.BAD_REQUEST);
    }


    @ExceptionHandler(AgentCommunicationException.class)
    public ResponseEntity<Object> handleAgentCommunicationException(AgentCommunicationException ex, WebRequest request) {

        log.error("Manejando AgentCommunicationException: {}", ex.getMessage(), ex.getCause());
        return buildErrorResponse(ex, HttpStatus.SERVICE_UNAVAILABLE);
    }

    @ExceptionHandler(Exception.class)
    public ResponseEntity<Object> handleGlobalException(Exception ex, WebRequest request) {
        log.error("¡Error no controlado capturado por el manejador global!", ex);
        return buildErrorResponse(ex, HttpStatus.INTERNAL_SERVER_ERROR);
    }


    private ResponseEntity<Object> buildErrorResponse(Exception ex, HttpStatus status) {
        Map<String, Object> body = Map.of(
                "timestamp", LocalDateTime.now(),
                "status", status.value(),
                "error", status.getReasonPhrase(),
                "message", ex.getMessage()
        );
        return new ResponseEntity<>(body, status);
    }
}
