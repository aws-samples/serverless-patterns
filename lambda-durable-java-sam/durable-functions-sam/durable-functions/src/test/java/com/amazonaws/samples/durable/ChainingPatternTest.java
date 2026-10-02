package com.amazonaws.samples.durable;

import static org.junit.jupiter.api.Assertions.*;

import java.util.Map;

import org.junit.jupiter.api.Test;
import software.amazon.awssdk.services.lambda.model.OperationType;
import software.amazon.lambda.durable.TypeToken;
import software.amazon.lambda.durable.model.ExecutionStatus;
import software.amazon.lambda.durable.testing.LocalDurableTestRunner;

import com.amazonaws.samples.durable.chaining.OrderProcessingHandler;

class ChainingPatternTest {

    private static final TypeToken<Map<String, Object>> MAP_TYPE = new TypeToken<>() {};

    @Test
    void executesAllStepsInSequence() {
        var handler = new OrderProcessingHandler();
        var runner = LocalDurableTestRunner.create(MAP_TYPE, handler);

        Map<String, Object> input = Map.of(
                "orderId", "ORD-TEST-001",
                "totalAmount", 299.99,
                "customerId", "CUST-001",
                "shippingAddress", "123 Main St"
        );

        var result = runner.runUntilComplete(input);

        assertEquals(ExecutionStatus.SUCCEEDED, result.getStatus());

        Map<String, Object> output = result.getResult(Map.class);
        assertEquals("CHAINING", output.get("pattern"));
        assertEquals("COMPLETED", output.get("finalStatus"));
        assertEquals("ORD-TEST-001", output.get("orderId"));
        assertNotNull(output.get("trackingNumber"));
        assertNotNull(output.get("transactionId"));
    }

    @Test
    void executesAllFiveSteps() {
        var handler = new OrderProcessingHandler();
        var runner = LocalDurableTestRunner.create(MAP_TYPE, handler);

        Map<String, Object> input = Map.of(
                "orderId", "ORD-TEST-002",
                "totalAmount", 100.00,
                "customerId", "CUST-002"
        );

        var result = runner.runUntilComplete(input);

        var stepNames = result.getOperations().stream()
                .filter(op -> op.getType() == OperationType.STEP)
                .map(op -> op.getName())
                .toList();

        assertTrue(stepNames.contains("validate-order"));
        assertTrue(stepNames.contains("reserve-inventory"));
        assertTrue(stepNames.contains("process-payment"));
        assertTrue(stepNames.contains("ship-order"));
        assertTrue(stepNames.contains("notify-customer"));
        assertEquals(5, stepNames.size());
    }

    @Test
    void failsOnInvalidAmount() {
        var handler = new OrderProcessingHandler();
        var runner = LocalDurableTestRunner.create(MAP_TYPE, handler);

        Map<String, Object> input = Map.of(
                "orderId", "ORD-TEST-003",
                "totalAmount", -10.00,
                "customerId", "CUST-003"
        );

        var result = runner.runUntilComplete(input);

        assertEquals(ExecutionStatus.FAILED, result.getStatus());
        assertTrue(result.getError().isPresent());
    }
}
