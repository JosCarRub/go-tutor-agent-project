package com.jose_carlos.go_tutor_backend.config;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.web.reactive.function.client.WebClient;

@Configuration
public class WebClientConfig {

    @Value("${go.agent.base-url}")
    private String goAgentBaseUrl;

    @Bean
    public WebClient goTutorAgentWebClient() {
        return WebClient.builder()
                .baseUrl(goAgentBaseUrl)
                .build();
    }
}
