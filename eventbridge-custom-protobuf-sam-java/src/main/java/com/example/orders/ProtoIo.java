// Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: MIT-0

package com.example.orders;

import com.example.orders.proto.OrderItem;
import com.example.orders.proto.OrderPlaced;
import com.google.protobuf.InvalidProtocolBufferException;

import java.io.ByteArrayOutputStream;
import java.nio.ByteBuffer;
import java.util.Arrays;
import java.util.List;
import java.util.UUID;

/**
 * Shared Protobuf encode/decode helpers plus the AWS Glue Schema Registry
 * Protobuf wire framing, used by the publisher (and the tests).
 *
 * <p>The {@code OrderPlaced} / {@code OrderItem} classes are generated from
 * {@code src/main/proto/order_placed.proto} by the protobuf-maven-plugin (which
 * downloads protoc) into {@code target/generated-sources} — regenerate them,
 * don't hand-edit.
 *
 * <p>The consumer does NOT use this class: EventBridge decodes the Protobuf
 * server-side and delivers Data as already-decoded JSON.
 */
public final class ProtoIo {

    static final int GLUE_HEADER_VERSION = 0x03;
    static final int GLUE_COMPRESSION_NONE = 0x00;

    // The full names of the two messages in order_placed.proto, used to compute
    // the Glue message index for OrderPlaced.
    private static final List<String> MESSAGE_FULL_NAMES =
        List.of("com.example.orders.OrderItem", "com.example.orders.OrderPlaced");
    private static final String ORDER_PLACED_FULL_NAME = "com.example.orders.OrderPlaced";

    private ProtoIo() {
    }

    /** Serialize a domain message to raw Protobuf wire bytes. */
    public static byte[] encode(OrderPlaced order) {
        return order.toByteArray();
    }

    /** Deserialize raw Protobuf wire bytes into a domain message. */
    public static OrderPlaced decode(byte[] data) throws InvalidProtocolBufferException {
        return OrderPlaced.parseFrom(data);
    }

    // --- AWS Glue Schema Registry wire format (Protobuf) ----------------------
    //
    // Frame layout (uncompressed):
    //   byte 0        header version, always 0x03
    //   byte 1        compression: 0x00 = none, 0x05 = zlib
    //   bytes 2-17    16-byte schema-version UUID (big-endian)
    //   bytes 18..    message-index (unsigned varint), then the Protobuf payload
    //
    // The message-index identifies WHICH message type in the .proto the payload
    // is. Glue assigns indices by breadth-first traversal of all message types in
    // the file, sorted lexicographically by full name, position in that list,
    // written as a plain unsigned varint (NOT zig-zag). For order_placed.proto
    // that is OrderItem = 0, OrderPlaced = 1, so the byte is 0x01.
    //
    // Getting this wrong does NOT fail the publish — the service decodes the
    // bytes against the WRONG message type and delivers a garbled record. So we
    // compute the index the same way Glue does rather than hardcode it.

    /**
     * Replicate Glue's message-index assignment: lexicographically sorted full
     * names, index = position. (Level-order traversal is irrelevant here because
     * there are no nested message types.)
     */
    static int messageIndex(String fullName) {
        List<String> ordered = MESSAGE_FULL_NAMES.stream().sorted().toList();
        return ordered.indexOf(fullName);
    }

    /** Encode a non-negative int as an unsigned LEB128 varint. */
    static byte[] encodeVarint(int value) {
        ByteArrayOutputStream out = new ByteArrayOutputStream();
        int v = value;
        while (true) {
            int b = v & 0x7F;
            v >>>= 7;
            if (v != 0) {
                out.write(b | 0x80);
            } else {
                out.write(b);
                return out.toByteArray();
            }
        }
    }

    /** Decode an unsigned varint at {@code offset}; return {value, newOffset}. */
    static int[] decodeVarint(byte[] data, int offset) {
        int result = 0;
        int shift = 0;
        int pos = offset;
        while (true) {
            int b = data[pos] & 0xFF;
            result |= (b & 0x7F) << shift;
            pos++;
            if ((b & 0x80) == 0) {
                return new int[] {result, pos};
            }
            shift += 7;
        }
    }

    /** Convert a UUID to its 16 big-endian bytes. */
    static byte[] uuidToBytes(String uuid) {
        UUID u = UUID.fromString(uuid);
        return ByteBuffer.allocate(16)
            .putLong(u.getMostSignificantBits())
            .putLong(u.getLeastSignificantBits())
            .array();
    }

    /** Convert 16 big-endian bytes to a UUID string. */
    static String bytesToUuid(byte[] bytes) {
        ByteBuffer buf = ByteBuffer.wrap(bytes);
        return new UUID(buf.getLong(), buf.getLong()).toString();
    }

    /**
     * Wrap raw Protobuf bytes in the Glue Schema Registry Protobuf wire format.
     *
     * <p>{@code schemaVersionId} is the Glue SchemaVersionId (a UUID string) from
     * glue:GetSchemaVersion. The message index for OrderPlaced is computed the
     * way Glue assigns it.
     */
    public static byte[] glueFrame(byte[] protoBytes, String schemaVersionId) {
        byte[] versionBytes = uuidToBytes(schemaVersionId);
        byte[] indexBytes = encodeVarint(messageIndex(ORDER_PLACED_FULL_NAME));
        ByteBuffer buf = ByteBuffer.allocate(2 + 16 + indexBytes.length + protoBytes.length);
        buf.put((byte) GLUE_HEADER_VERSION);
        buf.put((byte) GLUE_COMPRESSION_NONE);
        buf.put(versionBytes);
        buf.put(indexBytes);
        buf.put(protoBytes);
        return buf.array();
    }

    /** Result of splitting a Glue-framed payload. */
    public record Unframed(String schemaVersionId, byte[] protoBytes) {
    }

    /**
     * Split a Glue-framed Protobuf payload into its schema-version id and
     * Protobuf bytes. Validates the header and strips the message-index varint.
     */
    public static Unframed glueUnframe(byte[] framed) {
        if (framed.length < 19) {
            throw new IllegalArgumentException("payload too short to be a Glue Protobuf frame");
        }
        if ((framed[0] & 0xFF) != GLUE_HEADER_VERSION) {
            throw new IllegalArgumentException(
                "unexpected Glue header version: 0x" + Integer.toHexString(framed[0] & 0xFF));
        }
        if ((framed[1] & 0xFF) != GLUE_COMPRESSION_NONE) {
            throw new IllegalArgumentException(
                "compressed Glue payloads are not supported here: 0x"
                    + Integer.toHexString(framed[1] & 0xFF));
        }
        byte[] versionBytes = Arrays.copyOfRange(framed, 2, 18);
        int[] decoded = decodeVarint(framed, 18);
        int payloadOffset = decoded[1];
        byte[] protoBytes = Arrays.copyOfRange(framed, payloadOffset, framed.length);
        return new Unframed(bytesToUuid(versionBytes), protoBytes);
    }

    /** Protobuf-encode a message and wrap it in the Glue Protobuf wire format. */
    public static byte[] encodeFramed(OrderPlaced order, String schemaVersionId) {
        return glueFrame(encode(order), schemaVersionId);
    }

    /** Strip the Glue wire header/index and Protobuf-decode the payload. */
    public static OrderPlaced decodeFramed(byte[] framed) throws InvalidProtocolBufferException {
        return decode(glueUnframe(framed).protoBytes());
    }

    /** Construct a sample OrderPlaced protobuf message for the given order id. */
    public static OrderPlaced buildOrder(String orderId) {
        return OrderPlaced.newBuilder()
            .setOrderId(orderId)
            .setCustomerId("cust-987")
            .setAmount(129.95)
            .setCurrency("USD")
            .addItems(OrderItem.newBuilder().setSku("SKU-1").setQty(2).build())
            .addItems(OrderItem.newBuilder().setSku("SKU-2").setQty(1).build())
            .setPlacedAt(System.currentTimeMillis())
            .build();
    }
}
