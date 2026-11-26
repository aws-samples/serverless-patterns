/*! Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
 *  SPDX-License-Identifier: MIT-0
 */
package com.example.durableagent;

import com.fasterxml.jackson.databind.ObjectMapper;
import org.junit.jupiter.api.Test;
import software.amazon.awssdk.core.ResponseBytes;
import software.amazon.awssdk.services.bedrockagentcore.BedrockAgentCoreClient;
import software.amazon.awssdk.services.bedrockagentcore.model.InvokeAgentRuntimeRequest;
import software.amazon.awssdk.services.bedrockagentcore.model.InvokeAgentRuntimeResponse;
import software.amazon.awssdk.services.bedrockagentcore.model.RuntimeClientErrorException;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertNull;
import static org.junit.jupiter.api.Assertions.assertThrows;
import static org.junit.jupiter.api.Assertions.assertTrue;

class AgentClientTest {
    @Test
    void serviceFailureRetainsDiagnosticsInSerializableException() throws Exception {
        BedrockAgentCoreClient client = new BedrockAgentCoreClient() {
            @Override
            public ResponseBytes<InvokeAgentRuntimeResponse> invokeAgentRuntimeAsBytes(
                    InvokeAgentRuntimeRequest request) {
                throw RuntimeClientErrorException.builder()
                        .message("Model access denied")
                        .statusCode(424)
                        .requestId("request-123")
                        .build();
            }

            @Override
            public String serviceName() {
                return "bedrock-agentcore";
            }

            @Override
            public void close() {
            }
        };
        AgentClient agent = new AgentClient(client, "test-runtime");

        IllegalStateException failure = assertThrows(IllegalStateException.class,
                () -> agent.invoke("doc-001", "analyze", "Document", null, null));

        assertTrue(failure.getMessage().contains("AgentCore analyze failed"));
        assertTrue(failure.getMessage().contains("424"));
        assertTrue(failure.getMessage().contains("request-123"));
        assertTrue(failure.getMessage().contains("Model access denied"));
        assertNull(failure.getCause(), "the non-deserializable SDK exception must not enter the checkpoint");

        ObjectMapper mapper = new ObjectMapper();
        IllegalStateException restored = mapper.readValue(
                mapper.writeValueAsString(failure), IllegalStateException.class);
        assertEquals(failure.getMessage(), restored.getMessage());
        assertNull(restored.getCause());
    }
}
