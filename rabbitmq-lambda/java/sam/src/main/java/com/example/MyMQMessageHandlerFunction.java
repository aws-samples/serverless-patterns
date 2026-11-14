package com.example;

import com.amazonaws.services.lambda.runtime.Context;
import com.amazonaws.services.lambda.runtime.LambdaLogger;
import com.amazonaws.services.lambda.runtime.RequestHandler;
import com.amazonaws.services.lambda.runtime.events.RabbitMQEvent;
import com.amazonaws.services.lambda.runtime.events.RabbitMQEvent.RabbitMessage;
import java.util.List;
import java.util.Map;
import java.util.Base64;


public class MyMQMessageHandlerFunction implements RequestHandler<RabbitMQEvent, Void> {


    public Void handleRequest(RabbitMQEvent event, Context context) {

        LambdaLogger logger = context.getLogger();
        logger.log("Received RabbitMQ event: " + event);

        Map<String, List<RabbitMessage>> queueMap = event.getRmqMessagesByQueue();
        for (Map.Entry<String, List<RabbitMessage>> entry : queueMap.entrySet()) {
            logger.log("Queue name: " + entry.getKey());
            for (RabbitMessage message : entry.getValue()) {
                byte[] decodedBytes = Base64.getDecoder().decode(message.getData());
                logger.log("Message received: " + new String(decodedBytes));
            }
        }

        return null;

    }
}