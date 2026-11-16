// Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: MIT-0

package com.example.orders;

import org.apache.avro.generic.GenericRecord;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertNotNull;
import static org.junit.jupiter.api.Assertions.assertTrue;

/** Round-trip and Glue-framing tests for the shared Avro helper. */
class AvroIoTest {

    private static final String VERSION_ID = "e424651b-7a41-405d-bf05-2cae8cdf5aea";

    @Test
    void encodeProducesBytes() {
        byte[] encoded = AvroIo.encode(AvroIo.buildOrder("order-123"));
        assertNotNull(encoded);
        assertTrue(encoded.length > 0);
    }

    @Test
    void glueFrameRoundTrips() {
        byte[] framed = AvroIo.encodeFramed(AvroIo.buildOrder("order-123"), VERSION_ID);
        // Header: 0x03, 0x00, then the 16-byte UUID.
        assertEquals(0x03, framed[0] & 0xFF);
        assertEquals(0x00, framed[1] & 0xFF);
        AvroIo.Unframed unframed = AvroIo.glueUnframe(framed);
        assertEquals(VERSION_ID, unframed.schemaVersionId());
        GenericRecord decoded = AvroIo.decodeFramed(framed);
        assertEquals("order-123", decoded.get("orderId").toString());
    }

    @Test
    void roundTripIsLossless() {
        GenericRecord original = AvroIo.buildOrder("order-xyz");
        GenericRecord decoded = AvroIo.decode(AvroIo.encode(original));
        assertEquals(original.get("orderId").toString(), decoded.get("orderId").toString());
        assertEquals(original.get("customerId").toString(), decoded.get("customerId").toString());
        assertEquals(original.get("amount"), decoded.get("amount"));
        assertEquals(original.get("currency").toString(), decoded.get("currency").toString());
        assertEquals(original.get("placedAt"), decoded.get("placedAt"));
    }
}
