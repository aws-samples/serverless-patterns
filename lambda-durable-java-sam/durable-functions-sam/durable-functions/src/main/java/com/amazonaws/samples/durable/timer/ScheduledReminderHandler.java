package com.amazonaws.samples.durable.timer;

import java.time.Duration;
import java.util.Map;

import com.amazonaws.samples.durable.models.SnsEventParser;
import software.amazon.lambda.durable.DurableContext;
import software.amazon.lambda.durable.DurableFuture;
import software.amazon.lambda.durable.DurableHandler;

/**
 * PATTERN: Timer / Scheduled Delays
 *
 * Demonstrates the wait() operation which suspends execution for a specified
 * duration WITHOUT consuming compute. The function exits, and the backend
 * automatically resumes it when the wait completes.
 *
 * Use cases:
 * - Scheduled reminders
 * - Rate limiting between API calls
 * - Delayed retry patterns
 * - SLA-based escalations
 *
 * Flow: Process event -> Wait (suspend) -> Send reminder -> Wait -> Escalate
 */
public class ScheduledReminderHandler extends DurableHandler<Map<String, Object>, Map<String, Object>> {

    @Override
    public Map<String, Object> handleRequest(Map<String, Object> rawEvent, DurableContext context) {
        Map<String, Object> event = SnsEventParser.extractMessage(rawEvent);
        context.getLogger().info("Starting scheduled reminder workflow");

        String taskId = (String) event.getOrDefault("taskId", "TASK-001");
        String assignee = (String) event.getOrDefault("assignee", "developer@example.com");
        int reminderIntervalSeconds = ((Number) event.getOrDefault("reminderIntervalSeconds", 30)).intValue();
        int escalationSeconds = ((Number) event.getOrDefault("escalationSeconds", 60)).intValue();

        // Step 1: Create the task assignment
        Map<String, Object> taskAssignment = context.step("create-task", Map.class, stepCtx -> {
            stepCtx.getLogger().info("Creating task assignment: " + taskId + " -> " + assignee);
            return Map.of(
                    "taskId", taskId,
                    "assignee", assignee,
                    "status", "ASSIGNED",
                    "createdAt", java.time.Instant.now().toString()
            );
        });

        // Step 2: Send initial notification
        context.step("send-initial-notification", String.class, stepCtx -> {
            stepCtx.getLogger().info("Sending initial task notification to: " + assignee);
            return "Initial notification sent to " + assignee;
        });

        // Step 3: Wait for the first reminder interval
        // Function SUSPENDS here - no compute charges during this wait
        context.getLogger().info("Waiting " + reminderIntervalSeconds + " seconds before first reminder");
        context.wait("first-reminder-delay", Duration.ofSeconds(reminderIntervalSeconds));

        // Step 4: Send first reminder
        context.step("send-first-reminder", String.class, stepCtx -> {
            stepCtx.getLogger().info("Sending first reminder to: " + assignee);
            return "First reminder sent";
        });

        // Step 5: Wait for escalation period
        context.getLogger().info("Waiting " + escalationSeconds + " seconds before escalation");
        context.wait("escalation-delay", Duration.ofSeconds(escalationSeconds));

        // Step 6: Escalate to manager
        Map<String, Object> escalation = context.step("escalate-to-manager", Map.class, stepCtx -> {
            stepCtx.getLogger().info("Escalating task " + taskId + " to manager");
            return Map.of(
                    "taskId", taskId,
                    "originalAssignee", assignee,
                    "escalatedTo", "manager@example.com",
                    "reason", "Task not completed within SLA",
                    "escalatedAt", java.time.Instant.now().toString()
            );
        });

        // Step 7: Demonstrate async wait with concurrent step (minimum duration pattern)
        DurableFuture<Void> minimumWait = context.waitAsync("minimum-processing-time", Duration.ofSeconds(5));
        DurableFuture<String> processingFuture = context.stepAsync("final-processing", String.class, stepCtx -> {
            stepCtx.getLogger().info("Running final processing (guaranteed minimum 5s total)");
            return "Final processing complete";
        });

        // Both must complete - ensures at least 5 seconds elapsed
        minimumWait.get();
        String processingResult = processingFuture.get();

        // Step 8: Final summary
        return Map.of(
                "pattern", "TIMER",
                "taskId", taskId,
                "status", "ESCALATED",
                "assignee", assignee,
                "escalatedTo", escalation.get("escalatedTo"),
                "totalWaitTime", (reminderIntervalSeconds + escalationSeconds + 5) + " seconds"
        );
    }
}
