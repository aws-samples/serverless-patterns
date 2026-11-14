package com.example;

import com.amazonaws.services.lambda.runtime.Context;
import com.amazonaws.services.lambda.runtime.RequestHandler;

public class OrderState implements RequestHandler {

    @Override
    public String handleRequest(Object object, Context context) {

        System.out.println("[EventBridge event] " + object);

        return "State completed";
    }
}
