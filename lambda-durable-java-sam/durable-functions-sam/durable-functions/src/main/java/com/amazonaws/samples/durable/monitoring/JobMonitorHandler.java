package com.amazonaws.samples.durable.monitoring;

import java.time.Duration;
import java.util.Map;

import com.amazonaws.samples.durable.models.SnsEventParser;
import software.amazon.lambda.durable.DurableContext;
import software.amazon.lambda.durable.DurableHandler;
import software.amazon.lambda.durable.TypeToken;
import software.amazon.lambda.durable.config.WaitForConditionConfig;
import software.amazon.lambda.durable.model.WaitForConditionResult;
import software.amazon.lambda.durable.retry.JitterStrategy;
import software.amazon.lambda.durable.retry.WaitStrategies;
import software.amazon.lambda.durable.retry.WaitForConditionWaitStrategy;

/**
 * PATTERN: Monitoring / Polling
 *
 * Demonstrates the waitForCondition operation which polls an external
 * system on a schedule until a terminal condition is reached. The function
 * suspends between polling attempts without consuming compute.
 *
 * Use case: Monitor a long-running batch job, waiting for it to complete.
 *
 * Flow: Start monitoring -> Poll for status -> (suspend between polls) -> Return final status
 */
public class JobMonitorHandler extends DurableHandler<Map<String, Object>, Map<String, Object>> {

    private static int pollCount = 0;

    @Override
    public Map<String, Object> handleRequest(Map<String, Object> rawEvent, DurableContext context) {
        Map<String, Object> event = SnsEventParser.extractMessage(rawEvent);
        context.getLogger().info("Starting job monitor");

        String jobId = (String) event.getOrDefault("jobId", "JOB-" + System.currentTimeMillis());
        int maxPolls = ((Number) event.getOrDefault("maxPolls", 5)).intValue();

        // Step 1: Submit or acknowledge the job
        Map<String, Object> jobInfo = context.step("acknowledge-job", Map.class, stepCtx -> {
            stepCtx.getLogger().info("Acknowledging job: " + jobId);
            return Map.of(
                    "jobId", jobId,
                    "status", "SUBMITTED",
                    "submittedAt", java.time.Instant.now().toString()
            );
        });

        // Step 2: Use waitForCondition to poll until job completes
        // The function suspends between each poll - no compute charges during waits
        WaitForConditionWaitStrategy<Map<String, Object>> strategy = (state, attempt) -> {
            if (attempt >= maxPolls) {
                throw new RuntimeException("Job monitoring timed out after " + maxPolls + " attempts");
            }
            // Exponential backoff: 5s, 10s, 20s, 40s...
            long delaySeconds = Math.min(5L * (long) Math.pow(2, attempt - 1), 60);
            return Duration.ofSeconds(delaySeconds);
        };

        Map<String, Object> initialState = Map.of(
                "jobId", jobId,
                "status", "SUBMITTED",
                "attempts", 0,
                "done", false
        );

        WaitForConditionConfig<Map<String, Object>> config = WaitForConditionConfig
                .<Map<String, Object>>builder()
                .initialState(initialState)
                .waitStrategy(strategy)
                .build();

        Map<String, Object> finalJobState = context.waitForCondition(
                "poll-job-status",
                new TypeToken<>() {},
                (state, stepCtx) -> {
                    int attempts = ((Number) state.getOrDefault("attempts", 0)).intValue() + 1;
                    stepCtx.getLogger().info("Polling job status, attempt: " + attempts);

                    // Simulate checking external job status
                    // In production, this would call an external API
                    String currentStatus = simulateJobStatus(attempts, maxPolls);

                    Map<String, Object> updatedState = Map.of(
                            "jobId", state.get("jobId"),
                            "status", currentStatus,
                            "attempts", attempts,
                            "done", "COMPLETED".equals(currentStatus) || "FAILED".equals(currentStatus),
                            "lastChecked", java.time.Instant.now().toString()
                    );

                    boolean isDone = "COMPLETED".equals(currentStatus) || "FAILED".equals(currentStatus);
                    if (isDone) {
                        return WaitForConditionResult.stopPolling(updatedState);
                    }
                    return WaitForConditionResult.continuePolling(updatedState);
                },
                config
        );

        // Step 3: Process the final result
        Map<String, Object> finalResult = context.step("process-job-result", Map.class, stepCtx -> {
            String status = (String) finalJobState.get("status");
            stepCtx.getLogger().info("Job completed with status: " + status);
            return Map.of(
                    "jobId", jobId,
                    "finalStatus", status,
                    "totalAttempts", finalJobState.get("attempts"),
                    "completedAt", java.time.Instant.now().toString()
            );
        });

        return Map.of(
                "pattern", "MONITORING",
                "jobId", jobId,
                "status", finalResult.get("finalStatus"),
                "pollAttempts", finalResult.get("totalAttempts")
        );
    }

    private String simulateJobStatus(int attempt, int maxPolls) {
        // Simulate a job that completes after a few polling attempts
        if (attempt >= maxPolls - 1) {
            return "COMPLETED";
        } else if (attempt == 1) {
            return "RUNNING";
        } else {
            return "IN_PROGRESS";
        }
    }
}
