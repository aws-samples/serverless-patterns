package com.amazonaws.samples.durable.mapprocessing;

import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

import com.amazonaws.samples.durable.models.SnsEventParser;
import software.amazon.lambda.durable.DurableContext;
import software.amazon.lambda.durable.DurableHandler;
import software.amazon.lambda.durable.config.CompletionConfig;
import software.amazon.lambda.durable.config.MapConfig;
import software.amazon.lambda.durable.model.MapResult;

/**
 * PATTERN: Map Processing (Collection Processing)
 *
 * Demonstrates the map() operation which processes each item in a collection
 * concurrently. Each item runs in its own child context with independent
 * checkpointing. Supports concurrency limits, failure tolerance, and
 * completion strategies.
 *
 * Use cases:
 * - Batch processing of records
 * - Parallel API calls with rate limiting
 * - ETL pipelines with partial failure tolerance
 *
 * Flow: Receive batch -> Map over items (concurrent) -> Collect results -> Summarize
 */
public class BatchDataProcessorHandler extends DurableHandler<Map<String, Object>, Map<String, Object>> {

    @Override
    public Map<String, Object> handleRequest(Map<String, Object> rawEvent, DurableContext context) {
        Map<String, Object> event = SnsEventParser.extractMessage(rawEvent);
        context.getLogger().info("Starting batch data processing");

        int batchSize = ((Number) event.getOrDefault("batchSize", 10)).intValue();
        int maxConcurrency = ((Number) event.getOrDefault("maxConcurrency", 3)).intValue();
        int toleratedFailures = ((Number) event.getOrDefault("toleratedFailures", 2)).intValue();

        // Step 1: Generate or receive the batch of items to process
        List<Map<String, String>> batch = context.step("prepare-batch",
                (Class<List<Map<String, String>>>) (Class<?>) List.class, stepCtx -> {
                    stepCtx.getLogger().info("Preparing batch of " + batchSize + " items");
                    return IntStream.range(0, batchSize)
                            .mapToObj(i -> Map.of(
                                    "itemId", "ITEM-" + String.format("%03d", i),
                                    "data", "payload-for-item-" + i,
                                    "priority", i % 3 == 0 ? "HIGH" : "NORMAL"
                            ))
                            .collect(Collectors.toList());
                });

        // Step 2: Process all items using map() with concurrency control
        MapConfig mapConfig = MapConfig.builder()
                .maxConcurrency(maxConcurrency)
                .completionConfig(CompletionConfig.toleratedFailureCount(toleratedFailures))
                .build();

        MapResult<Map<String, Object>> processingResult = context.map(
                "process-batch-items",
                batch,
                (Class<Map<String, Object>>) (Class<?>) Map.class,
                (item, index, ctx) -> {
                    // Each item gets its own child context with independent checkpoints
                    // Multi-step processing per item
                    String validated = ctx.step("validate-" + index, String.class, stepCtx -> {
                        stepCtx.getLogger().info("Validating item: " + item.get("itemId"));
                        // Simulate validation failure for every 5th item
                        if (index % 5 == 4) {
                            throw new RuntimeException("Validation failed for item: " + item.get("itemId"));
                        }
                        return "VALID";
                    });

                    Map<String, Object> transformed = ctx.step("transform-" + index, Map.class, stepCtx -> {
                        stepCtx.getLogger().info("Transforming item: " + item.get("itemId"));
                        return Map.of(
                                "itemId", item.get("itemId"),
                                "originalData", item.get("data"),
                                "transformedData", item.get("data").toUpperCase(),
                                "priority", item.get("priority")
                        );
                    });

                    return ctx.step("store-" + index, Map.class, stepCtx -> {
                        stepCtx.getLogger().info("Storing transformed item: " + item.get("itemId"));
                        return Map.of(
                                "itemId", transformed.get("itemId"),
                                "status", "STORED",
                                "transformedData", transformed.get("transformedData")
                        );
                    });
                },
                mapConfig
        );

        // Step 3: Summarize results
        Map<String, Object> summary = context.step("summarize-results", Map.class, stepCtx -> {
            int succeeded = processingResult.succeeded().size();
            int failed = processingResult.failed().size();
            stepCtx.getLogger().info("Batch processing complete. Succeeded: " + succeeded + ", Failed: " + failed);

            List<String> failureReasons = processingResult.failed().stream()
                    .map(error -> error.errorType() + ": " + error.errorMessage())
                    .collect(Collectors.toList());

            return Map.of(
                    "totalItems", batchSize,
                    "succeeded", succeeded,
                    "failed", failed,
                    "allSucceeded", processingResult.allSucceeded(),
                    "completionReason", processingResult.completionReason().name(),
                    "failureReasons", failureReasons
            );
        });

        return Map.of(
                "pattern", "MAP_PROCESSING",
                "status", processingResult.allSucceeded() ? "ALL_SUCCEEDED" : "PARTIAL_SUCCESS",
                "summary", summary
        );
    }
}
