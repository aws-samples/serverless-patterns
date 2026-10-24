// Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: MIT-0

package com.example.orders;

import com.amazonaws.services.lambda.runtime.Context;
import com.amazonaws.services.lambda.runtime.RequestHandler;

import java.util.ArrayList;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;

/**
 * Consumer Lambda: the SYNCHRONOUS, ordered target of an EventBridge
 * custom-event-bus subscriber. It logs each delivered order to CloudWatch in the
 * order it is processed.
 *
 * <p>Why this demonstrates ordered processing:
 * <ul>
 *   <li>The subscriber is FIFO (Type = FIFO) and invokes this function
 *       synchronously (InvocationType = REQUEST_RESPONSE). EventBridge waits for
 *       the function to confirm successful processing of each event before
 *       acknowledging it and moving on to the next event in the same event
 *       group.</li>
 *   <li>That synchronous confirmation is what makes ordered, reliable,
 *       direct-to-Lambda processing possible — it removes the pattern of putting
 *       an SQS queue between the bus and Lambda just to get reliability and
 *       back-pressure.</li>
 *   <li>The publisher sends a sequence of orders that share one EventGroupId,
 *       each carrying a monotonically increasing {@code seq}. This handler logs
 *       {@code seq} as it processes each one; the log shows them in order
 *       (1, 2, 3, ...), proving the bus delivered and confirmed them one at a
 *       time, in sequence.</li>
 * </ul>
 *
 * <p>Delivery shape:
 * <ul>
 *   <li>A Lambda target receives a BATCH — a JSON array of delivered events — so
 *       the handler iterates it. Lambda deserializes it into a {@link List}.</li>
 *   <li>With the default RAW transformer and a PutEvents publish, each element is
 *       the classic envelope, so the order fields are under {@code detail}. The
 *       handler tolerates top-level fields too, for easy hand-invocation.</li>
 * </ul>
 *
 * <p>The input type is {@link Object} because the delivery is either a JSON array
 * (the real batch) or a single JSON object (hand-invocation); the handler
 * normalizes both.
 */
public class Consumer implements RequestHandler<Object, Map<String, Object>> {

    @Override
    public Map<String, Object> handleRequest(Object event, Context context) {
        List<Map<String, Object>> delivered = normalizeBatch(event);
        List<Map<String, Object>> processed = new ArrayList<>();

        for (int batchIndex = 0; batchIndex < delivered.size(); batchIndex++) {
            Map<String, Object> order = extractOrder(delivered.get(batchIndex));
            Object orderId = order.get("orderId");
            Object group = order.get("orderGroup");
            Object seq = order.get("seq");

            System.out.printf(
                "Processing order group=%s seq=%s orderId=%s (batchIndex=%d)%n",
                group, seq, orderId, batchIndex);

            Map<String, Object> summary = new LinkedHashMap<>();
            summary.put("orderId", orderId);
            summary.put("group", group);
            summary.put("seq", seq);
            processed.add(summary);
        }

        System.out.printf("Processed %d order(s): %s%n", processed.size(), processed);

        Map<String, Object> result = new LinkedHashMap<>();
        result.put("processed", processed.size());
        return result;
    }

    /** Coerce the incoming event into a list of delivered events. */
    @SuppressWarnings("unchecked")
    static List<Map<String, Object>> normalizeBatch(Object event) {
        if (event instanceof List<?> list) {
            List<Map<String, Object>> out = new ArrayList<>();
            for (Object item : list) {
                out.add((Map<String, Object>) item);
            }
            return out;
        }
        if (event instanceof Map<?, ?> map) {
            return List.of((Map<String, Object>) map);
        }
        throw new IllegalArgumentException("unexpected event type: "
            + (event == null ? "null" : event.getClass().getName()));
    }

    /**
     * Return the order fields from one delivered event.
     *
     * <p>A RAW PutEvents payload is the classic envelope, so the order is under
     * {@code detail}. Fall back to the top level for hand-invocation.
     */
    @SuppressWarnings("unchecked")
    static Map<String, Object> extractOrder(Map<String, Object> item) {
        Object detail = item.get("detail");
        if (detail instanceof Map<?, ?> map) {
            return (Map<String, Object>) map;
        }
        return item;
    }
}
