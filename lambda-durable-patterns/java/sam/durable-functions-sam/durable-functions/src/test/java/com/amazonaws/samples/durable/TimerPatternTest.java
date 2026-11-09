package com.amazonaws.samples.durable;

import static org.junit.jupiter.api.Assertions.*;

import java.util.Map;

import org.junit.jupiter.api.Test;
import software.amazon.awssdk.services.lambda.model.OperationType;
import software.amazon.lambda.durable.TypeToken;
import software.amazon.lambda.durable.model.ExecutionStatus;
import software.amazon.lambda.durable.testing.LocalDurableTestRunner;

import com.amazonaws.samples.durable.timer.ScheduledReminderHandler;

class TimerPatternTest {

    private static final TypeToken<Map<String, Object>> MAP_TYPE = new TypeToken<>() {};

    @Test
    void completesWithWaitsAdvancedAutomatically() {
        var handler = new ScheduledReminderHandler();
        var runner = LocalDurableTestRunner.create(MAP_TYPE, handler);

        Map<String, Object> input = Map.of(
                "taskId", "TASK-TEST-001",
                "assignee", "dev@example.com",
                "reminderIntervalSeconds", 30,
                "escalationSeconds", 60
        );

        var result = runner.runUntilComplete(input);

        assertEquals(ExecutionStatus.SUCCEEDED, result.getStatus());

        Map<String, Object> output = result.getResult(Map.class);
        assertEquals("TIMER", output.get("pattern"));
        assertEquals("ESCALATED", output.get("status"));
        assertEquals("TASK-TEST-001", output.get("taskId"));
    }

    @Test
    void includesWaitOperationsInHistory() {
        var handler = new ScheduledReminderHandler();
        var runner = LocalDurableTestRunner.create(MAP_TYPE, handler);

        Map<String, Object> input = Map.of(
                "taskId", "TASK-TEST-002",
                "assignee", "dev@example.com",
                "reminderIntervalSeconds", 10,
                "escalationSeconds", 20
        );

        var result = runner.runUntilComplete(input);

        var waitNames = result.getOperations().stream()
                .filter(op -> op.getType() == OperationType.WAIT)
                .map(op -> op.getName())
                .toList();

        assertTrue(waitNames.contains("first-reminder-delay"), "Should have first-reminder-delay wait");
        assertTrue(waitNames.contains("escalation-delay"), "Should have escalation-delay wait");
        assertTrue(waitNames.size() >= 2, "Should have at least 2 waits");
    }

    @Test
    void escalatesToManager() {
        var handler = new ScheduledReminderHandler();
        var runner = LocalDurableTestRunner.create(MAP_TYPE, handler);

        Map<String, Object> input = Map.of(
                "taskId", "TASK-TEST-003",
                "assignee", "dev@example.com",
                "reminderIntervalSeconds", 5,
                "escalationSeconds", 10
        );

        var result = runner.runUntilComplete(input);

        assertEquals(ExecutionStatus.SUCCEEDED, result.getStatus());

        Map<String, Object> output = result.getResult(Map.class);
        assertEquals("manager@example.com", output.get("escalatedTo"));
    }
}
