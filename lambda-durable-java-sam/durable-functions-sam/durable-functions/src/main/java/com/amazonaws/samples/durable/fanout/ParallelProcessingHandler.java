package com.amazonaws.samples.durable.fanout;

import java.util.List;
import java.util.Map;

import com.amazonaws.samples.durable.models.SnsEventParser;
import software.amazon.lambda.durable.DurableContext;
import software.amazon.lambda.durable.DurableFuture;
import software.amazon.lambda.durable.DurableHandler;
import software.amazon.lambda.durable.config.CompletionConfig;
import software.amazon.lambda.durable.config.ParallelConfig;
import software.amazon.lambda.durable.model.MapResult;
import software.amazon.lambda.durable.model.ParallelResult;

/**
 * PATTERN: Fan-Out / Fan-In
 *
 * Demonstrates parallel execution of multiple independent operations that are
 * then aggregated. Uses both the parallel() API for heterogeneous tasks and
 * map() for homogeneous collection processing.
 *
 * Flow: Receive data -> Fan-out to multiple processors -> Aggregate results
 */
public class ParallelProcessingHandler extends DurableHandler<Map<String, Object>, Map<String, Object>> {

    @Override
    public Map<String, Object> handleRequest(Map<String, Object> rawEvent, DurableContext context) {
        Map<String, Object> event = SnsEventParser.extractMessage(rawEvent);
        context.getLogger().info("Starting fan-out/fan-in processing");

        String dataId = (String) event.getOrDefault("dataId", "DATA-001");

        // Fan-out using parallel(): Execute different analyses concurrently
        DurableFuture<String> sentimentFuture;
        DurableFuture<String> entityFuture;
        DurableFuture<String> summaryFuture;

        try (var parallel = context.parallel("analyze-data")) {
            sentimentFuture = parallel.branch("sentiment-analysis", String.class, ctx ->
                    ctx.step("run-sentiment", String.class, stepCtx -> {
                        stepCtx.getLogger().info("Running sentiment analysis on: " + dataId);
                        simulateProcessing(500);
                        return "POSITIVE (confidence: 0.87)";
                    })
            );

            entityFuture = parallel.branch("entity-extraction", String.class, ctx ->
                    ctx.step("run-entity-extraction", String.class, stepCtx -> {
                        stepCtx.getLogger().info("Running entity extraction on: " + dataId);
                        simulateProcessing(300);
                        return "Entities: [AWS, Lambda, DurableFunctions, Java]";
                    })
            );

            summaryFuture = parallel.branch("summarization", String.class, ctx ->
                    ctx.step("run-summarization", String.class, stepCtx -> {
                        stepCtx.getLogger().info("Running summarization on: " + dataId);
                        simulateProcessing(700);
                        return "Summary: Document discusses Lambda Durable Functions patterns in Java";
                    })
            );

            ParallelResult result = parallel.get();
            context.getLogger().info("Parallel analysis complete. Succeeded: " + result.succeeded()
                    + ", Failed: " + result.failed());
        }

        String sentiment = sentimentFuture.get();
        String entities = entityFuture.get();
        String summary = summaryFuture.get();

        // Fan-in using map(): Process a collection of items with the same operation
        List<String> documents = List.of("doc-1", "doc-2", "doc-3", "doc-4", "doc-5");

        MapResult<Map<String, String>> mapResult = context.map(
                "process-documents",
                documents,
                (Class<Map<String, String>>) (Class<?>) Map.class,
                (doc, index, ctx) -> ctx.step("process-" + doc, (Class<Map<String, String>>) (Class<?>) Map.class,
                        stepCtx -> {
                            stepCtx.getLogger().info("Processing document: " + doc);
                            simulateProcessing(200);
                            return Map.of(
                                    "documentId", doc,
                                    "wordCount", String.valueOf((index + 1) * 150),
                                    "status", "PROCESSED"
                            );
                        })
        );

        // Aggregate all results
        Map<String, Object> aggregatedResult = context.step("aggregate-results", Map.class, stepCtx -> {
            stepCtx.getLogger().info("Aggregating all results");
            int totalDocsProcessed = mapResult.succeeded().size();
            return Map.of(
                    "dataId", dataId,
                    "sentiment", sentiment,
                    "entities", entities,
                    "summary", summary,
                    "documentsProcessed", totalDocsProcessed,
                    "allSucceeded", mapResult.allSucceeded()
            );
        });

        context.getLogger().info("Fan-out/fan-in processing completed");

        return Map.of(
                "pattern", "FAN_OUT_FAN_IN",
                "status", "COMPLETED",
                "result", aggregatedResult
        );
    }

    private void simulateProcessing(long millis) {
        try {
            Thread.sleep(millis);
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        }
    }
}
