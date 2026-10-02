package com.amazonaws.samples.durable;

import static org.junit.jupiter.api.Assertions.*;

import java.util.Map;

import org.junit.jupiter.api.Test;
import software.amazon.awssdk.services.lambda.model.OperationStatus;
import software.amazon.lambda.durable.TypeToken;
import software.amazon.lambda.durable.model.ExecutionStatus;
import software.amazon.lambda.durable.testing.LocalDurableTestRunner;

import com.amazonaws.samples.durable.errorhandling.ResilientPaymentHandler;

class ErrorHandlingPatternTest {

    private static final TypeToken<Map<String, Object>> MAP_TYPE = new TypeToken<>() {};

    @Test
    void completesSuccessfullyOnHappyPath() {
        var handler = new ResilientPaymentHandler();
        var runner = LocalDurableTestRunner.create(MAP_TYPE, handler);

        Map<String, Object> input = Map.of(
                "orderId", "ORD-TEST-001",
                "amount", 199.99,
                "simulateInventoryFailure", false
        );

        var result = runner.runUntilComplete(input);

        assertEquals(ExecutionStatus.SUCCEEDED, result.getStatus());

        Map<String, Object> output = result.getResult(Map.class);
        assertEquals("ERROR_HANDLING", output.get("pattern"));
        assertEquals("COMPLETED", output.get("status"));
        assertNotNull(output.get("transactionId"));
        assertNotNull(output.get("reservationId"));
    }

    @Test
    void inventoryFailureResultsInFailedExecution() {
        var handler = new ResilientPaymentHandler();
        var runner = LocalDurableTestRunner.create(MAP_TYPE, handler);

        Map<String, Object> input = Map.of(
                "orderId", "ORD-TEST-002",
                "amount", 199.99,
                "simulateInventoryFailure", true
        );

        var result = runner.runUntilComplete(input);

        assertEquals(ExecutionStatus.FAILED, result.getStatus());

        var inventoryOp = result.getOperation("reserve-inventory");
        assertNotNull(inventoryOp);
        assertEquals(OperationStatus.FAILED, inventoryOp.getStatus());
    }

    @Test
    void paymentSucceedsBeforeInventoryFails() {
        var handler = new ResilientPaymentHandler();
        var runner = LocalDurableTestRunner.create(MAP_TYPE, handler);

        Map<String, Object> input = Map.of(
                "orderId", "ORD-TEST-003",
                "amount", 50.00,
                "simulateInventoryFailure", true
        );

        var result = runner.runUntilComplete(input);

        var paymentOp = result.getOperation("charge-payment");
        assertNotNull(paymentOp);
        assertEquals(OperationStatus.SUCCEEDED, paymentOp.getStatus());
    }

    @Test
    void retriesPaymentOnTransientFailure() {
        var handler = new ResilientPaymentHandler();
        var runner = LocalDurableTestRunner.create(MAP_TYPE, handler);

        Map<String, Object> input = Map.of(
                "orderId", "ORD-TEST-004",
                "amount", 75.00,
                "simulateInventoryFailure", false
        );

        var result = runner.runUntilComplete(input);

        assertEquals(ExecutionStatus.SUCCEEDED, result.getStatus());

        var paymentOp = result.getOperation("charge-payment");
        assertNotNull(paymentOp);
        assertTrue(paymentOp.getAttempt() >= 1, "Payment should have retried at least once");
    }
}
