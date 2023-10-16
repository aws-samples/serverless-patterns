package com.aws.microservices.order.messaging.infrastructure.msk;

import software.amazon.lambda.powertools.tracing.Tracing;

import java.util.Properties;

public interface KafkaProducerPropertiesFactory {

    @Tracing
    Properties getProducerProperties();
}
