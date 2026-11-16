package com.example;

import com.amazonaws.services.lambda.runtime.Context;
import com.amazonaws.services.lambda.runtime.RequestHandler;

public class ProcessOrder implements RequestHandler {

    @Override
    public Object handleRequest(Object event, Context context) {

        System.out.println("Processing Order Event" + event.toString());
        return "Done";
    }
}
