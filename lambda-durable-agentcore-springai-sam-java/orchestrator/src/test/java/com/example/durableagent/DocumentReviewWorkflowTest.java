/*! Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
 *  SPDX-License-Identifier: MIT-0
 */
package com.example.durableagent;

import java.util.concurrent.atomic.AtomicInteger;

import com.example.durableagent.model.ReviewRequest;
import com.example.durableagent.model.ReviewResult;
import org.junit.jupiter.api.Test;
import software.amazon.lambda.durable.model.ExecutionStatus;
import software.amazon.lambda.durable.testing.LocalDurableTestRunner;
import software.amazon.lambda.durable.testing.TestResult;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertNotEquals;
import static org.junit.jupiter.api.Assertions.assertNotNull;
import static org.junit.jupiter.api.Assertions.assertNull;
import static org.junit.jupiter.api.Assertions.assertTrue;

/**
 * Exercises all three approval outcomes against the durable execution SDK's in-memory runner -
 * no AWS account, no deployment. The agent is replaced with a counting stand-in so the tests can
 * assert on control flow and, crucially, on replay behaviour.
 */
class DocumentReviewWorkflowTest {

    /**
     * waitForCallback expands into a child context containing a callback and a submitter step.
     * The CALLBACK operation is the "-callback" child, which is what the runner keys resume on.
     */
    private static final String CALLBACK_OP = "await-human-review-callback";

    private static final ReviewRequest REQUEST =
            new ReviewRequest("doc-001", "Q3 Budget", "Headcount increases by 4 FTE.");

    /** Counts invocations per mode, so a step re-executed on replay would be visible. */
    private static final class FakeAgent extends AgentClient {
        final AtomicInteger analyzeCalls = new AtomicInteger();
        final AtomicInteger finalizeCalls = new AtomicInteger();

        FakeAgent() {
            super(null, "arn:aws:bedrock-agentcore:us-east-1:123456789012:runtime/test");
        }

        @Override
        public String invoke(String documentId, String mode, String document, String draft, String comments) {
            if ("analyze".equals(mode)) {
                analyzeCalls.incrementAndGet();
                return "DRAFT: " + document;
            }
            finalizeCalls.incrementAndGet();
            return "FINAL: " + draft + (comments == null ? "" : " / " + comments);
        }
    }

    private record Fixture(
            LocalDurableTestRunner<ReviewRequest, ReviewResult> runner,
            FakeAgent agent) {
    }

    private static Fixture fixture() {
        FakeAgent agent = new FakeAgent();
        LocalDurableTestRunner<ReviewRequest, ReviewResult> runner =
                LocalDurableTestRunner.create(ReviewRequest.class, new DocumentReviewWorkflow(agent))
                        .withOutputType(ReviewResult.class);
        return new Fixture(runner, agent);
    }

    @Test
    void approvedReviewProducesFinalSummary() {
        Fixture f = fixture();

        // The first invocation runs the analyze step, then suspends at the callback.
        f.runner().run(REQUEST);

        // A human approves.
        f.runner().completeCallback(f.runner().getCallbackId(CALLBACK_OP),
                "{\"decision\":\"approved\",\"comments\":\"Looks good\"}");

        TestResult<ReviewResult> result = f.runner().runUntilComplete(REQUEST);

        assertEquals(ExecutionStatus.SUCCEEDED, result.getStatus());
        ReviewResult review = result.getResult();
        assertEquals("DECIDED", review.outcome());
        assertEquals("APPROVED", review.decision());
        assertEquals("DRAFT: " + REQUEST.documentText(), review.draft());
        assertTrue(review.finalSummary().startsWith("FINAL: DRAFT:"));
        assertTrue(review.finalSummary().contains("Looks good"), "reviewer comments reach the agent");

        // The heart of the durable model: the handler body ran again after the callback resumed
        // it, but the completed step was served from its checkpoint rather than re-executed.
        assertEquals(1, f.agent().analyzeCalls.get(), "analyze step re-executed on replay");
        assertEquals(1, f.agent().finalizeCalls.get());
    }

    @Test
    void rejectedReviewSkipsFinalizeStep() {
        Fixture f = fixture();
        f.runner().run(REQUEST);

        f.runner().completeCallback(f.runner().getCallbackId(CALLBACK_OP),
                "{\"decision\":\"rejected\",\"comments\":\"Needs cost breakdown\"}");

        TestResult<ReviewResult> result = f.runner().runUntilComplete(REQUEST);

        assertEquals(ExecutionStatus.SUCCEEDED, result.getStatus());
        ReviewResult review = result.getResult();
        assertEquals("DECIDED", review.outcome(), "a rejection is still a completed review");
        assertEquals("REJECTED", review.decision());
        assertNull(review.finalSummary(), "rejected reviews must not be finalized");
        assertEquals("Needs cost breakdown", review.comments());
        assertEquals(0, f.agent().finalizeCalls.get(), "finalize must be skipped on rejection");
    }

    @Test
    void timedOutApprovalIsRecorded() {
        Fixture f = fixture();
        f.runner().run(REQUEST);

        f.runner().timeoutCallback(f.runner().getCallbackId(CALLBACK_OP));

        TestResult<ReviewResult> result = f.runner().runUntilComplete(REQUEST);

        assertEquals(ExecutionStatus.SUCCEEDED, result.getStatus());
        ReviewResult review = result.getResult();
        assertEquals("EXPIRED", review.outcome());
        assertNull(review.decision(), "no decision was ever made");
        assertNotNull(review.draft(), "the draft is retained even when approval expires");
        assertEquals(0, f.agent().finalizeCalls.get());
    }

    @Test
    void sessionIdMeetsServiceMinimumAndIsStable() {
        String sessionId = AgentClient.sessionIdFor("doc-001");
        assertTrue(sessionId.length() >= 33, "AgentCore requires at least 33 characters");
        assertTrue(sessionId.startsWith("doc-review-doc-001"), "document ID stays legible in logs");
        assertEquals(sessionId, AgentClient.sessionIdFor("doc-001"),
                "must be a pure function of the document ID, or replay would change the session");
        assertNotEquals(sessionId, AgentClient.sessionIdFor("doc-002"),
                "different documents must not share a session");
    }
}
