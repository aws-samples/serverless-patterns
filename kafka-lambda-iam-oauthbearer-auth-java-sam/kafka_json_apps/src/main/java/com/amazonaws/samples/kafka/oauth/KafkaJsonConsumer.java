package com.amazonaws.samples.kafka.oauth;

import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import com.google.gson.JsonElement;
import com.google.gson.JsonParser;
import org.apache.kafka.clients.consumer.ConsumerConfig;
import org.apache.kafka.clients.consumer.ConsumerRecord;
import org.apache.kafka.clients.consumer.ConsumerRecords;
import org.apache.kafka.clients.consumer.KafkaConsumer;
import org.apache.kafka.common.errors.WakeupException;
import org.apache.kafka.common.serialization.StringDeserializer;

import java.io.FileInputStream;
import java.time.Duration;
import java.util.Collections;
import java.util.Properties;

/**
 * Consumes JSON messages from a Kafka topic and prints each one in a parsed,
 * pretty-printed format, using SASL/OAUTHBEARER authentication (the OAuth
 * access token is supplied in the properties file loaded at startup).
 *
 * Usage: KafkaJsonConsumer <properties-file> <topic> [group-id]
 */
public class KafkaJsonConsumer {

    public static void main(String[] args) throws Exception {
        if (args.length < 2) {
            System.err.println("Usage: KafkaJsonConsumer <properties-file> <topic> [group-id]");
            System.exit(2);
        }
        String propertiesFile = args[0];
        String topic = args[1];
        String groupId = args.length >= 3 ? args[2] : "kafka-oauth-consumer-group";

        Properties props = new Properties();
        try (FileInputStream fis = new FileInputStream(propertiesFile)) {
            props.load(fis);
        }
        props.put(ConsumerConfig.KEY_DESERIALIZER_CLASS_CONFIG, StringDeserializer.class.getName());
        props.put(ConsumerConfig.VALUE_DESERIALIZER_CLASS_CONFIG, StringDeserializer.class.getName());
        props.put(ConsumerConfig.GROUP_ID_CONFIG, groupId);
        props.put(ConsumerConfig.AUTO_OFFSET_RESET_CONFIG, "earliest");
        props.put(ConsumerConfig.ENABLE_AUTO_COMMIT_CONFIG, "true");

        Gson gson = new GsonBuilder().setPrettyPrinting().create();
        KafkaConsumer<String, String> consumer = new KafkaConsumer<>(props);
        Thread main = Thread.currentThread();
        Runtime.getRuntime().addShutdownHook(new Thread(() -> {
            consumer.wakeup();
            try { main.join(); } catch (InterruptedException ignored) { }
        }));

        System.out.printf("Consuming from topic '%s' (group '%s'). Press Ctrl-C to stop.%n", topic, groupId);
        consumer.subscribe(Collections.singletonList(topic));
        try {
            while (true) {
                ConsumerRecords<String, String> records = consumer.poll(Duration.ofMillis(1000));
                for (ConsumerRecord<String, String> record : records) {
                    String pretty;
                    try {
                        JsonElement parsed = JsonParser.parseString(record.value());
                        pretty = gson.toJson(parsed);
                    } catch (RuntimeException ex) {
                        pretty = record.value();
                    }
                    System.out.printf("%n--- message partition=%d offset=%d key=%s ---%n%s%n",
                            record.partition(), record.offset(), record.key(), pretty);
                }
            }
        } catch (WakeupException e) {
            // expected on shutdown
        } finally {
            consumer.close();
            System.out.println("Consumer closed.");
        }
    }
}
