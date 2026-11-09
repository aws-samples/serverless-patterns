// Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: MIT-0

package com.example.orders;

import com.amazonaws.services.lambda.runtime.Context;
import com.amazonaws.services.lambda.runtime.RequestHandler;
import com.fasterxml.jackson.databind.ObjectMapper;

import java.util.ArrayList;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;

/**
 * Consumer Lambda: log the OrderPlaced events delivered by the subscriber to
 * CloudWatch, proving the delivered event is the same domain event that was
 * originally published.
 *
 * <p>Delivery shape (verified against the live service):
 * <ul>
 *   <li>A subscriber's Lambda target receives a BATCH: the event is a JSON array
 *       of delivered events, not a single object. Lambda deserializes it into a
 *       {@link List}; the handler iterates it.</li>
 *   <li>This subscriber uses a WITH_METADATA transformer, so each delivered event
 *       has the three-part envelope: {@code Data} (the payload), {@code Metadata}
 *       (the publisher's custom keys), and {@code SystemMetadata} (service
 *       fields).</li>
 *   <li>The payload was published as Avro (ContentType application/avro) against a
 *       Glue Schema Registry. EventBridge decodes the Avro server-side and
 *       delivers {@code Data} as an already-decoded JSON object — the handler does
 *       NOT base64-decode or Avro-decode. {@code SystemMetadata} carries
 *       {@code aws:SchemaId} and {@code aws:RegistryType: Glue}.</li>
 * </ul>
 *
 * <p>Because the service does the Avro decode, this function needs no Avro
 * library and no bundled schema.
 */
public class Consumer implements RequestHandler<Object, Map<String, Object>> {

    private static final ObjectMapper MAPPER = new ObjectMapper();

    @Override
    public Map<String, Object> handleRequest(Object event, Context context) {
        List<Map<String, Object>> delivered = normalizeBatch(event);
        int count = 0;

        for (int index = 0; index < delivered.size(); index++) {
            Map<String, Object> item = delivered.get(index);
            Object record = extractRecord(item);
            Object metadata = item.getOrDefault("Metadata", Map.of());
            Object systemMetadata = item.getOrDefault("SystemMetadata", Map.of());

            Object schemaId = (systemMetadata instanceof Map<?, ?> sm) ? sm.get("aws:SchemaId") : null;
            Object registry = (systemMetadata instanceof Map<?, ?> sm) ? sm.get("aws:RegistryType") : null;

            System.out.printf(
                "OrderPlaced[%d]: %s | metadata=%s | schemaId=%s registry=%s%n",
                index, record, metadata, schemaId, registry);
            count++;
        }

        Map<String, Object> result = new LinkedHashMap<>();
        result.put("recordCount", count);
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
     * Return the decoded domain record from one delivered event.
     *
     * <p>{@code Data} arrives as a JSON object (the service already Avro-decoded
     * it). If it is delivered as a JSON string, parse it.
     */
    static Object extractRecord(Map<String, Object> item) {
        Object data = item.get("Data");
        if (data instanceof Map<?, ?>) {
            return data;
        }
        if (data instanceof String s) {
            try {
                return MAPPER.readValue(s, Map.class);
            } catch (Exception e) {
                throw new IllegalArgumentException("Data was a string but not JSON: " + s, e);
            }
        }
        throw new IllegalArgumentException("unexpected Data type: "
            + (data == null ? "null" : data.getClass().getName()));
    }
}
