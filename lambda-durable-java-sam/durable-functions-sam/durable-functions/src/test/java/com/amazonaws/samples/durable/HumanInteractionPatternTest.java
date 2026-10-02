package com.amazonaws.samples.durable;

import static org.junit.jupiter.api.Assertions.*;

import java.util.Map;

import org.junit.jupiter.api.Test;
import software.amazon.lambda.durable.TypeToken;
import software.amazon.lambda.durable.model.ExecutionStatus;
import software.amazon.lambda.durable.testing.LocalDurableTestRunner;

import com.amazonaws.samples.durable.humaninteraction.ApprovalWorkflowHandler;

class HumanInteractionPatternTest {

    private static final TypeToken<Map<String, Object>> MAP_TYPE = new TypeToken<>() {};

    @Test
    void completesWhenCallbackApproved() {
        var handler = new ApprovalWorkflowHandler();
        var runner = LocalDurableTestRunner.create(MAP_TYPE, handler);

        Map<String, Object> input = Map.of(
                "requestId", "REQ-TEST-001",
                "amount", 5000.00,
                "requestor", "employee@example.com"
        );

        var result = runner.run(input);
        assertEquals(ExecutionStatus.PENDING, result.getStatus());

        String callbackId = runner.getCallbackId("wait-for-approval");
        assertNotNull(callbackId);

        runner.completeCallback(callbackId,
                "{\"decision\":\"APPROVED\",\"approver\":\"manager@example.com\"}");

        result = runner.runUntilComplete(input);

        assertEquals(ExecutionStatus.SUCCEEDED, result.getStatus());
        Map<String, Object> output = result.getResult(Map.class);
        assertEquals("HUMAN_INTERACTION", output.get("pattern"));
        assertEquals("COMPLETED", output.get("status"));
        assertEquals("manager@example.com", output.get("approvedBy"));
    }

    @Test
    void handlesCallbackRejection() {
        var handler = new ApprovalWorkflowHandler();
        var runner = LocalDurableTestRunner.create(MAP_TYPE, handler);

        Map<String, Object> input = Map.of(
                "requestId", "REQ-TEST-002",
                "amount", 15000.00,
                "requestor", "employee@example.com"
        );

        var result = runner.run(input);
        assertEquals(ExecutionStatus.PENDING, result.getStatus());

        String callbackId = runner.getCallbackId("wait-for-approval");
        assertNotNull(callbackId);

        runner.failCallback(callbackId, software.amazon.awssdk.services.lambda.model.ErrorObject.builder()
                .errorType("Rejected")
                .errorMessage("Budget exceeded policy limit")
                .build());

        result = runner.runUntilComplete(input);

        assertEquals(ExecutionStatus.SUCCEEDED, result.getStatus());
        Map<String, Object> output = result.getResult(Map.class);
        assertEquals("HUMAN_INTERACTION", output.get("pattern"));
        assertEquals("REJECTED", output.get("status"));
    }

    @Test
    void requiresVpApprovalForHighAmounts() {
        var handler = new ApprovalWorkflowHandler();
        var runner = LocalDurableTestRunner.create(MAP_TYPE, handler);

        Map<String, Object> input = Map.of(
                "requestId", "REQ-TEST-003",
                "amount", 25000.00,
                "requestor", "employee@example.com"
        );

        var result = runner.run(input);
        assertEquals(ExecutionStatus.PENDING, result.getStatus());

        var prepareOp = result.getOperation("prepare-approval");
        assertNotNull(prepareOp);
    }
}
