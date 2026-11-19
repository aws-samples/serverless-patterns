/*! Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
 *  SPDX-License-Identifier: MIT-0
 */
package com.example.durableagent;

import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.databind.node.ObjectNode;
import software.amazon.awssdk.core.ResponseBytes;
import software.amazon.awssdk.core.SdkBytes;
import software.amazon.awssdk.services.bedrockagentcore.BedrockAgentCoreClient;
import software.amazon.awssdk.services.bedrockagentcore.model.InvokeAgentRuntimeRequest;
import software.amazon.awssdk.services.bedrockagentcore.model.InvokeAgentRuntimeResponse;

/**
 * Thin wrapper over {@code InvokeAgentRuntime} for the Spring AI agent hosted on AgentCore.
 *
 * <p>Two details are easy to get wrong:
 *
 * <ul>
 *   <li>{@code InvokeAgentRuntimeResponse} exposes no {@code payload()} accessor - the response
 *       body is streamed. {@code invokeAgentRuntimeAsBytes} buffers it so the result can be read
 *       as a string.
 *   <li>{@code runtimeSessionId} must be at least 33 characters, and is derived deterministically
 *       from the document ID by {@link #sessionIdFor} - never randomly - so that a replay reuses
 *       the same session and the agent sees one continuous conversation across the approval gate.
 * </ul>
 */
public class AgentClient {

    /** AgentCore requires a session ID of at least this many characters. */
    private static final int MIN_SESSION_ID_LENGTH = 33;

    /** Marks the session as belonging to this workflow, and lengthens short document IDs. */
    private static final String SESSION_ID_PREFIX = "doc-review-";

    private static final ObjectMapper MAPPER = new ObjectMapper();

    private final BedrockAgentCoreClient client;
    private final String agentRuntimeArn;

    public AgentClient(BedrockAgentCoreClient client, String agentRuntimeArn) {
        this.client = client;
        this.agentRuntimeArn = agentRuntimeArn;
    }

    /**
     * Invokes the agent and returns its response text.
     *
     * @param documentId identifies the review; both turns share the session derived from it
     * @param mode      {@code analyze} or {@code finalize}
     * @param document  document text for {@code analyze}; may be null for {@code finalize}
     * @param draft     approved draft for {@code finalize}; may be null for {@code analyze}
     * @param comments  reviewer comments to fold into the final summary; may be null
     */
    public String invoke(String documentId, String mode, String document, String draft, String comments) {
        if (client == null) {
            throw new IllegalStateException("No AgentCore client configured");
        }
        ObjectNode payload = MAPPER.createObjectNode();
        payload.put("mode", mode);
        if (document != null) {
            payload.put("document", document);
        }
        if (draft != null) {
            payload.put("draft", draft);
        }
        if (comments != null) {
            payload.put("reviewerComments", comments);
        }

        String body;
        try {
            body = MAPPER.writeValueAsString(payload);
        } catch (Exception e) {
            throw new IllegalStateException("Unable to serialize agent request", e);
        }

        ResponseBytes<InvokeAgentRuntimeResponse> response = client.invokeAgentRuntimeAsBytes(
                InvokeAgentRuntimeRequest.builder()
                        .agentRuntimeArn(agentRuntimeArn)
                        .runtimeSessionId(sessionIdFor(documentId))
                        .contentType("application/json")
                        .accept("application/json")
                        .payload(SdkBytes.fromUtf8String(body))
                        .build());

        return response.asUtf8String();
    }

    /**
     * Builds the AgentCore session ID for a document.
     *
     * <p>AgentCore requires {@code runtimeSessionId} to be at least
     * {@value #MIN_SESSION_ID_LENGTH} characters. Document IDs are often shorter than that, so the
     * ID is prefixed and then right-padded to the minimum. The document ID stays at the front,
     * which keeps AgentCore's logs readable.
     *
     * <p>This must be a pure function of the document ID. Using a random value - a fresh
     * {@code UUID}, say - would hand the agent a different session on every replay, so the
     * finalize turn would lose the context of the analyze turn.
     */
    static String sessionIdFor(String documentId) {
        StringBuilder id = new StringBuilder(SESSION_ID_PREFIX).append(documentId);
        while (id.length() < MIN_SESSION_ID_LENGTH) {
            id.append('0');
        }
        return id.toString();
    }
}
