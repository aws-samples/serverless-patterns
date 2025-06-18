package com.amazonaws.services.lambda.samples.events.msk;

import org.apache.kafka.clients.producer.KafkaProducer;
import org.apache.kafka.clients.producer.Producer;
import org.apache.kafka.clients.producer.ProducerConfig;
import org.apache.kafka.clients.producer.ProducerRecord;
import org.apache.kafka.common.serialization.StringSerializer;
import software.amazon.awssdk.services.kafka.KafkaClient;
import software.amazon.awssdk.services.kafka.model.GetBootstrapBrokersRequest;
import software.amazon.awssdk.services.kafka.model.GetBootstrapBrokersResponse;
import software.amazon.awssdk.http.urlconnection.UrlConnectionHttpClient;

import com.amazonaws.services.schemaregistry.serializers.avro.AWSKafkaAvroSerializer;
import com.amazonaws.services.schemaregistry.utils.AWSSchemaRegistryConstants;
import com.amazonaws.services.schemaregistry.utils.AvroRecordType;

import org.apache.avro.generic.GenericRecord;
import org.apache.avro.io.BinaryEncoder;
import org.apache.avro.io.DatumWriter;
import org.apache.avro.io.EncoderFactory;
import org.apache.avro.specific.SpecificDatumWriter;

import java.io.ByteArrayOutputStream;
import java.util.Properties;
import java.util.concurrent.ExecutionException;

/**
 * Helper class for producing messages to Kafka
 */
public class KafkaProducerHelper {

    /**
     * Get bootstrap brokers for an MSK cluster
     * 
     * @param clusterArn ARN of the MSK cluster
     * @return Bootstrap brokers string
     */
    public static String getBootstrapBrokers(String clusterArn) {
        try {
            // Explicitly specify the HTTP client implementation
            KafkaClient kafkaClient = KafkaClient.builder()
                    .httpClientBuilder(UrlConnectionHttpClient.builder())
                    .build();
                    
            GetBootstrapBrokersRequest request = GetBootstrapBrokersRequest.builder()
                    .clusterArn(clusterArn)
                    .build();
            
            GetBootstrapBrokersResponse response = kafkaClient.getBootstrapBrokers(request);
            return response.bootstrapBrokerStringSaslIam();
        } catch (Exception e) {
            throw new RuntimeException("Failed to get bootstrap brokers: " + e.getMessage(), e);
        }
    }

    /**
     * Create a Kafka producer configured for IAM authentication and AWS Glue Schema Registry
     * 
     * @param bootstrapServers Bootstrap servers string
     * @param region AWS region
     * @param registryName Schema registry name
     * @param schemaName Schema name
     * @return Configured Kafka producer
     */
    public static Producer<String, GenericRecord> createProducer(String bootstrapServers, String region, 
                                                               String registryName, String schemaName) {
        Properties props = new Properties();
        props.put(ProducerConfig.BOOTSTRAP_SERVERS_CONFIG, bootstrapServers);
        props.put(ProducerConfig.KEY_SERIALIZER_CLASS_CONFIG, StringSerializer.class.getName());
        props.put(ProducerConfig.VALUE_SERIALIZER_CLASS_CONFIG, AWSKafkaAvroSerializer.class.getName());
        
        // Configure IAM authentication
        props.put("security.protocol", "SASL_SSL");
        props.put("sasl.mechanism", "AWS_MSK_IAM");
        props.put("sasl.jaas.config", "software.amazon.msk.auth.iam.IAMLoginModule required;");
        props.put("sasl.client.callback.handler.class", "software.amazon.msk.auth.iam.IAMClientCallbackHandler");
        
        // Configure AWS Glue Schema Registry
        props.put(AWSSchemaRegistryConstants.AWS_REGION, region);
        props.put(AWSSchemaRegistryConstants.REGISTRY_NAME, registryName);
        props.put(AWSSchemaRegistryConstants.SCHEMA_NAME, schemaName);
        props.put(AWSSchemaRegistryConstants.AVRO_RECORD_TYPE, AvroRecordType.GENERIC_RECORD.getName());
        props.put(AWSSchemaRegistryConstants.SCHEMA_AUTO_REGISTRATION_SETTING, true);
        
        // Additional producer configurations
        props.put(ProducerConfig.ACKS_CONFIG, "all");
        props.put(ProducerConfig.RETRIES_CONFIG, 3);
        props.put(ProducerConfig.MAX_BLOCK_MS_CONFIG, 120000); // 2 minutes
        props.put(ProducerConfig.REQUEST_TIMEOUT_MS_CONFIG, 60000); // 1 minute
        
        return new KafkaProducer<>(props);
    }

    /**
     * Send an AVRO message to a Kafka topic
     * 
     * @param producer Kafka producer
     * @param topic Topic name
     * @param key Message key (can be null)
     * @param avroRecord AVRO record
     * @throws ExecutionException If sending fails
     * @throws InterruptedException If sending is interrupted
     */
    public static void sendAvroMessage(Producer<String, GenericRecord> producer, String topic, String key, GenericRecord avroRecord) 
            throws ExecutionException, InterruptedException {
        try {
            // Print AVRO record details before sending
            System.out.println("Sending AVRO message to topic: '" + topic + "'");
            System.out.println("Message key: " + key);
            System.out.println("AVRO record: " + avroRecord.toString());
            
            // Serialize the AVRO record to bytes to print it
            byte[] serializedBytes = serializeAvroRecord(avroRecord);
            System.out.println("Serialized AVRO (without schema registry header) in hex: " + bytesToHexString(serializedBytes, 0));
            
            // Create and send the record
            ProducerRecord<String, GenericRecord> record = new ProducerRecord<>(topic, key, avroRecord);
            producer.send(record).get(); // Using get() to make it synchronous
            System.out.println("Successfully sent AVRO message to topic: " + topic);
        } catch (Exception e) {
            System.err.println("Error sending message to topic '" + topic + "': " + e.getMessage());
            e.printStackTrace();
            throw e;
        }
    }
    
    /**
     * Serialize an AVRO record to bytes (without schema registry header)
     * 
     * @param avroRecord AVRO record to serialize
     * @return Serialized AVRO bytes
     */
    private static byte[] serializeAvroRecord(GenericRecord avroRecord) {
        try {
            ByteArrayOutputStream outputStream = new ByteArrayOutputStream();
            org.apache.avro.io.BinaryEncoder encoder = org.apache.avro.io.EncoderFactory.get().binaryEncoder(outputStream, null);
            org.apache.avro.specific.SpecificDatumWriter<GenericRecord> writer = 
                new org.apache.avro.specific.SpecificDatumWriter<>(avroRecord.getSchema());
            writer.write(avroRecord, encoder);
            encoder.flush();
            return outputStream.toByteArray();
        } catch (Exception e) {
            System.err.println("Error serializing AVRO record: " + e.getMessage());
            return new byte[0];
        }
    }
    
    /**
     * Convert byte array to hexadecimal string representation
     * 
     * @param bytes Byte array to convert
     * @param maxLength Maximum number of bytes to convert (0 for all)
     * @return Hexadecimal string representation
     */
    public static String bytesToHexString(byte[] bytes, int maxLength) {
        StringBuilder sb = new StringBuilder();
        int length = maxLength > 0 && maxLength < bytes.length ? maxLength : bytes.length;
        
        for (int i = 0; i < length; i++) {
            sb.append(String.format("%02X", bytes[i]));
            if (i % 16 == 15) {
                sb.append("\n");
            } else if (i % 4 == 3) {
                sb.append(" ");
            }
        }
        
        if (maxLength > 0 && length < bytes.length) {
            sb.append("... (").append(bytes.length - length).append(" more bytes)");
        }
        
        return sb.toString();
    }
}
