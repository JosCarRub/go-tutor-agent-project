package com.jose_carlos.go_tutor_backend.client;

/**
 * Interface that abstracts the communication with the external container of the Go Agent.
 * Defines the contract for obtaining responses from the agent
 */
public interface GoTutorAgentClient {

    /**
     * Sends a prompt to the Go agent and gets his response.
     *
     * @param prompt The text prompt to send to the agent.
     * @return The plaintext response from the agent.
     */
    String getResponse(String prompt);

}