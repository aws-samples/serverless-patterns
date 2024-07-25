package com.example.producer;

import com.amazonaws.services.lambda.runtime.Context;
import com.amazonaws.services.lambda.runtime.RequestHandler;
import com.example.model.OrderCreated;
import com.example.utils.SNSUtils;
import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.util.UUID;

public class OrderProducer implements RequestHandler<OrderCreated, String> {

    private final ObjectMapper MAPPER = new ObjectMapper();
    private final Logger LOGGER  = LoggerFactory.getLogger(OrderProducer.class);

    @Override
    public String handleRequest(OrderCreated orderCreated, Context context) {

        LOGGER.info("[order received] [user] " + orderCreated.getUserId());

        String orderId = UUID.randomUUID().toString();
        orderCreated.setOrderId(orderId);

        try {
            SNSUtils.publishMessage(MAPPER.writeValueAsString(orderCreated), "Orders");
        } catch (JsonProcessingException e) {
            e.printStackTrace();
        }

        return "[Order ID] " + orderId;
    }
}
