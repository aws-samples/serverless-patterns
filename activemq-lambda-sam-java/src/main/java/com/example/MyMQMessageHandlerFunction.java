package com.example;

import com.amazonaws.services.lambda.runtime.Context;
import com.amazonaws.services.lambda.runtime.LambdaLogger;
import com.amazonaws.services.lambda.runtime.RequestHandler;
import com.amazonaws.services.lambda.runtime.events.ActiveMQEvent;

import java.util.Base64;


public class MyMQMessageHandlerFunction implements RequestHandler<ActiveMQEvent, Void> {


    public Void handleRequest(ActiveMQEvent event, Context context) {

        LambdaLogger logger = context.getLogger();
        logger.log("Received ActiveMQ event: " + event);

        event.getMessages().forEach(message -> logger.log("Message received: " + new String(Base64.getDecoder().decode(message.getData()))));

        return null;

    }
}