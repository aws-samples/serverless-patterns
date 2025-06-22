package com.amazonaws.services.lambda.samples.events.msk;

import org.apache.avro.Schema;
import org.apache.avro.generic.GenericData;
import org.apache.avro.generic.GenericDatumReader;
import org.apache.avro.generic.GenericRecord;
import org.apache.avro.io.BinaryEncoder;
import org.apache.avro.io.DatumReader;
import org.apache.avro.io.DatumWriter;
import org.apache.avro.io.DecoderFactory;
import org.apache.avro.io.EncoderFactory;
import org.apache.avro.specific.SpecificDatumWriter;
import software.amazon.awssdk.services.glue.GlueClient;
import software.amazon.awssdk.services.glue.model.GetSchemaVersionRequest;
import software.amazon.awssdk.services.glue.model.GetSchemaVersionResponse;
import software.amazon.awssdk.services.glue.model.SchemaId;
import software.amazon.awssdk.services.glue.model.SchemaVersionNumber;

import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.nio.ByteBuffer;
import java.util.Arrays;
import java.util.UUID;

/**
 * Helper class for working with AVRO schemas from AWS Glue Schema Registry
 */
public class AvroSchemaHelper {

    // Schema registry constants
    private static final byte HEADER_VERSION_BYTE = 0x00;

    /**
     * Get schema definition from AWS Glue Schema Registry
     * 
     * @param schemaName Name of the schema in Glue Schema Registry
     * @return Schema definition as a string
     */
    public static String getSchemaDefinition(String schemaName) {
        try (GlueClient glueClient = GlueClient.builder().build()) {
            GetSchemaVersionRequest request = GetSchemaVersionRequest.builder()
                    .schemaId(SchemaId.builder()
                            .registryName("default-registry")
                            .schemaName(schemaName)
                            .build())
                    .schemaVersionNumber(SchemaVersionNumber.builder().latestVersion(true).build())
                    .build();

            GetSchemaVersionResponse response = glueClient.getSchemaVersion(request);
            return response.schemaDefinition();
        } catch (Exception e) {
            throw new RuntimeException("Failed to get schema definition: " + e.getMessage(), e);
        }
    }

    /**
     * Get schema version ID from AWS Glue Schema Registry
     * 
     * @param schemaName Name of the schema in Glue Schema Registry
     * @return Schema version ID as UUID
     */
    public static UUID getSchemaVersionId(String schemaName) {
        try (GlueClient glueClient = GlueClient.builder().build()) {
            GetSchemaVersionRequest request = GetSchemaVersionRequest.builder()
                    .schemaId(SchemaId.builder()
                            .registryName("default-registry")
                            .schemaName(schemaName)
                            .build())
                    .schemaVersionNumber(SchemaVersionNumber.builder().latestVersion(true).build())
                    .build();

            GetSchemaVersionResponse response = glueClient.getSchemaVersion(request);
            String schemaVersionId = response.schemaVersionId();
            
            // Print the original UUID schema ID
            System.out.println("Retrieved schema version ID (UUID): " + schemaVersionId);
            
            // Return the actual UUID
            return UUID.fromString(schemaVersionId);
        } catch (Exception e) {
            throw new RuntimeException("Failed to get schema version ID: " + e.getMessage(), e);
        }
    }

    /**
     * Create an AVRO record from a Contact object using the schema from Glue Schema Registry
     * 
     * @param schemaDefinition AVRO schema definition
     * @param contact Contact object to convert to AVRO
     * @param schemaId Schema ID to include in the header
     * @return AVRO record as byte array with schema registry header
     */
    public static byte[] createAvroRecord(String schemaDefinition, Contact contact, UUID schemaId) {
        try {
            Schema schema = new Schema.Parser().parse(schemaDefinition);
            GenericRecord avroRecord = new GenericData.Record(schema);
            
            // Populate the record with data from the Contact object
            avroRecord.put("firstname", contact.getFirstname());
            avroRecord.put("lastname", contact.getLastname());
            avroRecord.put("company", contact.getCompany());
            avroRecord.put("street", contact.getStreet());
            avroRecord.put("city", contact.getCity());
            avroRecord.put("county", contact.getCounty());
            avroRecord.put("state", contact.getState());
            avroRecord.put("zip", contact.getZip());
            avroRecord.put("homePhone", contact.getHomePhone());
            avroRecord.put("cellPhone", contact.getCellPhone());
            avroRecord.put("email", contact.getEmail());
            avroRecord.put("website", contact.getWebsite());
            
            // Serialize the record to a byte array
            ByteArrayOutputStream outputStream = new ByteArrayOutputStream();
            BinaryEncoder encoder = EncoderFactory.get().binaryEncoder(outputStream, null);
            DatumWriter<GenericRecord> datumWriter = new SpecificDatumWriter<>(schema);
            datumWriter.write(avroRecord, encoder);
            encoder.flush();
            
            // Add schema registry header with schema ID
            byte[] avroData = outputStream.toByteArray();
            return addSchemaRegistryHeader(avroData, schemaId);
        } catch (IOException e) {
            throw new RuntimeException("Failed to create AVRO record: " + e.getMessage(), e);
        }
    }
    
    /**
     * Add schema registry header to AVRO data
     * 
     * @param avroData AVRO serialized data
     * @param schemaId Schema ID as UUID
     * @return AVRO data with schema registry header
     */
    private static byte[] addSchemaRegistryHeader(byte[] avroData, UUID schemaId) {
        // Schema registry header format:
        // Byte 0: Magic byte (0x00)
        // Bytes 1-16: UUID (16 bytes)
        ByteBuffer buffer = ByteBuffer.allocate(1 + 16 + avroData.length);
        buffer.put((byte) 0x00);  // Magic byte
        
        // Add UUID bytes (16 bytes)
        buffer.putLong(schemaId.getMostSignificantBits());
        buffer.putLong(schemaId.getLeastSignificantBits());
        
        // Add AVRO data
        buffer.put(avroData);
        
        System.out.println("Added schema registry header with UUID: " + schemaId);
        System.out.println("First 17 bytes of message (hex): " + bytesToHex(buffer.array(), 17));
        
        return buffer.array();
    }
    
    /**
     * Parse an AVRO message with schema registry header
     * 
     * @param avroMessage Complete AVRO message with schema registry header
     * @param schemaDefinition AVRO schema definition
     * @return Parsed GenericRecord
     */
    public static GenericRecord parseAvroMessage(byte[] avroMessage, String schemaDefinition) {
        try {
            // Check if this is a valid message with schema registry header
            if (avroMessage.length <= 17 || avroMessage[0] != 0x00) {
                throw new IllegalArgumentException("Invalid AVRO message format: missing or invalid schema registry header");
            }
            
            // Extract the AVRO data (skip the 17-byte header)
            byte[] avroData = Arrays.copyOfRange(avroMessage, 17, avroMessage.length);
            
            // Parse the schema
            Schema schema = new Schema.Parser().parse(schemaDefinition);
            
            // Create a datum reader for the schema
            DatumReader<GenericRecord> datumReader = new GenericDatumReader<>(schema);
            
            // Create a decoder for the AVRO data
            org.apache.avro.io.Decoder decoder = DecoderFactory.get().binaryDecoder(avroData, null);
            
            // Read the record
            return datumReader.read(null, decoder);
        } catch (Exception e) {
            throw new RuntimeException("Failed to parse AVRO message: " + e.getMessage(), e);
        }
    }
    
    /**
     * Convert byte array to hexadecimal string
     * 
     * @param bytes Byte array to convert
     * @param maxLength Maximum number of bytes to convert (0 for all)
     * @return Hexadecimal string
     */
    private static String bytesToHex(byte[] bytes, int maxLength) {
        StringBuilder sb = new StringBuilder();
        int length = maxLength > 0 && maxLength < bytes.length ? maxLength : bytes.length;
        
        for (int i = 0; i < length; i++) {
            sb.append(String.format("%02X", bytes[i]));
            if (i % 4 == 3 && i < length - 1) {
                sb.append(" ");
            }
        }
        
        if (maxLength > 0 && length < bytes.length) {
            sb.append("...");
        }
        
        return sb.toString();
    }
}
