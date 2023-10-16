package com.aws.microservices.order.messaging.infrastructure.msk;

import static software.amazon.lambda.powertools.utilities.jmespath.Base64Function.decode;

import java.util.HashMap;
import java.util.Map;
import java.util.concurrent.Future;

import org.apache.kafka.clients.producer.KafkaProducer;
import org.apache.kafka.clients.producer.ProducerRecord;
import org.apache.kafka.clients.producer.RecordMetadata;
import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;

import com.amazonaws.services.lambda.runtime.events.APIGatewayProxyRequestEvent;
import com.amazonaws.services.lambda.runtime.events.APIGatewayProxyResponseEvent;

import software.amazon.lambda.powertools.logging.Logging;
import software.amazon.lambda.powertools.tracing.Tracing;

public class KafkaProducerSendMessageClient {
	
	public static final String TOPIC_NAME = "order-notification-event-topic";

    private static final Logger log = LogManager.getLogger(KafkaProducerSendMessageClient.class);
    public KafkaProducerPropertiesFactory kafkaProducerProperties = new KafkaProducerPropertiesFactoryImpl();
    private KafkaProducer<String, String> producer;

   // @Override
    @Tracing
    @Logging(logEvent = true)
    public APIGatewayProxyResponseEvent sendMessage(String message) {
        APIGatewayProxyResponseEvent response = createEmptyResponse();
        try {

           // String message = getMessageBody(payload);

            KafkaProducer<String, String> producer = createProducer();

            ProducerRecord<String, String> record = new ProducerRecord<String, String>(TOPIC_NAME, "requestId", message);

            Future<RecordMetadata> send = producer.send(record);
            producer.flush();

            RecordMetadata metadata = send.get();

            log.info(String.format("Message was send to partition %s", metadata.partition()));

            return response.withStatusCode(200).withBody("Message successfully pushed to kafka");
        } catch (Exception e) {
            log.error(e.getMessage(), e);
            return response.withBody(e.getMessage()).withStatusCode(500);
        }
    }

    @Tracing
    private KafkaProducer<String, String> createProducer() {
        if (producer == null) {
            log.info("Connecting to kafka cluster");
            producer = new KafkaProducer<String, String>(kafkaProducerProperties.getProducerProperties());
        }
        return producer;
    }


    private String getMessageBody(APIGatewayProxyRequestEvent input) {
        String body = input.getBody();

        if (input.getIsBase64Encoded()) {
            body = decode(body);
        }
        return body;
    }

    private APIGatewayProxyResponseEvent createEmptyResponse() {
        Map<String, String> headers = new HashMap<>();
        headers.put("Content-Type", "application/json");
        headers.put("X-Custom-Header", "application/json");
        APIGatewayProxyResponseEvent response = new APIGatewayProxyResponseEvent().withHeaders(headers);
        return response;
    }

}
