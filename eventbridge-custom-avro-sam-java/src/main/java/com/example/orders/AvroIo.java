// Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: MIT-0

package com.example.orders;

import org.apache.avro.Schema;
import org.apache.avro.generic.GenericData;
import org.apache.avro.generic.GenericDatumReader;
import org.apache.avro.generic.GenericDatumWriter;
import org.apache.avro.generic.GenericRecord;
import org.apache.avro.io.BinaryDecoder;
import org.apache.avro.io.BinaryEncoder;
import org.apache.avro.io.DecoderFactory;
import org.apache.avro.io.EncoderFactory;

import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.UncheckedIOException;
import java.nio.ByteBuffer;
import java.nio.charset.StandardCharsets;
import java.util.UUID;

/**
 * Shared Avro encode/decode helpers plus the AWS Glue Schema Registry wire
 * framing, used by the publisher (and the tests).
 *
 * <p>Encoding uses Avro binary (the plain binary encoding via
 * {@link GenericDatumWriter} + {@link BinaryEncoder} — NOT a
 * {@code DataFileWriter} object-container), which is what EventBridge decodes
 * against the Glue Schema Registry when the payload is published with
 * ContentType application/avro.
 *
 * <p>The consumer does NOT use this class: EventBridge decodes the Avro
 * server-side and delivers Data as already-decoded JSON.
 */
public final class AvroIo {

    static final int GLUE_HEADER_VERSION = 0x03;
    static final int GLUE_COMPRESSION_NONE = 0x00;

    /** The OrderPlaced schema, loaded once from the bundled classpath resource. */
    public static final Schema SCHEMA = loadSchema();

    private AvroIo() {
    }

    static Schema loadSchema() {
        try (InputStream in = AvroIo.class.getResourceAsStream("/order_placed.avsc")) {
            if (in == null) {
                throw new IllegalStateException("order_placed.avsc not found on the classpath");
            }
            return new Schema.Parser().parse(in);
        } catch (IOException e) {
            throw new UncheckedIOException("failed to load Avro schema", e);
        }
    }

    /**
     * Serialize a domain record to Avro binary bytes.
     *
     * <p>Returns raw bytes. Do NOT base64-encode these before handing them to
     * the SDK; the SDK does the wire encoding itself.
     */
    public static byte[] encode(GenericRecord record) {
        try {
            ByteArrayOutputStream out = new ByteArrayOutputStream();
            BinaryEncoder encoder = EncoderFactory.get().binaryEncoder(out, null);
            new GenericDatumWriter<GenericRecord>(SCHEMA).write(record, encoder);
            encoder.flush();
            return out.toByteArray();
        } catch (IOException e) {
            throw new UncheckedIOException("failed to Avro-encode record", e);
        }
    }

    /** Deserialize Avro binary bytes back into a domain record. */
    public static GenericRecord decode(byte[] data) {
        try {
            BinaryDecoder decoder = DecoderFactory.get().binaryDecoder(data, null);
            return new GenericDatumReader<GenericRecord>(SCHEMA).read(null, decoder);
        } catch (IOException e) {
            throw new UncheckedIOException("failed to Avro-decode payload", e);
        }
    }

    // --- AWS Glue Schema Registry wire format ---------------------------------
    //
    // Frame layout (uncompressed):
    //   byte 0      header version, always 0x03
    //   byte 1      compression: 0x00 = none, 0x05 = zlib
    //   bytes 2-17  16-byte schema-version UUID (big-endian)
    //   bytes 18+   the Avro binary payload
    //
    // EventBridge reads the header to look up the schema version, so bare Avro is
    // rejected with "Malformed Glue wire format".

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
     * Wrap Avro bytes in the Glue Schema Registry wire format.
     *
     * <p>{@code schemaVersionId} is the Glue SchemaVersionId (a UUID string) from
     * glue:GetSchemaVersion.
     */
    public static byte[] glueFrame(byte[] avroBytes, String schemaVersionId) {
        byte[] versionBytes = uuidToBytes(schemaVersionId);
        ByteBuffer buf = ByteBuffer.allocate(2 + 16 + avroBytes.length);
        buf.put((byte) GLUE_HEADER_VERSION);
        buf.put((byte) GLUE_COMPRESSION_NONE);
        buf.put(versionBytes);
        buf.put(avroBytes);
        return buf.array();
    }

    /** Result of splitting a Glue-framed payload. */
    public record Unframed(String schemaVersionId, byte[] avroBytes) {
    }

    /**
     * Split a Glue-framed payload into its schema-version id and Avro bytes.
     *
     * <p>Validates the header version and compression byte; throws on a frame
     * that is not uncompressed Glue-format.
     */
    public static Unframed glueUnframe(byte[] framed) {
        if (framed.length < 18) {
            throw new IllegalArgumentException("payload too short to be Glue-framed");
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
        byte[] versionBytes = new byte[16];
        System.arraycopy(framed, 2, versionBytes, 0, 16);
        byte[] avroBytes = new byte[framed.length - 18];
        System.arraycopy(framed, 18, avroBytes, 0, avroBytes.length);
        return new Unframed(bytesToUuid(versionBytes), avroBytes);
    }

    /** Avro-encode a record and wrap it in the Glue wire format. */
    public static byte[] encodeFramed(GenericRecord record, String schemaVersionId) {
        return glueFrame(encode(record), schemaVersionId);
    }

    /** Strip the Glue wire header and Avro-decode the payload. */
    public static GenericRecord decodeFramed(byte[] framed) {
        return decode(glueUnframe(framed).avroBytes());
    }

    /** Build a sample OrderPlaced GenericRecord for the given order id. */
    public static GenericRecord buildOrder(String orderId) {
        Schema itemSchema = SCHEMA.getField("items").schema().getElementType();

        GenericRecord item1 = new GenericData.Record(itemSchema);
        item1.put("sku", "SKU-1");
        item1.put("qty", 2);
        GenericRecord item2 = new GenericData.Record(itemSchema);
        item2.put("sku", "SKU-2");
        item2.put("qty", 1);

        GenericRecord order = new GenericData.Record(SCHEMA);
        order.put("orderId", orderId);
        order.put("customerId", "cust-987");
        order.put("amount", 129.95);
        order.put("currency", "USD");
        order.put("items", java.util.List.of(item1, item2));
        order.put("placedAt", System.currentTimeMillis());
        return order;
    }

    /** Read a string field from a decoded record (Avro returns Utf8 for strings). */
    static String stringField(GenericRecord record, String field) {
        Object value = record.get(field);
        return value == null ? null : new String(value.toString().getBytes(StandardCharsets.UTF_8),
            StandardCharsets.UTF_8);
    }
}
