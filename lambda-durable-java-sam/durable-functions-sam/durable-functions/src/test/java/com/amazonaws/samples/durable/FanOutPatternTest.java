package com.amazonaws.samples.durable;

import static org.junit.jupiter.api.Assertions.*;

import java.util.Map;

import org.junit.jupiter.api.Test;
import software.amazon.lambda.durable.TypeToken;
import software.amazon.lambda.durable.model.ExecutionStatus;
import software.amazon.lambda.durable.testing.LocalDurableTestRunner;

import com.amazonaws.samples.durable.fanout.ParallelProcessingHandler;

class FanOutPatternTest {

    private static final TypeToken<Map<String, Object>> MAP_TYPE = new TypeToken<>() {};

    @Test
    void executesParallelBranchesAndMapConcurrently() {
        var handler = new ParallelProcessingHandler();
        var runner = LocalDurableTestRunner.create(MAP_TYPE, handler);

        Map<String, Object> input = Map.of(
                "dataId", "DATA-TEST-001",
                "source", "s3://test-bucket/doc.pdf"
        );

        var result = runner.runUntilComplete(input);

        assertEquals(ExecutionStatus.SUCCEEDED, result.getStatus());

        Map<String, Object> output = result.getResult(Map.class);
        assertEquals("FAN_OUT_FAN_IN", output.get("pattern"));
        assertEquals("COMPLETED", output.get("status"));
    }

    @Test
    void aggregatesResultsFromAllBranches() {
        var handler = new ParallelProcessingHandler();
        var runner = LocalDurableTestRunner.create(MAP_TYPE, handler);

        Map<String, Object> input = Map.of("dataId", "DATA-TEST-002");

        var result = runner.runUntilComplete(input);

        assertEquals(ExecutionStatus.SUCCEEDED, result.getStatus());

        Map<String, Object> output = result.getResult(Map.class);
        @SuppressWarnings("unchecked")
        Map<String, Object> aggregated = (Map<String, Object>) output.get("result");
        assertNotNull(aggregated.get("sentiment"));
        assertNotNull(aggregated.get("entities"));
        assertNotNull(aggregated.get("summary"));
        assertNotNull(aggregated.get("documentsProcessed"));
    }
}
