package com.amazonaws.services.lambda.samples.events.msk;

import com.amazonaws.services.lambda.runtime.Context;
import com.amazonaws.services.lambda.runtime.RequestHandler;
import org.apache.kafka.clients.consumer.ConsumerRecord;
import org.apache.kafka.clients.consumer.ConsumerRecords;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import software.amazon.lambda.powertools.kafka.Deserialization;
import software.amazon.lambda.powertools.kafka.DeserializationType;
import software.amazon.lambda.powertools.logging.Logging;

public class AvroKafkaHandler implements RequestHandler<ConsumerRecords<String, Contact>, String> {
    private static final Logger LOGGER = LoggerFactory.getLogger(AvroKafkaHandler.class);

    @Override
    @Logging(logEvent = true)
    @Deserialization(type = DeserializationType.KAFKA_AVRO)
    public String handleRequest(ConsumerRecords<String, Contact> records, Context context) {
        LOGGER.info("=== AvroKafkaHandler called ===");
        LOGGER.info("Event object: {}", records);
        LOGGER.info("Number of records: {}", records.count());
        
        for (ConsumerRecord<String, Contact> record : records) {
            LOGGER.info("Processing record - Topic: {}, Partition: {}, Offset: {}", 
                       record.topic(), record.partition(), record.offset());
            LOGGER.info("Record key: {}", record.key());
            LOGGER.info("Record value: {}", record.value());
            
            if (record.value() != null) {
                Contact contact = record.value();
                LOGGER.info("Contact details - firstName: {}, zip: {}", 
                           contact.getFirstname(), contact.getZip());
            }
        }
        
        LOGGER.info("=== AvroKafkaHandler completed ===");
        return "OK";
    }
}