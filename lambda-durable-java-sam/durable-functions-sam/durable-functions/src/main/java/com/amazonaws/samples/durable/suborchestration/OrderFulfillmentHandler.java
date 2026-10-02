package com.amazonaws.samples.durable.suborchestration;

import java.time.Duration;
import java.util.List;
import java.util.Map;

import com.amazonaws.samples.durable.models.SnsEventParser;
import software.amazon.lambda.durable.DurableContext;
import software.amazon.lambda.durable.DurableFuture;
import software.amazon.lambda.durable.DurableHandler;

/**
 * PATTERN: Sub-Orchestration (Child Contexts)
 *
 * Demonstrates runInChildContext() for organizing complex workflows into
 * isolated, reusable sub-workflows. Each child context has its own operation
 * namespace and checkpoints results as a single unit.
 *
 * Also demonstrates concurrent child contexts using runInChildContextAsync().
 *
 * Use cases:
 * - Breaking complex workflows into logical sub-workflows
 * - Running independent sub-workflows concurrently
 * - Reusable workflow components
 *
 * Flow: Order Received -> [Payment Sub-workflow || Inventory Sub-workflow] -> Shipping Sub-workflow -> Complete
 */
public class OrderFulfillmentHandler extends DurableHandler<Map<String, Object>, Map<String, Object>> {

    @Override
    public Map<String, Object> handleRequest(Map<String, Object> rawEvent, DurableContext context) {
        Map<String, Object> event = SnsEventParser.extractMessage(rawEvent);
        context.getLogger().info("Starting order fulfillment orchestration");

        String orderId = (String) event.getOrDefault("orderId", "ORD-" + System.currentTimeMillis());
        double amount = ((Number) event.getOrDefault("amount", 149.99)).doubleValue();
        String customerId = (String) event.getOrDefault("customerId", "CUST-001");

        // Step 1: Order validation (in main context)
        Map<String, Object> orderDetails = context.step("validate-order", Map.class, stepCtx -> {
            stepCtx.getLogger().info("Validating order: " + orderId);
            return Map.of(
                    "orderId", orderId,
                    "customerId", customerId,
                    "amount", amount,
                    "status", "VALIDATED"
            );
        });

        // Step 2: Run Payment and Inventory sub-workflows CONCURRENTLY
        // Each runs in its own isolated child context
        DurableFuture<Map<String, Object>> paymentFuture = context.runInChildContextAsync(
                "payment-workflow", (Class<Map<String, Object>>) (Class<?>) Map.class,
                child -> processPayment(child, orderId, amount)
        );

        DurableFuture<Map<String, Object>> inventoryFuture = context.runInChildContextAsync(
                "inventory-workflow", (Class<Map<String, Object>>) (Class<?>) Map.class,
                child -> reserveInventory(child, orderId, event)
        );

        // Wait for both concurrent sub-workflows to complete
        DurableFuture.allOf(paymentFuture, inventoryFuture);
        Map<String, Object> paymentResult = paymentFuture.get();
        Map<String, Object> inventoryResult = inventoryFuture.get();

        context.getLogger().info("Payment and inventory sub-workflows completed");

        // Step 3: Shipping sub-workflow (sequential, depends on previous results)
        Map<String, Object> shippingResult = context.runInChildContext(
                "shipping-workflow", (Class<Map<String, Object>>) (Class<?>) Map.class,
                child -> processShipping(child, orderId, inventoryResult)
        );

        // Step 4: Notification sub-workflow
        Map<String, Object> notificationResult = context.runInChildContext(
                "notification-workflow", (Class<Map<String, Object>>) (Class<?>) Map.class,
                child -> sendNotifications(child, orderId, customerId, shippingResult)
        );

        return Map.of(
                "pattern", "SUB_ORCHESTRATION",
                "orderId", orderId,
                "status", "FULFILLED",
                "payment", paymentResult,
                "inventory", inventoryResult,
                "shipping", shippingResult,
                "notification", notificationResult
        );
    }

    private Map<String, Object> processPayment(DurableContext child, String orderId, double amount) {
        // Sub-workflow with multiple steps, isolated in its own context
        Map<String, Object> authorization = child.step("authorize-card", Map.class, stepCtx -> {
            stepCtx.getLogger().info("Authorizing payment for order: " + orderId);
            return Map.of(
                    "authCode", "AUTH-" + orderId,
                    "amount", amount,
                    "status", "AUTHORIZED"
            );
        });

        child.wait("fraud-check-delay", Duration.ofSeconds(2));

        Map<String, Object> fraudCheck = child.step("fraud-check", Map.class, stepCtx -> {
            stepCtx.getLogger().info("Running fraud check for: " + authorization.get("authCode"));
            return Map.of(
                    "authCode", authorization.get("authCode"),
                    "fraudScore", 0.05,
                    "passed", true
            );
        });

        return child.step("capture-payment", Map.class, stepCtx -> {
            stepCtx.getLogger().info("Capturing payment: " + authorization.get("authCode"));
            return Map.of(
                    "transactionId", "TXN-" + orderId,
                    "authCode", authorization.get("authCode"),
                    "amount", amount,
                    "status", "CAPTURED"
            );
        });
    }

    private Map<String, Object> reserveInventory(DurableContext child, String orderId, Map<String, Object> event) {
        Map<String, Object> availability = child.step("check-availability", Map.class, stepCtx -> {
            stepCtx.getLogger().info("Checking inventory availability for order: " + orderId);
            return Map.of(
                    "orderId", orderId,
                    "available", true,
                    "warehouse", "WAREHOUSE-EAST-1"
            );
        });

        return child.step("reserve-stock", Map.class, stepCtx -> {
            stepCtx.getLogger().info("Reserving stock in: " + availability.get("warehouse"));
            return Map.of(
                    "reservationId", "RES-" + orderId,
                    "warehouse", availability.get("warehouse"),
                    "status", "RESERVED"
            );
        });
    }

    private Map<String, Object> processShipping(DurableContext child, String orderId, Map<String, Object> inventoryResult) {
        Map<String, Object> label = child.step("create-shipping-label", Map.class, stepCtx -> {
            stepCtx.getLogger().info("Creating shipping label for order: " + orderId);
            return Map.of(
                    "labelId", "LBL-" + orderId,
                    "warehouse", inventoryResult.get("warehouse"),
                    "carrier", "EXPRESS-SHIPPING"
            );
        });

        child.step("schedule-pickup", Map.class, stepCtx -> {
            stepCtx.getLogger().info("Scheduling pickup from: " + label.get("warehouse"));
            return Map.of("pickupScheduled", true, "estimatedPickup", "2 hours");
        });

        return child.step("generate-tracking", Map.class, stepCtx -> {
            stepCtx.getLogger().info("Generating tracking number");
            return Map.of(
                    "trackingNumber", "TRACK-" + orderId,
                    "carrier", label.get("carrier"),
                    "estimatedDelivery", "2-3 business days",
                    "status", "LABEL_CREATED"
            );
        });
    }

    private Map<String, Object> sendNotifications(DurableContext child, String orderId, String customerId,
                                                   Map<String, Object> shippingResult) {
        child.step("send-order-confirmation", String.class, stepCtx -> {
            stepCtx.getLogger().info("Sending order confirmation to customer: " + customerId);
            return "Order confirmation sent";
        });

        child.step("send-shipping-notification", String.class, stepCtx -> {
            stepCtx.getLogger().info("Sending shipping notification with tracking: " + shippingResult.get("trackingNumber"));
            return "Shipping notification sent";
        });

        return child.step("notification-summary", Map.class, stepCtx -> {
            return Map.of(
                    "orderId", orderId,
                    "customerId", customerId,
                    "notificationsSent", 2,
                    "trackingNumber", shippingResult.get("trackingNumber")
            );
        });
    }
}
