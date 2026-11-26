/*! Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
 *  SPDX-License-Identifier: MIT-0
 */
package com.example.agent;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springaicommunity.agentcore.annotation.AgentCoreInvocation;
import org.springaicommunity.agentcore.context.AgentCoreContext;
import org.springaicommunity.agentcore.context.AgentCoreHeaders;
import org.springframework.ai.chat.client.ChatClient;
import org.springframework.web.bind.annotation.RestController;

/**
 * The document review agent.
 *
 * <p>The method annotated with {@link AgentCoreInvocation} is wired to {@code POST
 * /invocations} by the AgentCore runtime starter. Returning a plain {@code String} (rather
 * than a {@code Flux}) yields a single non-streaming JSON response, which is what the
 * calling durable function step expects.
 */
@RestController
public class ReviewAgentController {

    private static final Logger logger = LoggerFactory.getLogger(ReviewAgentController.class);

    private static final String ANALYZE_PROMPT = """
            You are a document review assistant. Read the document supplied by the user and
            produce a concise draft summary for a human reviewer.

            Your response must contain:
            1. A one-paragraph summary of the document's purpose.
            2. Three to five key points as a bullet list.
            3. Any concerns, ambiguities, or missing information a reviewer should check.

            Be factual. Do not invent details that are not present in the document.
            """;

    private static final String FINALIZE_PROMPT = """
            You are a document review assistant. A human reviewer has approved the draft
            supplied by the user. Produce the final, polished version of the summary.

            Apply any reviewer comments that are provided. Tighten the wording, remove
            reviewer-only scaffolding such as open questions, and return prose suitable for
            publication. Do not introduce new factual claims.
            """;

    private final ChatClient chatClient;

    public ReviewAgentController(ChatClient.Builder chatClientBuilder) {
        this.chatClient = chatClientBuilder.build();
    }

    @AgentCoreInvocation
    public String handleInvocation(AgentRequest request, AgentCoreContext agentCoreContext) {
        String sessionId = agentCoreContext.getHeader(AgentCoreHeaders.SESSION_ID);
        String mode = request.mode() == null ? "analyze" : request.mode();
        logger.info("Handling '{}' invocation for session {}", mode, sessionId);

        return switch (mode) {
            case "analyze" -> chatClient.prompt()
                    .system(ANALYZE_PROMPT)
                    .user("Review the following document:\n\n" + request.document())
                    .call()
                    .content();
            case "finalize" -> chatClient.prompt()
                    .system(FINALIZE_PROMPT)
                    .user(buildFinalizeMessage(request))
                    .call()
                    .content();
            default -> throw new IllegalArgumentException(
                    "Unsupported mode '" + mode + "'. Expected 'analyze' or 'finalize'.");
        };
    }

    private static String buildFinalizeMessage(AgentRequest request) {
        StringBuilder message = new StringBuilder("Approved draft:\n\n").append(request.draft());
        if (request.reviewerComments() != null && !request.reviewerComments().isBlank()) {
            message.append("\n\nReviewer comments:\n").append(request.reviewerComments());
        }
        return message.toString();
    }
}
