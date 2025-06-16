package com.amazonaws.services.lambda.samples.events.msk;

import com.amazonaws.services.lambda.runtime.Context;
import com.amazonaws.services.lambda.runtime.LambdaLogger;
import com.amazonaws.services.lambda.runtime.RequestHandler;
import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import org.apache.kafka.clients.producer.Producer;

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

        try {
            // Get environment variables
            String mskClusterArn = System.getenv("MSK_CLUSTER_ARN");
            String kafkaTopic = System.getenv("KAFKA_TOPIC");
            String schemaName = System.getenv("CONTACT_SCHEMA_NAME");

            if (mskClusterArn == null || kafkaTopic == null || schemaName == null) {
                throw new RuntimeException("Required environment variables not set: MSK_CLUSTER_ARN, KAFKA_TOPIC, CONTACT_SCHEMA_NAME");
            }

            // Create a Contact object from the input event or use default values
            Contact contact = createContactFromEvent(event);
            logger.log("Created contact: " + contact.toString());

            // Get the schema definition from Glue Schema Registry
            String schemaDefinition = AvroSchemaHelper.getSchemaDefinition(schemaName);
            logger.log("Retrieved schema definition for: " + schemaName);

            // Create AVRO record
            byte[] avroData = AvroSchemaHelper.createAvroRecord(schemaDefinition, contact);
            logger.log("Created AVRO record, size: " + avroData.length + " bytes");

            // Get bootstrap brokers
            String bootstrapBrokers = KafkaProducerHelper.getBootstrapBrokers(mskClusterArn);
            logger.log("Using bootstrap brokers: " + bootstrapBrokers);

            // Create Kafka producer
            try (Producer<String, byte[]> producer = KafkaProducerHelper.createProducer(bootstrapBrokers)) {
                // Send 10 messages
                int messageCount = 10;
                logger.log("Sending " + messageCount + " AVRO messages to topic: " + kafkaTopic);
                
                for (int i = 0; i < messageCount; i++) {
                    // Generate a random key for each message
                    String messageKey = UUID.randomUUID().toString();
                    
                    // Create a new contact for each message to ensure variety
                    Contact messageContact = createContactFromEvent(event);
                    byte[] messageAvroData = AvroSchemaHelper.createAvroRecord(schemaDefinition, messageContact);
                    
                    // Send the message
                    KafkaProducerHelper.sendAvroMessage(producer, kafkaTopic, messageKey, messageAvroData);
                    logger.log("Successfully sent AVRO message #" + (i+1) + " to topic: " + kafkaTopic);
                }
            }

            return "Successfully sent 10 AVRO messages to Kafka topic: " + kafkaTopic;
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
        contact.setZip(getStringValue(event, "zip", "1000" + randomDigit()));
        contact.setHomePhone(getStringValue(event, "homePhone", "555-123-" + randomDigits(4)));
        contact.setCellPhone(getStringValue(event, "cellPhone", "555-456-" + randomDigits(4)));
        contact.setEmail(getStringValue(event, "email", "user-" + randomSuffix() + "@example.com"));
        contact.setWebsite(getStringValue(event, "website", "https://www." + randomSuffix() + ".com"));
        
        return contact;
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
}
