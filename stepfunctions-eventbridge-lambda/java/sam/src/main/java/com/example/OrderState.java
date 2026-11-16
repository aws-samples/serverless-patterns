package com.example;

import com.amazonaws.services.lambda.runtime.Context;
import com.amazonaws.services.lambda.runtime.RequestHandler;
import com.fasterxml.jackson.databind.ObjectMapper;

public class OrderState implements RequestHandler {

    private static final ObjectMapper MAPPER = new ObjectMapper();

    @Override
    public OrderCreated handleRequest(Object object, Context context) {

        OrderCreated orderCreated = new OrderCreated("OrderId:123456789");

        return orderCreated;
    }
}
