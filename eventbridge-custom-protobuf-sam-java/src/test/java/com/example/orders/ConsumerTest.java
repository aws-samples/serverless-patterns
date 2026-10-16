// Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: MIT-0

package com.example.orders;

import com.fasterxml.jackson.databind.ObjectMapper;
import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import java.io.ByteArrayOutputStream;
import java.io.PrintStream;
import java.nio.charset.StandardCharsets;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertTrue;

/**
 * Tests for the consumer Lambda handler.
 *
 * <p>Builds a synthetic delivery batch the way the live subscriber does: a
 * WITH_METADATA envelope whose {@code Data} is the already-decoded JSON record,
 * with {@code SystemMetadata} carrying the Glue schema id.
 */
class ConsumerTest {

    private static final ObjectMapper MAPPER = new ObjectMapper();
    private final Consumer consumer = new Consumer();
    private ByteArrayOutputStream out;
    private PrintStream originalOut;

    @BeforeEach
    void captureStdout() {
        originalOut = System.out;
        out = new ByteArrayOutputStream();
        System.setOut(new PrintStream(out, true, StandardCharsets.UTF_8));
    }

    @AfterEach
    void restoreStdout() {
        System.setOut(originalOut);
    }

    private static Map<String, Object> sampleRecord() {
        Map<String, Object> r = new LinkedHashMap<>();
        r.put("order_id", "order-xyz");
        r.put("customer_id", "cust-1");
        r.put("amount", 42.5);
        r.put("currency", "USD");
        r.put("items", List.of(Map.of("sku", "A", "qty", 3)));
        r.put("placed_at", "1789601953851");
        return r;
    }

    private static Map<String, Object> deliveredEvent(Object record, Map<String, Object> metadata) {
        Map<String, Object> systemMetadata = new LinkedHashMap<>();
        systemMetadata.put("ContentType", "application/protobuf");
        systemMetadata.put("aws:SchemaId", "e424651b-7a41-405d-bf05-2cae8cdf5aea");
        systemMetadata.put("aws:RegistryType", "Glue");
        systemMetadata.put("aws:DeliveryType", "LIVE");

        Map<String, Object> e = new LinkedHashMap<>();
        e.put("Data", record);
        e.put("Metadata", metadata);
        e.put("SystemMetadata", systemMetadata);
        return e;
    }

    private String output() {
        return out.toString(StandardCharsets.UTF_8);
    }

    @Test
    void processesBatch() {
        Map<String, Object> metadata = Map.of("eventType", "OrderPlaced", "source", "com.example.orders");
        List<Map<String, Object>> batch = List.of(deliveredEvent(sampleRecord(), metadata));
        Map<String, Object> result = consumer.handleRequest(batch, null);
        assertEquals(1, result.get("recordCount"));
    }

    @Test
    void logsRecordMetadataAndSchemaId() {
        Map<String, Object> metadata = Map.of("eventType", "OrderPlaced", "source", "com.example.orders");
        consumer.handleRequest(List.of(deliveredEvent(sampleRecord(), metadata)), null);
        String logged = output();
        assertTrue(logged.contains("order-xyz"));
        assertTrue(logged.contains("OrderPlaced"));
        assertTrue(logged.contains("e424651b"));
    }

    @Test
    void acceptsDataAsJsonString() throws Exception {
        String dataAsString = MAPPER.writeValueAsString(sampleRecord());
        Map<String, Object> result =
            consumer.handleRequest(deliveredEvent(dataAsString, Map.of()), null);
        assertEquals(1, result.get("recordCount"));
    }

    @Test
    void acceptsSingleObject() {
        Map<String, Object> result =
            consumer.handleRequest(deliveredEvent(sampleRecord(), Map.of()), null);
        assertEquals(1, result.get("recordCount"));
    }
}
