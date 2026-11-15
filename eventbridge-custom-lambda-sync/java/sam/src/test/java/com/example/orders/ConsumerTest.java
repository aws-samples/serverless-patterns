// Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: MIT-0

package com.example.orders;

import com.amazonaws.services.lambda.runtime.Context;
import com.amazonaws.services.lambda.runtime.LambdaLogger;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import java.nio.charset.StandardCharsets;
import java.util.ArrayList;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertTrue;
import static org.mockito.Mockito.mock;
import static org.mockito.Mockito.when;

/**
 * Tests for the ordered-processing consumer Lambda handler.
 *
 * <p>The handler logs each delivered order in processing order. These tests
 * assert it processes a batch and logs the sequence numbers it received, in
 * order. A mocked {@link Context} returns a {@link LambdaLogger} that captures
 * the log lines for inspection.
 */
class ConsumerTest {

    /** Collects everything the handler writes through {@code context.getLogger()}. */
    private static final class CapturingLogger implements LambdaLogger {
        private final StringBuilder buffer = new StringBuilder();

        @Override
        public void log(String message) {
            buffer.append(message);
        }

        @Override
        public void log(byte[] message) {
            buffer.append(new String(message, StandardCharsets.UTF_8));
        }
    }

    private final Consumer consumer = new Consumer();
    private CapturingLogger logger;
    private Context context;

    @BeforeEach
    void setUpContext() {
        logger = new CapturingLogger();
        context = mock(Context.class);
        when(context.getLogger()).thenReturn(logger);
    }

    private static Map<String, Object> order(String group, int seq) {
        Map<String, Object> o = new LinkedHashMap<>();
        o.put("orderId", String.format("%s-%03d", group, seq));
        o.put("orderGroup", group);
        o.put("seq", seq);
        o.put("customerId", "cust-1");
        o.put("amount", 100.0 + seq);
        o.put("currency", "USD");
        o.put("placedAt", "2026-09-21T12:00:00Z");
        return o;
    }

    // RAW PutEvents delivery: the payload is the classic envelope with the order
    // under `detail`.
    private static Map<String, Object> deliveredEvent(Map<String, Object> order) {
        Map<String, Object> e = new LinkedHashMap<>();
        e.put("detail", order);
        e.put("detail-type", "OrderPlaced");
        e.put("source", "com.example.orders");
        return e;
    }

    private String output() {
        return logger.buffer.toString();
    }

    @Test
    void processesSingleEvent() {
        Map<String, Object> result = consumer.handleRequest(
            List.of(deliveredEvent(order("g1", 1))), context);
        assertEquals(1, result.get("processed"));
    }

    @Test
    void processesBatchInReceivedOrder() {
        List<Map<String, Object>> batch = new ArrayList<>();
        for (int seq : new int[] {1, 2, 3}) {
            batch.add(deliveredEvent(order("g-order", seq)));
        }
        Map<String, Object> result = consumer.handleRequest(batch, context);
        assertEquals(3, result.get("processed"));

        // The per-event log lines carry seq= in the order they were processed.
        Matcher m = Pattern.compile("seq=(\\d+)").matcher(output());
        List<Integer> seqs = new ArrayList<>();
        while (m.find()) {
            // Skip the summary line, which does not contain "Processing order".
            seqs.add(Integer.parseInt(m.group(1)));
        }
        // The first three matches are the per-event lines in order.
        assertEquals(List.of(1, 2, 3), seqs.subList(0, 3));
    }

    @Test
    void logsGroupSeqAndOrderId() {
        consumer.handleRequest(List.of(deliveredEvent(order("mygroup", 7))), context);
        String logged = output();
        assertTrue(logged.contains("mygroup"));
        assertTrue(logged.contains("seq=7"));
        assertTrue(logged.contains("mygroup-007"));
    }

    @Test
    void acceptsSingleObjectWithTopLevelOrder() {
        // Hand-invocation: order fields at the top level (no `detail` envelope).
        Map<String, Object> result = consumer.handleRequest(order("g", 1), context);
        assertEquals(1, result.get("processed"));
    }
}
