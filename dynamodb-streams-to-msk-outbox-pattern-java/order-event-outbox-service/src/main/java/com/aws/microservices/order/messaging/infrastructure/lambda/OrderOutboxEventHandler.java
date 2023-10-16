package com.aws.microservices.order.messaging.infrastructure.lambda;

import com.amazonaws.services.lambda.runtime.Context;
import com.amazonaws.services.lambda.runtime.RequestHandler;
import com.amazonaws.services.lambda.runtime.events.DynamodbEvent;
import com.aws.microservices.order.messaging.infrastructure.msk.KafkaProducerSendMessageClient;
import lombok.extern.slf4j.Slf4j;

@Slf4j
public class OrderOutboxEventHandler implements RequestHandler<DynamodbEvent, String> {
    public String handleRequest(DynamodbEvent ddbEvent, Context context) {
        for (DynamodbEvent.DynamodbStreamRecord record : ddbEvent.getRecords()){
            log.debug(record.getEventID());
            log.debug(record.getEventName());
            log.debug(record.getDynamodb().toString());
            log.debug("NewImage:,"+record.getDynamodb().getNewImage());

            try {
                String payload = record.getDynamodb().getNewImage().get("payload").getS();
                String bootstrap_server = System.getenv("bootstrap_server");

                KafkaProducerSendMessageClient client = new KafkaProducerSendMessageClient();
                client.sendMessage(payload);

            } catch (Exception e) {
                throw new RuntimeException(e);
            }

        }
        return "Successfully processed " + ddbEvent.getRecords().size() + " records.";
    }
}