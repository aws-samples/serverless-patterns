package com.amazonaws.samples.kafka.oauth;

import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import net.datafaker.Faker;
import org.apache.kafka.clients.producer.KafkaProducer;
import org.apache.kafka.clients.producer.ProducerConfig;
import org.apache.kafka.clients.producer.ProducerRecord;
import org.apache.kafka.clients.producer.RecordMetadata;
import org.apache.kafka.common.serialization.StringSerializer;

import java.io.FileInputStream;
import java.util.Properties;

/**
 * Publishes a given number of JSON "person" messages to a Kafka topic, using
 * SASL/OAUTHBEARER authentication (the OAuth access token is supplied in the
 * properties file loaded at startup).
 *
 * Usage: KafkaJsonProducer <properties-file> <topic> <count>
 */
public class KafkaJsonProducer {

    public static void main(String[] args) throws Exception {
        if (args.length < 3) {
            System.err.println("Usage: KafkaJsonProducer <properties-file> <topic> <count>");
            System.exit(2);
        }
        String propertiesFile = args[0];
        String topic = args[1];
        int count = Integer.parseInt(args[2]);

        Properties props = new Properties();
        try (FileInputStream fis = new FileInputStream(propertiesFile)) {
            props.load(fis);
        }
        props.put(ProducerConfig.KEY_SERIALIZER_CLASS_CONFIG, StringSerializer.class.getName());
        props.put(ProducerConfig.VALUE_SERIALIZER_CLASS_CONFIG, StringSerializer.class.getName());
        // Keep the producer ACL minimal (WRITE on the topic only) by not
        // requiring the cluster-level IDEMPOTENT_WRITE permission.
        props.put(ProducerConfig.ENABLE_IDEMPOTENCE_CONFIG, "false");
        props.put(ProducerConfig.ACKS_CONFIG, "all");

        Faker faker = new Faker();
        Gson gson = new GsonBuilder().create();

        System.out.printf("Producing %d JSON message(s) to topic '%s'...%n", count, topic);
        try (KafkaProducer<String, String> producer = new KafkaProducer<>(props)) {
            for (int i = 0; i < count; i++) {
                Person person = Person.random(faker);
                String json = gson.toJson(person);
                RecordMetadata md = producer.send(new ProducerRecord<>(topic, person.getEmail(), json)).get();
                System.out.printf("Sent [%d/%d] partition=%d offset=%d : %s%n",
                        i + 1, count, md.partition(), md.offset(), json);
            }
            producer.flush();
        }
        System.out.printf("Done. Sent %d message(s) to '%s'.%n", count, topic);
    }
}
