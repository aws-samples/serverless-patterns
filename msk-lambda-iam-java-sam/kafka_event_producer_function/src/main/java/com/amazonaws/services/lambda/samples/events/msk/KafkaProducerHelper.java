package com.amazonaws.services.lambda.samples.events.msk;

import org.apache.kafka.clients.producer.KafkaProducer;
import org.apache.kafka.clients.producer.Producer;
import org.apache.kafka.clients.producer.ProducerConfig;
import org.apache.kafka.clients.producer.ProducerRecord;
import org.apache.kafka.common.serialization.ByteArraySerializer;
import org.apache.kafka.common.serialization.StringSerializer;
import software.amazon.awssdk.services.kafka.KafkaClient;
import software.amazon.awssdk.services.kafka.model.GetBootstrapBrokersRequest;
import software.amazon.awssdk.services.kafka.model.GetBootstrapBrokersResponse;

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
        try (KafkaClient kafkaClient = KafkaClient.builder().build()) {
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
     * Create a Kafka producer configured for IAM authentication
     * 
     * @param bootstrapServers Bootstrap servers string
     * @return Configured Kafka producer
     */
    public static Producer<String, byte[]> createProducer(String bootstrapServers) {
        Properties props = new Properties();
        props.put(ProducerConfig.BOOTSTRAP_SERVERS_CONFIG, bootstrapServers);
        props.put(ProducerConfig.KEY_SERIALIZER_CLASS_CONFIG, StringSerializer.class.getName());
        props.put(ProducerConfig.VALUE_SERIALIZER_CLASS_CONFIG, ByteArraySerializer.class.getName());
        
        // Configure IAM authentication
        props.put("security.protocol", "SASL_SSL");
        props.put("sasl.mechanism", "AWS_MSK_IAM");
        props.put("sasl.jaas.config", "software.amazon.msk.auth.iam.IAMLoginModule required;");
        props.put("sasl.client.callback.handler.class", "software.amazon.msk.auth.iam.IAMClientCallbackHandler");
        
        // Additional producer configurations
        props.put(ProducerConfig.ACKS_CONFIG, "all");
        props.put(ProducerConfig.RETRIES_CONFIG, 3);
        
        return new KafkaProducer<>(props);
    }

    /**
     * Send an AVRO message to a Kafka topic
     * 
     * @param producer Kafka producer
     * @param topic Topic name
     * @param key Message key (can be null)
     * @param avroData AVRO serialized data
     * @throws ExecutionException If sending fails
     * @throws InterruptedException If sending is interrupted
     */
    public static void sendAvroMessage(Producer<String, byte[]> producer, String topic, String key, byte[] avroData) 
            throws ExecutionException, InterruptedException {
        ProducerRecord<String, byte[]> record = new ProducerRecord<>(topic, key, avroData);
        producer.send(record).get(); // Using get() to make it synchronous
    }
}
