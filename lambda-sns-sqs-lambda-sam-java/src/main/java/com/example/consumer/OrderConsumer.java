package com.example.consumer;

import com.amazonaws.services.lambda.runtime.Context;
import com.amazonaws.services.lambda.runtime.RequestHandler;
import com.amazonaws.services.lambda.runtime.events.SQSEvent;
import com.example.model.OrderCreated;
import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.DeserializationFeature;
import com.fasterxml.jackson.databind.ObjectMapper;

public class OrderConsumer implements RequestHandler<SQSEvent, OrderCreated> {

    private static final ObjectMapper MAPPER = new ObjectMapper()
            .configure(DeserializationFeature.FAIL_ON_UNKNOWN_PROPERTIES, false);

    @Override
    public OrderCreated handleRequest(SQSEvent event, Context context) {
        OrderCreated orderCreated = null;

        for(SQSEvent.SQSMessage msg : event.getRecords()){

            try {
                OrderSQSMessage sqsOrder = MAPPER.readValue(msg.getBody(), OrderSQSMessage.class);

                orderCreated = MAPPER.readValue(sqsOrder.getMessage(), OrderCreated.class);

                System.out.println("[ORDER CREATED] " + orderCreated);
            } catch (JsonProcessingException e) {
                e.printStackTrace();
            }
        }
        return orderCreated;
    }
}
