package com.example;

import software.amazon.lambda.durable.DurableContext;
import software.amazon.lambda.durable.DurableHandler;

import java.time.Duration;
import java.util.Map;
import java.util.UUID;

/**
 * Durable order processing workflow that demonstrates automatic checkpointing,
 * wait operations, and multi-step orchestration using the Java Durable Execution SDK.
 *
 * Each step is checkpointed — if the function is interrupted, it resumes from
 * the last completed step without re-executing previous work.
 */
public class OrderProcessor extends DurableHandler<Map<String, Object>, Map<String, Object>> {

    @Override
    public Map<String, Object> handleRequest(Map<String, Object> input, DurableContext ctx) {
        String orderId = (String) input.getOrDefault("orderId", UUID.randomUUID().toString());
        double amount = ((Number) input.getOrDefault("amount", 99.99)).doubleValue();

        // Step 1: Validate order
        String validation = ctx.step("validate-order", String.class, stepCtx -> {
            System.out.println("Validating order " + orderId);
            if (amount <= 0) {
                throw new IllegalArgumentException("Invalid order amount: " + amount);
            }
            return "VALIDATED";
        });

        // Step 2: Reserve inventory
        String reservationId = ctx.step("reserve-inventory", String.class, stepCtx -> {
            System.out.println("Reserving inventory for order " + orderId);
            return "RES-" + UUID.randomUUID().toString().substring(0, 8);
        });

        // Step 3: Process payment
        String paymentId = ctx.step("process-payment", String.class, stepCtx -> {
            System.out.println("Processing payment of $" + amount + " for order " + orderId);
            return "PAY-" + UUID.randomUUID().toString().substring(0, 8);
        });

        // Wait for warehouse processing (no compute charges during wait)
        ctx.wait("warehouse-processing", Duration.ofSeconds(5));

        // Step 4: Confirm shipment
        String trackingNumber = ctx.step("confirm-shipment", String.class, stepCtx -> {
            System.out.println("Confirming shipment for order " + orderId);
            return "TRACK-" + UUID.randomUUID().toString().substring(0, 8);
        });

        return Map.of(
            "orderId", orderId,
            "status", "COMPLETED",
            "validation", validation,
            "reservationId", reservationId,
            "paymentId", paymentId,
            "trackingNumber", trackingNumber
        );
    }
}
