// Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: MIT-0

package com.example.orders;

import com.example.orders.proto.OrderPlaced;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertNotNull;
import static org.junit.jupiter.api.Assertions.assertTrue;

/** Round-trip, Glue-framing, and message-index tests for the Protobuf helper. */
class ProtoIoTest {

    private static final String VERSION_ID = "e424651b-7a41-405d-bf05-2cae8cdf5aea";

    @Test
    void encodeProducesBytes() {
        byte[] encoded = ProtoIo.encode(ProtoIo.buildOrder("order-123"));
        assertNotNull(encoded);
        assertTrue(encoded.length > 0);
    }

    @Test
    void messageIndexMatchesGlueRule() {
        assertEquals(0, ProtoIo.messageIndex("com.example.orders.OrderItem"));
        assertEquals(1, ProtoIo.messageIndex("com.example.orders.OrderPlaced"));
    }

    @Test
    void glueFrameRoundTripsWithMessageIndexByte() throws Exception {
        byte[] framed = ProtoIo.encodeFramed(ProtoIo.buildOrder("order-123"), VERSION_ID);
        // Header: 0x03, 0x00, then the 16-byte UUID, then the message-index varint.
        assertEquals(0x03, framed[0] & 0xFF);
        assertEquals(0x00, framed[1] & 0xFF);
        // byte 18 is the message index varint: OrderPlaced = 1.
        assertEquals(0x01, framed[18] & 0xFF);
        ProtoIo.Unframed unframed = ProtoIo.glueUnframe(framed);
        assertEquals(VERSION_ID, unframed.schemaVersionId());
        OrderPlaced decoded = ProtoIo.decodeFramed(framed);
        assertEquals("order-123", decoded.getOrderId());
    }

    @Test
    void roundTripIsLossless() throws Exception {
        OrderPlaced original = ProtoIo.buildOrder("order-xyz");
        OrderPlaced decoded = ProtoIo.decode(ProtoIo.encode(original));
        assertEquals(original.getOrderId(), decoded.getOrderId());
        assertEquals(original.getCustomerId(), decoded.getCustomerId());
        assertEquals(original.getAmount(), decoded.getAmount());
        assertEquals(original.getCurrency(), decoded.getCurrency());
        assertEquals(original.getItemsList(), decoded.getItemsList());
        assertEquals(original.getPlacedAt(), decoded.getPlacedAt());
    }
}
