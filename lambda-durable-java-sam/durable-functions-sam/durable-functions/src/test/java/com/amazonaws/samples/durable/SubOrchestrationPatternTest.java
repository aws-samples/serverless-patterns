package com.amazonaws.samples.durable;

import static org.junit.jupiter.api.Assertions.*;

import java.util.List;
import java.util.Map;

import org.junit.jupiter.api.Test;
import software.amazon.awssdk.services.lambda.model.OperationType;
import software.amazon.lambda.durable.TypeToken;
import software.amazon.lambda.durable.model.ExecutionStatus;
import software.amazon.lambda.durable.testing.LocalDurableTestRunner;

import com.amazonaws.samples.durable.suborchestration.OrderFulfillmentHandler;

class SubOrchestrationPatternTest {

    private static final TypeToken<Map<String, Object>> MAP_TYPE = new TypeToken<>() {};

    @Test
    void completesFullOrderFulfillment() {
        var handler = new OrderFulfillmentHandler();
        var runner = LocalDurableTestRunner.create(MAP_TYPE, handler);

        Map<String, Object> input = Map.of(
                "orderId", "ORD-TEST-001",
                "customerId", "CUST-TEST-001",
                "amount", 499.99,
                "items", List.of(
                        Map.of("productId", "PROD-001", "name", "Widget", "qty", 2)
                )
        );

        var result = runner.runUntilComplete(input);

        assertEquals(ExecutionStatus.SUCCEEDED, result.getStatus());

        Map<String, Object> output = result.getResult(Map.class);
        assertEquals("SUB_ORCHESTRATION", output.get("pattern"));
        assertEquals("FULFILLED", output.get("status"));
        assertEquals("ORD-TEST-001", output.get("orderId"));
    }

    @Test
    void executesPaymentAndInventorySubWorkflowsConcurrently() {
        var handler = new OrderFulfillmentHandler();
        var runner = LocalDurableTestRunner.create(MAP_TYPE, handler);

        Map<String, Object> input = Map.of(
                "orderId", "ORD-TEST-002",
                "customerId", "CUST-TEST-002",
                "amount", 150.00
        );

        var result = runner.runUntilComplete(input);

        assertEquals(ExecutionStatus.SUCCEEDED, result.getStatus());

        var contextOps = result.getOperations().stream()
                .filter(op -> op.getType() == OperationType.CONTEXT)
                .toList();

        var contextNames = contextOps.stream().map(op -> op.getName()).toList();
        assertTrue(contextNames.contains("payment-workflow"));
        assertTrue(contextNames.contains("inventory-workflow"));
        assertTrue(contextNames.contains("shipping-workflow"));
        assertTrue(contextNames.contains("notification-workflow"));
    }

    @Test
    void producesPaymentAndShippingResults() {
        var handler = new OrderFulfillmentHandler();
        var runner = LocalDurableTestRunner.create(MAP_TYPE, handler);

        Map<String, Object> input = Map.of(
                "orderId", "ORD-TEST-003",
                "customerId", "CUST-TEST-003",
                "amount", 200.00
        );

        var result = runner.runUntilComplete(input);

        assertEquals(ExecutionStatus.SUCCEEDED, result.getStatus());

        Map<String, Object> output = result.getResult(Map.class);

        @SuppressWarnings("unchecked")
        Map<String, Object> payment = (Map<String, Object>) output.get("payment");
        assertEquals("CAPTURED", payment.get("status"));
        assertNotNull(payment.get("transactionId"));

        @SuppressWarnings("unchecked")
        Map<String, Object> shipping = (Map<String, Object>) output.get("shipping");
        assertNotNull(shipping.get("trackingNumber"));

        @SuppressWarnings("unchecked")
        Map<String, Object> inventory = (Map<String, Object>) output.get("inventory");
        assertEquals("RESERVED", inventory.get("status"));
    }
}
