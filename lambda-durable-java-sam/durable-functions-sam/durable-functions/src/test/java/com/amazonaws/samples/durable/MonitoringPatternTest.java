package com.amazonaws.samples.durable;

import static org.junit.jupiter.api.Assertions.*;

import java.util.Map;

import org.junit.jupiter.api.Test;
import software.amazon.lambda.durable.TypeToken;
import software.amazon.lambda.durable.model.ExecutionStatus;
import software.amazon.lambda.durable.testing.LocalDurableTestRunner;

import com.amazonaws.samples.durable.monitoring.JobMonitorHandler;

class MonitoringPatternTest {

    private static final TypeToken<Map<String, Object>> MAP_TYPE = new TypeToken<>() {};

    @Test
    void pollsUntilJobCompletes() {
        var handler = new JobMonitorHandler();
        var runner = LocalDurableTestRunner.create(MAP_TYPE, handler);

        Map<String, Object> input = Map.of(
                "jobId", "JOB-TEST-001",
                "jobType", "DATA_EXPORT",
                "maxPolls", 5
        );

        var result = runner.runUntilComplete(input);

        assertEquals(ExecutionStatus.SUCCEEDED, result.getStatus());

        Map<String, Object> output = result.getResult(Map.class);
        assertEquals("MONITORING", output.get("pattern"));
        assertEquals("COMPLETED", output.get("status"));
        assertEquals("JOB-TEST-001", output.get("jobId"));
    }

    @Test
    void completesWithinPollLimit() {
        var handler = new JobMonitorHandler();
        var runner = LocalDurableTestRunner.create(MAP_TYPE, handler);

        Map<String, Object> input = Map.of(
                "jobId", "JOB-TEST-002",
                "maxPolls", 3
        );

        var result = runner.runUntilComplete(input);

        assertEquals(ExecutionStatus.SUCCEEDED, result.getStatus());

        Map<String, Object> output = result.getResult(Map.class);
        assertNotNull(output.get("pollAttempts"));
    }

    @Test
    void reportsCorrectPollAttemptCount() {
        var handler = new JobMonitorHandler();
        var runner = LocalDurableTestRunner.create(MAP_TYPE, handler);

        Map<String, Object> input = Map.of(
                "jobId", "JOB-TEST-003",
                "maxPolls", 4
        );

        var result = runner.runUntilComplete(input);

        assertEquals(ExecutionStatus.SUCCEEDED, result.getStatus());

        Map<String, Object> output = result.getResult(Map.class);
        int pollAttempts = ((Number) output.get("pollAttempts")).intValue();
        assertTrue(pollAttempts >= 2, "Should have polled at least twice");
    }
}
