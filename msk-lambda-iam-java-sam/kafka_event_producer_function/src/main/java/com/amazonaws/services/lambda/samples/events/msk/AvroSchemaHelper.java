package com.amazonaws.services.lambda.samples.events.msk;

import org.apache.avro.Schema;
import org.apache.avro.generic.GenericData;
import org.apache.avro.generic.GenericRecord;
import org.apache.avro.io.BinaryEncoder;
import org.apache.avro.io.DatumWriter;
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

/**
 * Helper class for working with AVRO schemas from AWS Glue Schema Registry
 */
public class AvroSchemaHelper {

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
     * Create an AVRO record from a Contact object using the schema from Glue Schema Registry
     * 
     * @param schemaDefinition AVRO schema definition
     * @param contact Contact object to convert to AVRO
     * @return AVRO record as byte array
     */
    public static byte[] createAvroRecord(String schemaDefinition, Contact contact) {
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
            
            return outputStream.toByteArray();
        } catch (IOException e) {
            throw new RuntimeException("Failed to create AVRO record: " + e.getMessage(), e);
        }
    }
}
