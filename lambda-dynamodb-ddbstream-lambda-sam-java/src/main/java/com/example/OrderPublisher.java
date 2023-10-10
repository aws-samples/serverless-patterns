package com.example;

import com.amazonaws.services.lambda.runtime.Context;
import com.amazonaws.services.lambda.runtime.RequestHandler;
import com.example.model.Order;
import com.example.utils.DDBUtils;

public class OrderPublisher implements RequestHandler<Order,String> {

    @Override
    public String handleRequest(Order order, Context context) {

        System.out.println(order);

        DDBUtils.persistTicket(order);

        return "Publishing Order";
    }
}
