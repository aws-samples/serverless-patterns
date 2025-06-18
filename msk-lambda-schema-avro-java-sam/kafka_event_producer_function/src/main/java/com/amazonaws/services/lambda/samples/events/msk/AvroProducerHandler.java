package com.amazonaws.services.lambda.samples.events.msk;

import com.amazonaws.services.lambda.runtime.Context;
import com.amazonaws.services.lambda.runtime.LambdaLogger;
import com.amazonaws.services.lambda.runtime.RequestHandler;
import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import org.apache.avro.Schema;
import org.apache.avro.generic.GenericData;
import org.apache.avro.generic.GenericRecord;
import org.apache.kafka.clients.producer.Producer;

import software.amazon.awssdk.http.urlconnection.UrlConnectionHttpClient;
import software.amazon.awssdk.services.glue.GlueClient;
import software.amazon.awssdk.services.glue.model.*;

import java.util.Map;
import java.util.UUID;

/**
 * Lambda function handler that produces AVRO messages to a Kafka topic
 */
public class AvroProducerHandler implements RequestHandler<Map<String, Object>, String> {

    private final Gson gson = new GsonBuilder().setPrettyPrinting().create();

    @Override
    public String handleRequest(Map<String, Object> event, Context context) {
        LambdaLogger logger = context.getLogger();
        logger.log("Received event: " + gson.toJson(event));

        // Initialize counters for zip code distribution
        int messageCount = 10;
        int zip1000Count = 0;
        int zip2000Count = 0;

        try {
            // Get environment variables
            String mskClusterArn = System.getenv("MSK_CLUSTER_ARN");
            String kafkaTopic = System.getenv("MSK_TOPIC");
            String schemaName = System.getenv("CONTACT_SCHEMA_NAME");
            String region = System.getenv("AWS_REGION");
            String registryName = System.getenv("REGISTRY_NAME") != null ? 
                                 System.getenv("REGISTRY_NAME") : "default-registry";

            if (mskClusterArn == null || kafkaTopic == null || schemaName == null) {
                throw new RuntimeException("Required environment variables not set: MSK_CLUSTER_ARN, KAFKA_TOPIC, CONTACT_SCHEMA_NAME");
            }

            // Log that we're generating zip codes with different prefixes
            logger.log("Generating contacts with zip codes starting with 1000 (50% chance) or 2000 (50% chance)");
            
            // Create a Contact object from the input event or use default values
            Contact contact = createContactFromEvent(event);
            logger.log("Created contact: " + gson.toJson(contact));

            // Get the schema definition from AWS Glue Schema Registry
            String schemaDefinition = getSchemaDefinitionFromRegistry(region, registryName, schemaName);
            logger.log("Retrieved schema definition from registry for: " + schemaName);

            // Create AVRO record
            Schema schema = new Schema.Parser().parse(schemaDefinition);
            GenericRecord avroRecord = createAvroRecord(schema, contact);
            logger.log("Created AVRO record");

            // Get bootstrap brokers
            String bootstrapBrokers = KafkaProducerHelper.getBootstrapBrokers(mskClusterArn);
            logger.log("Using bootstrap brokers: " + bootstrapBrokers);
            
            // Log the topic name for debugging
            logger.log("Target Kafka topic: '" + kafkaTopic + "'");
            
            // Create Kafka producer with AWS Glue Schema Registry serializer
            try (Producer<String, GenericRecord> producer = KafkaProducerHelper.createProducer(
                    bootstrapBrokers, region, registryName, schemaName)) {
                
                // Log producer configuration
                logger.log("Created Kafka producer with AWS Glue Schema Registry serializer");
                logger.log("Registry name: " + registryName);
                logger.log("Schema name: " + schemaName);
                logger.log("Schema definition: " + schemaDefinition);
                
                // Send 10 messages
                logger.log("Sending " + messageCount + " AVRO messages to topic: " + kafkaTopic);
                
                for (int i = 0; i < messageCount; i++) {
                    // Generate a random key for each message
                    String messageKey = UUID.randomUUID().toString();
                    
                    // Create a new contact for each message to ensure variety
                    Contact messageContact = createContactFromEvent(event);
                    
                    // Create AVRO record
                    GenericRecord messageAvroRecord = createAvroRecord(schema, messageContact);
                    
                    // Print the contact details before sending
                    logger.log("Sending contact #" + (i+1) + ": " + gson.toJson(messageContact));
                    logger.log("AVRO record #" + (i+1) + ": " + messageAvroRecord.toString());
                    
                    // Log the zip code prefix for distribution tracking
                    String zipCode = messageContact.getZip();
                    if (zipCode != null && zipCode.length() >= 4) {
                        String prefix = zipCode.substring(0, 4);
                        logger.log("Contact #" + (i+1) + " zip code prefix: " + prefix);
                        
                        // Count zip codes by prefix
                        if ("1000".equals(prefix)) {
                            zip1000Count++;
                        } else if ("2000".equals(prefix)) {
                            zip2000Count++;
                        }
                    }
                    
                    // Send the message
                    KafkaProducerHelper.sendAvroMessage(producer, kafkaTopic, messageKey, messageAvroRecord);
                    logger.log("Successfully sent AVRO message #" + (i+1) + " to topic: " + kafkaTopic);
                }
                
                // Log summary of zip code distribution
                logger.log("ZIP CODE DISTRIBUTION SUMMARY:");
                logger.log("Messages with zip code starting with 1000: " + zip1000Count);
                logger.log("Messages with zip code starting with 2000: " + zip2000Count);
                logger.log("Other zip code formats: " + (messageCount - zip1000Count - zip2000Count));
            }

            return "Successfully sent " + messageCount + " AVRO messages to Kafka topic: " + kafkaTopic + 
                   " (Zip codes: " + zip1000Count + " with prefix 1000, " + zip2000Count + " with prefix 2000)";
        } catch (Exception e) {
            logger.log("Error sending AVRO message: " + e.getMessage());
            e.printStackTrace();
            throw new RuntimeException("Failed to send AVRO message: " + e.getMessage(), e);
        }
    }

    /**
     * Create a Contact object from the input event or use default values
     * 
     * @param event Input event map
     * @return Contact object
     */
    private Contact createContactFromEvent(Map<String, Object> event) {
        Contact contact = new Contact();
        
        // Set fields from event if available, otherwise use default values
        contact.setFirstname(getStringValue(event, "firstname", "FirstName-" + randomSuffix()));
        contact.setLastname(getStringValue(event, "lastname", "LastName-" + randomSuffix()));
        contact.setCompany(getStringValue(event, "company", "Company-" + randomSuffix()));
        contact.setStreet(getStringValue(event, "street", "123 Main St"));
        contact.setCity(getStringValue(event, "city", "AnyCity"));
        contact.setCounty(getStringValue(event, "county", "AnyCounty"));
        contact.setState(getStringValue(event, "state", "AnyState"));
        
        // Generate zip code starting with 1000 50% of the time and 2000 the other 50%
        if (event.containsKey("zip") && event.get("zip") != null) {
            // If zip is provided in the event, use it as is
            contact.setZip(event.get("zip").toString());
        } else {
            // 50% chance for each prefix
            String prefix = Math.random() < 0.5 ? "1000" : "2000";
            contact.setZip(prefix + randomDigit());
        }
        
        contact.setHomePhone(getStringValue(event, "homePhone", "555-123-" + randomDigits(4)));
        contact.setCellPhone(getStringValue(event, "cellPhone", "555-456-" + randomDigits(4)));
        contact.setEmail(getStringValue(event, "email", "user-" + randomSuffix() + "@example.com"));
        contact.setWebsite(getStringValue(event, "website", "https://www." + randomSuffix() + ".com"));
        
        return contact;
    }

    /**
     * Create an AVRO record from a Contact object
     * 
     * @param schema AVRO schema
     * @param contact Contact object
     * @return GenericRecord
     */
    private GenericRecord createAvroRecord(Schema schema, Contact contact) {
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
        
        return avroRecord;
    }

    /**
     * Get a string value from the event map, or return a default value if not found
     * 
     * @param event Input event map
     * @param key Key to look for
     * @param defaultValue Default value to return if key not found
     * @return String value
     */
    private String getStringValue(Map<String, Object> event, String key, String defaultValue) {
        if (event.containsKey(key) && event.get(key) != null) {
            return event.get(key).toString();
        }
        return defaultValue;
    }

    /**
     * Generate a random suffix for default values
     * 
     * @return Random string
     */
    private String randomSuffix() {
        return UUID.randomUUID().toString().substring(0, 8);
    }

    /**
     * Generate a random digit
     * 
     * @return Random digit as string
     */
    private String randomDigit() {
        return Integer.toString((int) (Math.random() * 10));
    }

    /**
     * Generate random digits of specified length
     * 
     * @param length Number of digits to generate
     * @return Random digits as string
     */
    private String randomDigits(int length) {
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < length; i++) {
            sb.append(randomDigit());
        }
        return sb.toString();
    }
    
    /**
     * Get schema definition from AWS Glue Schema Registry
     * 
     * @param region AWS region
     * @param registryName Registry name
     * @param schemaName Schema name
     * @return Schema definition as a string
     */
    private String getSchemaDefinitionFromRegistry(String region, String registryName, String schemaName) {
        try {
            // Create Glue client with explicit HTTP client
            GlueClient glueClient = GlueClient.builder()
                    .httpClientBuilder(UrlConnectionHttpClient.builder())
                    .region(software.amazon.awssdk.regions.Region.of(region))
                    .build();
            
            // Get schema definition
            GetSchemaVersionRequest request = GetSchemaVersionRequest.builder()
                    .schemaId(SchemaId.builder()
                            .registryName(registryName)
                            .schemaName(schemaName)
                            .build())
                    .schemaVersionNumber(SchemaVersionNumber.builder().latestVersion(true).build())
                    .build();
            
            GetSchemaVersionResponse response = glueClient.getSchemaVersion(request);
            String schemaVersionId = response.schemaVersionId();
            String schemaDefinition = response.schemaDefinition();
            
            System.out.println("Retrieved schema version ID: " + schemaVersionId);
            System.out.println("Retrieved schema definition: " + schemaDefinition);
            
            return schemaDefinition;
        } catch (Exception e) {
            throw new RuntimeException("Failed to get schema definition from registry: " + e.getMessage(), e);
        }
    }
}
