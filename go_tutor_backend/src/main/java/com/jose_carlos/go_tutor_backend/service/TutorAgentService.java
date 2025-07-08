package com.jose_carlos.go_tutor_backend.service;

import com.jose_carlos.go_tutor_backend.dto.AgentPromptResponseDTO;
import com.jose_carlos.go_tutor_backend.dto.UserPromptRequestDTO;

public interface TutorAgentService {

    AgentPromptResponseDTO processPrompt(UserPromptRequestDTO requestDTO);
}