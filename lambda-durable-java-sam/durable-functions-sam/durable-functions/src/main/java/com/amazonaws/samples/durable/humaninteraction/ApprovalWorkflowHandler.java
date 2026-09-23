package com.amazonaws.samples.durable.humaninteraction;

import java.time.Duration;
import java.util.Map;

import com.amazonaws.samples.durable.models.SnsEventParser;
import software.amazon.lambda.durable.DurableCallbackFuture;
import software.amazon.lambda.durable.DurableContext;
import software.amazon.lambda.durable.DurableHandler;
import software.amazon.lambda.durable.config.CallbackConfig;
import software.amazon.lambda.durable.exception.CallbackFailedException;

/**
 * PATTERN: Human Interaction (Approval Workflow)
 *
 * Demonstrates waiting for external human input using callbacks.
 * The function suspends (no compute charges) while waiting for
 * a human to approve or reject a request. Uses the callback mechanism
 * where an external system calls SendDurableExecutionCallbackSuccess
 * or SendDurableExecutionCallbackFailure.
 *
 * Flow: Submit Request -> Wait for Manager Approval -> Process Approved Request
 *
 * To complete the callback externally, use:
 *   aws lambda send-durable-execution-callback-success \
 *     --callback-id <callback-id> \
 *     --cli-binary-format raw-in-base64-out \
 *     --result '{"decision":"APPROVED","approver":"manager@example.com"}'
 *
 * Or to reject:
 *   aws lambda send-durable-execution-callback-failure \
 *     --callback-id <callback-id> \
 *     --error ErrorType=Rejected,ErrorMessage="Budget exceeded"
 */
public class ApprovalWorkflowHandler extends DurableHandler<Map<String, Object>, Map<String, Object>> {

    @Override
    public Map<String, Object> handleRequest(Map<String, Object> rawEvent, DurableContext context) {
        Map<String, Object> event = SnsEventParser.extractMessage(rawEvent);
        context.getLogger().info("Starting approval workflow");

        String requestId = (String) event.getOrDefault("requestId", "REQ-" + System.currentTimeMillis());
        double amount = ((Number) event.getOrDefault("amount", 5000)).doubleValue();
        String requestor = (String) event.getOrDefault("requestor", "employee@example.com");

        // Step 1: Validate and prepare the approval request
        Map<String, Object> approvalRequest = context.step("prepare-approval", Map.class, stepCtx -> {
            stepCtx.getLogger().info("Preparing approval request: " + requestId);
            String approvalLevel = amount > 10000 ? "VP" : "MANAGER";
            return Map.of(
                    "requestId", requestId,
                    "amount", amount,
                    "requestor", requestor,
                    "approvalLevel", approvalLevel,
                    "status", "PENDING_APPROVAL"
            );
        });

        // Step 2: Send notification to approver (simulated)
        context.step("notify-approver", String.class, stepCtx -> {
            stepCtx.getLogger().info("Sending approval notification to: " + approvalRequest.get("approvalLevel"));
            return "Notification sent to " + approvalRequest.get("approvalLevel");
        });

        // Step 3: Wait for human approval using callback
        // The function SUSPENDS here - no compute charges while waiting
        Map<String, String> approvalDecision;
        try {
            CallbackConfig callbackConfig = CallbackConfig.builder()
                    .timeout(Duration.ofHours(72))
                    .heartbeatTimeout(Duration.ofHours(24))
                    .build();

            DurableCallbackFuture<Map<String, String>> callback =
                    context.createCallback("wait-for-approval", (Class<Map<String, String>>) (Class<?>) Map.class, callbackConfig);

            // Log the callback ID so the approver can use it
            context.getLogger().info("Approval callback created. Callback ID: " + callback.callbackId());
            context.getLogger().info("To approve, run: aws lambda send-durable-execution-callback-success "
                    + "--callback-id " + callback.callbackId()
                    + " --cli-binary-format raw-in-base64-out"
                    + " --result '{\"decision\":\"APPROVED\",\"approver\":\"manager@example.com\"}'");

            // Execution suspends here until the external system calls back
            approvalDecision = callback.get();
            context.getLogger().info("Received approval decision: " + approvalDecision.get("decision"));

        } catch (CallbackFailedException e) {
            context.getLogger().info("Approval was rejected: " + e.getMessage());
            return Map.of(
                    "pattern", "HUMAN_INTERACTION",
                    "requestId", requestId,
                    "status", "REJECTED",
                    "reason", e.getMessage()
            );
        }

        // Step 4: Process the approved request
        Map<String, Object> processingResult = context.step("process-approved-request", Map.class, stepCtx -> {
            stepCtx.getLogger().info("Processing approved request: " + requestId);
            return Map.of(
                    "requestId", requestId,
                    "status", "PROCESSED",
                    "approvedBy", approvalDecision.getOrDefault("approver", "unknown"),
                    "decision", approvalDecision.getOrDefault("decision", "APPROVED"),
                    "processedAmount", amount
            );
        });

        // Step 5: Send confirmation
        context.step("send-confirmation", String.class, stepCtx -> {
            stepCtx.getLogger().info("Sending confirmation to requestor: " + requestor);
            return "Confirmation sent";
        });

        return Map.of(
                "pattern", "HUMAN_INTERACTION",
                "requestId", requestId,
                "status", "COMPLETED",
                "approvedBy", processingResult.get("approvedBy"),
                "amount", amount
        );
    }
}
