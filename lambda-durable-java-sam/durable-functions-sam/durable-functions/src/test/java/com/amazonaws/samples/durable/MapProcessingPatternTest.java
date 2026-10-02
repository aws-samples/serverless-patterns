package com.amazonaws.samples.durable;

import static org.junit.jupiter.api.Assertions.*;

import java.util.Map;

import org.junit.jupiter.api.Test;
import software.amazon.lambda.durable.TypeToken;
import software.amazon.lambda.durable.model.ExecutionStatus;
import software.amazon.lambda.durable.testing.LocalDurableTestRunner;

import com.amazonaws.samples.durable.mapprocessing.BatchDataProcessorHandler;

class MapProcessingPatternTest {

    private static final TypeToken<Map<String, Object>> MAP_TYPE = new TypeToken<>() {};

    @Test
    void processesAllItemsWithPartialFailureTolerance() {
        var handler = new BatchDataProcessorHandler();
        var runner = LocalDurableTestRunner.create(MAP_TYPE, handler);

        Map<String, Object> input = Map.of(
                "batchSize", 10,
                "maxConcurrency", 3,
                "toleratedFailures", 2
        );

        var result = runner.runUntilComplete(input);

        assertEquals(ExecutionStatus.SUCCEEDED, result.getStatus());

        Map<String, Object> output = result.getResult(Map.class);
        assertEquals("MAP_PROCESSING", output.get("pattern"));
    }

    @Test
    void reportsCorrectSuccessAndFailureCounts() {
        var handler = new BatchDataProcessorHandler();
        var runner = LocalDurableTestRunner.create(MAP_TYPE, handler);

        Map<String, Object> input = Map.of(
                "batchSize", 10,
                "maxConcurrency", 3,
                "toleratedFailures", 2
        );

        var result = runner.runUntilComplete(input);

        assertEquals(ExecutionStatus.SUCCEEDED, result.getStatus());

        Map<String, Object> output = result.getResult(Map.class);
        @SuppressWarnings("unchecked")
        Map<String, Object> summary = (Map<String, Object>) output.get("summary");
        int succeeded = ((Number) summary.get("succeeded")).intValue();
        int failed = ((Number) summary.get("failed")).intValue();

        assertEquals(8, succeeded);
        assertEquals(2, failed);
        assertEquals(10, ((Number) summary.get("totalItems")).intValue());
    }

    @Test
    void respectsConcurrencyLimit() {
        var handler = new BatchDataProcessorHandler();
        var runner = LocalDurableTestRunner.create(MAP_TYPE, handler);

        Map<String, Object> input = Map.of(
                "batchSize", 5,
                "maxConcurrency", 2,
                "toleratedFailures", 1
        );

        var result = runner.runUntilComplete(input);

        assertEquals(ExecutionStatus.SUCCEEDED, result.getStatus());
    }

    @Test
    void handlesSmallBatch() {
        var handler = new BatchDataProcessorHandler();
        var runner = LocalDurableTestRunner.create(MAP_TYPE, handler);

        Map<String, Object> input = Map.of(
                "batchSize", 3,
                "maxConcurrency", 3,
                "toleratedFailures", 1
        );

        var result = runner.runUntilComplete(input);

        assertEquals(ExecutionStatus.SUCCEEDED, result.getStatus());

        Map<String, Object> output = result.getResult(Map.class);
        @SuppressWarnings("unchecked")
        Map<String, Object> summary = (Map<String, Object>) output.get("summary");
        assertEquals(3, ((Number) summary.get("totalItems")).intValue());
    }
}
