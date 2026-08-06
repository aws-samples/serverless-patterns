/*! Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
 *  SPDX-License-Identifier: MIT-0
 */
package com.example.agent;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

/**
 * Spring Boot entry point for the document review agent.
 *
 * <p>The {@code spring-ai-agentcore-runtime-starter} on the classpath auto-configures the
 * two endpoints Amazon Bedrock AgentCore Runtime requires - {@code POST /invocations} and
 * {@code GET /ping} - so this application only needs to supply the agent logic itself.
 */
@SpringBootApplication
public class AgentApplication {

    public static void main(String[] args) {
        SpringApplication.run(AgentApplication.class, args);
    }
}
