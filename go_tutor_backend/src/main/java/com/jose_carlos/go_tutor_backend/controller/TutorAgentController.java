package com.jose_carlos.go_tutor_backend.controller;

import com.jose_carlos.go_tutor_backend.constant.ApiPathConstant;
import com.jose_carlos.go_tutor_backend.dto.AgentPromptResponseDTO;
import com.jose_carlos.go_tutor_backend.dto.UserPromptRequestDTO;
import com.jose_carlos.go_tutor_backend.service.TutorAgentService;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;


@RestController
@RequestMapping(ApiPathConstant.TUTOR_AGENT_RESOURCE)
@RequiredArgsConstructor
@Slf4j
public class TutorAgentController {

    private final TutorAgentService tutorAgentService;

    @PostMapping("/prompt")
    public ResponseEntity<AgentPromptResponseDTO> handleUserPrompt(@RequestBody UserPromptRequestDTO requestDTO) {

        log.info("Petición POST recibida en {}", ApiPathConstant.TUTOR_AGENT_RESOURCE + "/prompt");

        AgentPromptResponseDTO responseDTO = tutorAgentService.processPrompt(requestDTO);

        return ResponseEntity.ok(responseDTO);
    }
}