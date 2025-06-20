package com.amazonaws.services.lambda.samples.events.msk;

import com.amazonaws.services.lambda.runtime.Context;
import com.amazonaws.services.lambda.runtime.RequestHandler;

public class SimpleHandler implements RequestHandler<Object, String> {

    @Override
    public String handleRequest(Object event, Context context) {
        System.out.println("=== SIMPLE HANDLER CALLED ===");
        System.out.println("Event: " + event);
        System.out.println("Event class: " + (event != null ? event.getClass().getName() : "null"));
        System.out.println("Context: " + context.getFunctionName());
        System.out.println("=== SIMPLE HANDLER END ===");
        
        return "Simple handler executed successfully";
    }
}
