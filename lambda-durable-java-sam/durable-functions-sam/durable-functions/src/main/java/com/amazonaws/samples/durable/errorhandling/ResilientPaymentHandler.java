package com.amazonaws.samples.durable.errorhandling;

import java.time.Duration;
import java.util.Map;

import com.amazonaws.samples.durable.models.SnsEventParser;
import software.amazon.lambda.durable.DurableContext;
import software.amazon.lambda.durable.DurableHandler;
import software.amazon.lambda.durable.config.StepConfig;
import software.amazon.lambda.durable.config.StepSemantics;
import software.amazon.lambda.durable.exception.StepFailedException;
import software.amazon.lambda.durable.exception.StepInterruptedException;
import software.amazon.lambda.durable.retry.JitterStrategy;
import software.amazon.lambda.durable.retry.RetryDecision;
import software.amazon.lambda.durable.retry.RetryStrategies;
import software.amazon.lambda.durable.retry.RetryStrategy;

/**
 * PATTERN: Error Handling and Compensation (Saga Pattern)
 *
 * Demonstrates:
 * 1. Retry strategies with exponential backoff
 * 2. Custom retry strategies with error-type filtering
 * 3. At-most-once semantics for non-idempotent operations
 * 4. Saga pattern: compensation logic when later steps fail
 * 5. Catching and handling StepFailedException
 *
 * Flow: Validate -> Charge Payment (with retries) -> Reserve Inventory
 *       If inventory fails -> Refund Payment (compensation)
 */
public class ResilientPaymentHandler extends DurableHandler<Map<String, Object>, Map<String, Object>> {

    @Override
    public Map<String, Object> handleRequest(Map<String, Object> rawEvent, DurableContext context) {
        Map<String, Object> event = SnsEventParser.extractMessage(rawEvent);
        context.getLogger().info("Starting resilient payment workflow");

        String orderId = (String) event.getOrDefault("orderId", "ORD-001");
        double amount = ((Number) event.getOrDefault("amount", 99.99)).doubleValue();
        boolean simulateInventoryFailure = Boolean.TRUE.equals(event.get("simulateInventoryFailure"));

        // Step 1: Validate with standard retry
        StepConfig validationConfig = StepConfig.builder()
                .retryStrategy(RetryStrategies.exponentialBackoff(
                        3, Duration.ofSeconds(1), Duration.ofSeconds(10), 2.0, JitterStrategy.FULL))
                .build();

        Map<String, Object> validation = context.step("validate-payment", Map.class, stepCtx -> {
            stepCtx.getLogger().info("Validating payment for order: " + orderId);
            if (amount <= 0) {
                throw new IllegalArgumentException("Invalid amount: " + amount);
            }
            return Map.of("orderId", orderId, "amount", amount, "valid", true);
        }, validationConfig);

        // Step 2: Charge payment with at-most-once semantics and custom retry
        // At-most-once ensures we never double-charge even if Lambda is interrupted
        RetryStrategy paymentRetry = (error, attempt) -> {
            // Only retry on transient errors, not business logic errors
            if (error instanceof IllegalArgumentException) {
                return RetryDecision.fail();
            }
            if (attempt >= 4) {
                return RetryDecision.fail();
            }
            return RetryDecision.retry(Duration.ofSeconds(2 * attempt));
        };

        StepConfig paymentConfig = StepConfig.builder()
                .retryStrategy(paymentRetry)
                .semantics(StepSemantics.AT_MOST_ONCE_PER_RETRY)
                .build();

        Map<String, Object> paymentResult;
        try {
            paymentResult = context.step("charge-payment", Map.class, stepCtx -> {
                stepCtx.getLogger().info("Charging payment: $" + amount + " for order: " + orderId);
                stepCtx.getLogger().info("Attempt: " + stepCtx.getAttempt());
                // Simulate transient failure on first attempt
                if (stepCtx.getAttempt() == 0) {
                    throw new RuntimeException("Payment gateway timeout - transient error");
                }
                return Map.of(
                        "orderId", orderId,
                        "transactionId", "TXN-" + orderId + "-" + System.currentTimeMillis(),
                        "amount", amount,
                        "status", "CHARGED"
                );
            }, paymentConfig);
        } catch (StepInterruptedException e) {
            // At-most-once step was interrupted - check external system
            context.getLogger().warn("Payment step interrupted - checking payment system");
            paymentResult = context.step("check-payment-status", Map.class, stepCtx -> {
                return Map.of("orderId", orderId, "status", "UNKNOWN", "requiresManualCheck", true);
            });
            return Map.of(
                    "pattern", "ERROR_HANDLING",
                    "orderId", orderId,
                    "status", "INTERRUPTED",
                    "paymentResult", paymentResult
            );
        } catch (StepFailedException e) {
            context.getLogger().info("Payment failed permanently: " + e.getMessage());
            return Map.of(
                    "pattern", "ERROR_HANDLING",
                    "orderId", orderId,
                    "status", "PAYMENT_FAILED",
                    "error", e.getErrorObject().errorMessage()
            );
        }

        // Step 3: Reserve inventory - may fail, triggering compensation
        Map<String, Object> inventoryResult;
        try {
            StepConfig inventoryConfig = StepConfig.builder()
                    .retryStrategy(RetryStrategies.exponentialBackoff(
                            2, Duration.ofSeconds(1), Duration.ofSeconds(5), 2.0, JitterStrategy.NONE))
                    .build();

            inventoryResult = context.step("reserve-inventory", Map.class, stepCtx -> {
                stepCtx.getLogger().info("Reserving inventory for order: " + orderId);
                if (simulateInventoryFailure) {
                    throw new RuntimeException("Inventory unavailable - out of stock");
                }
                return Map.of(
                        "orderId", orderId,
                        "reservationId", "INV-" + orderId,
                        "status", "RESERVED"
                );
            }, inventoryConfig);
        } catch (StepFailedException e) {
            // SAGA COMPENSATION: Inventory failed, refund the payment
            context.getLogger().info("Inventory reservation failed - initiating compensation");

            final Map<String, Object> capturedPayment = paymentResult;
            Map<String, Object> refundResult = context.step("refund-payment", Map.class, stepCtx -> {
                stepCtx.getLogger().info("Refunding payment: " + capturedPayment.get("transactionId"));
                return Map.of(
                        "orderId", orderId,
                        "originalTransactionId", capturedPayment.get("transactionId"),
                        "refundId", "REFUND-" + orderId,
                        "amount", amount,
                        "status", "REFUNDED"
                );
            });

            return Map.of(
                    "pattern", "ERROR_HANDLING",
                    "orderId", orderId,
                    "status", "COMPENSATED",
                    "reason", "Inventory unavailable",
                    "refund", refundResult
            );
        }

        return Map.of(
                "pattern", "ERROR_HANDLING",
                "orderId", orderId,
                "status", "COMPLETED",
                "transactionId", paymentResult.get("transactionId"),
                "reservationId", inventoryResult.get("reservationId")
        );
    }
}
