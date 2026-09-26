/*! Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
 *  SPDX-License-Identifier: MIT-0
 */
package com.example.durableagent;

import java.time.Duration;

import com.example.durableagent.model.Decision;
import com.example.durableagent.model.ReviewRequest;
import com.example.durableagent.model.ReviewResult;
import software.amazon.awssdk.services.bedrockagentcore.BedrockAgentCoreClient;
import software.amazon.lambda.durable.DurableContext;
import software.amazon.lambda.durable.DurableHandler;
import software.amazon.lambda.durable.config.CallbackConfig;
import software.amazon.lambda.durable.config.WaitForCallbackConfig;
import software.amazon.lambda.durable.exception.CallbackTimeoutException;

/**
 * Orchestrates a document review across an AI agent and a human approver.
 *
 * <pre>
 *   step            analyze-document    -&gt; Spring AI agent on AgentCore drafts a summary
 *   waitForCallback await-human-review  -&gt; execution suspends until a human decides
 *   step            finalize-document   -&gt; agent polishes the approved draft
 * </pre>
 *
 * <p>While suspended at the callback the function consumes no compute, and it can stay that way
 * for as long as {@code DurableConfig.ExecutionTimeout} allows. When the decision arrives, Lambda
 * starts a fresh invocation and replays this method from the top, skipping the operations that
 * already completed - so the agent is not asked to analyze the document a second time.
 *
 * <h2>Where state lives</h2>
 *
 * Nowhere in this pattern. Lambda checkpoints each durable operation - step results, the pending
 * callback, and this method's return value - into storage the service manages, retained for
 * {@code DurableConfig.RetentionPeriodInDays}. Read it back with
 * {@code aws lambda get-durable-execution} and {@code ... get-durable-execution-history}; there is
 * no table to provision.
 *
 * <h2>Determinism</h2>
 *
 * Both agent calls happen inside steps, so replay reuses the checkpointed text rather than
 * re-invoking the model. Steps return their values instead of mutating captured state, because on
 * replay a step body does not execute and any such mutation would silently be lost.
 */
public class DocumentReviewWorkflow extends DurableHandler<ReviewRequest, ReviewResult> {

    /**
     * How long a review may sit awaiting a human. Must stay below the function's
     * {@code DurableConfig.ExecutionTimeout}, which is set to 7 days in template.yaml.
     */
    static final Duration APPROVAL_TIMEOUT = Duration.ofHours(24);

    private final AgentClient agent;

    /** Constructor used by the Lambda runtime. */
    public DocumentReviewWorkflow() {
        this(new AgentClient(SharedClients.AGENT_CORE, System.getenv("AGENT_RUNTIME_ARN")));
    }

    /** Constructor used by tests, which supply a stand-in agent. */
    DocumentReviewWorkflow(AgentClient agent) {
        this.agent = agent;
    }

    @Override
    public ReviewResult handleRequest(ReviewRequest request, DurableContext ctx) {
        String documentId = request.documentId();
        ctx.getLogger().info("Starting review of document " + documentId);

        // Step 1 - the agent drafts a summary for the reviewer.
        String draft = ctx.step("analyze-document", String.class,
                stepCtx -> agent.invoke(documentId, "analyze", request.documentText(), null, null));

        // Step 2 - suspend until a human decides. The submitter runs as a step, so the SDK retries
        // it if it fails; here it simply publishes the callback ID for the reviewer to pick up.
        Decision decision;
        try {
            decision = ctx.waitForCallback("await-human-review", Decision.class,
                    (callbackId, stepCtx) -> {},
                    WaitForCallbackConfig.builder()
                            .callbackConfig(CallbackConfig.builder()
                                    .timeout(APPROVAL_TIMEOUT)
                                    .build())
                            .build());
        } catch (CallbackTimeoutException e) {
            ctx.getLogger().warn("No decision within " + APPROVAL_TIMEOUT + " for " + documentId);
            return ReviewResult.expired(documentId, draft);
        }

        if (!decision.isApproved()) {
            ctx.getLogger().info("Document " + documentId + " was rejected");
            // A rejection is a completed review, not a failure - see Decision's javadoc.
            return ReviewResult.rejected(documentId, draft, decision.comments());
        }

        // Step 3 - the agent produces the final copy, reusing the same AgentCore session so it
        // still has the analyze turn in context.
        String finalSummary = ctx.step("finalize-document", String.class,
                stepCtx -> agent.invoke(documentId, "finalize", null, draft, decision.comments()));

        ctx.getLogger().info("Review of document " + documentId + " complete");
        return ReviewResult.approved(documentId, draft, finalSummary, decision.comments());
    }

    /** Holder so the AgentCore client is created once per environment, and never in unit tests. */
    private static final class SharedClients {
        static final BedrockAgentCoreClient AGENT_CORE = BedrockAgentCoreClient.create();
    }
}
