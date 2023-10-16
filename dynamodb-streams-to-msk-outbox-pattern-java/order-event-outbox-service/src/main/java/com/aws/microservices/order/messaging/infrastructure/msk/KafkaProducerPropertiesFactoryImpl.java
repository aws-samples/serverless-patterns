package com.aws.microservices.order.messaging.infrastructure.msk;

import lombok.extern.slf4j.Slf4j;

import java.util.Map;
import java.util.Properties;
@Slf4j
public class KafkaProducerPropertiesFactoryImpl implements KafkaProducerPropertiesFactory {

    private Properties kafkaProducerProperties;

    public KafkaProducerPropertiesFactoryImpl() {

    }

    private String getBootstrapServer() {
        log.debug("bootstrap_server:::{}",System.getenv("bootstrap_server"));
        return System.getenv("bootstrap_server");
    }

    @Override
    public Properties getProducerProperties() {
        if (kafkaProducerProperties != null)
            return kafkaProducerProperties;

        String serializer = org.apache.kafka.common.serialization.StringSerializer.class.getCanonicalName();
        String callbackHandler = software.amazon.msk.auth.iam.IAMClientCallbackHandler.class.getCanonicalName();
        String loginModule = software.amazon.msk.auth.iam.IAMLoginModule.class.getCanonicalName();

        Map<String, String> configuration = Map.of(
                "key.serializer", serializer,
                "value.serializer", serializer,
                "bootstrap.servers", System.getenv("bootstrap_server"),
                "security.protocol", "SASL_SSL",
                "sasl.mechanism", "AWS_MSK_IAM",
                "sasl.jaas.config", loginModule+ " required;",
                "sasl.client.callback.handler.class", callbackHandler,
                "connections.max.idle.ms", "60",
                "reconnect.backoff.ms", "1000"
        );

        log.debug("configuration::{}",configuration);

        kafkaProducerProperties = new Properties();

        for (Map.Entry<String, String> configEntry : configuration.entrySet()) {
            kafkaProducerProperties.put(configEntry.getKey(), configEntry.getValue());
        }
        return kafkaProducerProperties;
    }
}
