package com.jose_carlos.go_tutor_backend.exception;

import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.ResponseStatus;

@ResponseStatus(HttpStatus.BAD_REQUEST)
public class InvalidPromptException extends RuntimeException {

    public InvalidPromptException(String message) {
        super(message);
    }
}
