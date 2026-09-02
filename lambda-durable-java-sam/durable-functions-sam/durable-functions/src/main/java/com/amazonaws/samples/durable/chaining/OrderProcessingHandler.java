package com.amazonaws.samples.durable.chaining;

import java.util.Map;
import java.time.Duration;

import com.amazonaws.samples.durable.models.SnsEventParser;
import software.amazon.lambda.durable.DurableContext;
import software.amazon.lambda.durable.DurableHandler;
import software.amazon.lambda.durable.config.StepConfig;
import software.amazon.lambda.durable.retry.RetryStrategies;
import software.amazon.lambda.durable.retry.JitterStrategy;

/**
 * PATTERN: Function Chaining
 *
 * Demonstrates sequential step execution where each step's output feeds
 * into the next step. The durable execution SDK checkpoints each step's
 * result so that on replay (after a wait or failure), completed steps
 * are not re-executed.
 *
 * Flow: Validate Order -> Reserve Inventory -> Process Payment -> Ship Order -> Notify Customer
 */
public class OrderProcessingHandler extends DurableHandler<Map<String, Object>, Map<String, Object>> {

    @Override
    public Map<String, Object> handleRequest(Map<String, Object> rawEvent, DurableContext context) {
        Map<String, Object> event = SnsEventParser.extractMessage(rawEvent);
        context.getLogger().info("Starting order processing chain for: " + event.get("orderId"));

        StepConfig retryConfig = StepConfig.builder()
                .retryStrategy(RetryStrategies.exponentialBackoff(
                        3, Duration.ofSeconds(2), Duration.ofSeconds(30), 2.0, JitterStrategy.FULL))
                .build();

        // Step 1: Validate the order
        Map<String, Object> validationResult = context.step("validate-order", Map.class, stepCtx -> {
            stepCtx.getLogger().info("Validating order...");
            String orderId = (String) event.get("orderId");
            double amount = ((Number) event.get("totalAmount")).doubleValue();
            if (orderId == null || orderId.isEmpty()) {
                throw new IllegalArgumentException("Order ID is required");
            }
            if (amount <= 0) {
                throw new IllegalArgumentException("Order amount must be positive");
            }
            return Map.of(
                    "orderId", orderId,
                    "status", "VALIDATED",
                    "amount", amount,
                    "customerId", event.getOrDefault("customerId", "unknown")
            );
        }, retryConfig);

        // Step 2: Reserve inventory
        Map<String, Object> inventoryResult = context.step("reserve-inventory", Map.class, stepCtx -> {
            stepCtx.getLogger().info("Reserving inventory for order: " + validationResult.get("orderId"));
            return Map.of(
                    "orderId", validationResult.get("orderId"),
                    "status", "INVENTORY_RESERVED",
                    "reservationId", "RES-" + validationResult.get("orderId"),
                    "warehouse", "WAREHOUSE-EAST-1"
            );
        }, retryConfig);

        // Step 3: Process payment
        Map<String, Object> paymentResult = context.step("process-payment", Map.class, stepCtx -> {
            stepCtx.getLogger().info("Processing payment for order: " + inventoryResult.get("orderId"));
            return Map.of(
                    "orderId", inventoryResult.get("orderId"),
                    "status", "PAYMENT_PROCESSED",
                    "transactionId", "TXN-" + System.currentTimeMillis(),
                    "amount", validationResult.get("amount")
            );
        }, retryConfig);

        // Step 4: Ship order
        Map<String, Object> shippingResult = context.step("ship-order", Map.class, stepCtx -> {
            stepCtx.getLogger().info("Shipping order: " + paymentResult.get("orderId"));
            return Map.of(
                    "orderId", paymentResult.get("orderId"),
                    "status", "SHIPPED",
                    "trackingNumber", "TRACK-" + paymentResult.get("transactionId"),
                    "estimatedDelivery", "3-5 business days"
            );
        }, retryConfig);

        // Step 5: Notify customer
        Map<String, Object> notificationResult = context.step("notify-customer", Map.class, stepCtx -> {
            stepCtx.getLogger().info("Notifying customer about shipment");
            return Map.of(
                    "orderId", shippingResult.get("orderId"),
                    "status", "CUSTOMER_NOTIFIED",
                    "trackingNumber", shippingResult.get("trackingNumber"),
                    "message", "Your order has been shipped!"
            );
        });

        context.getLogger().info("Order processing chain completed successfully");

        return Map.of(
                "pattern", "CHAINING",
                "orderId", event.get("orderId"),
                "finalStatus", "COMPLETED",
                "trackingNumber", shippingResult.get("trackingNumber"),
                "transactionId", paymentResult.get("transactionId")
        );
    }
}
