package com.example.cancel;

import com.amazonaws.services.lambda.runtime.Context;
import com.amazonaws.services.lambda.runtime.RequestHandler;

public class CancelOrder implements RequestHandler {

    @Override
    public Object handleRequest(Object o, Context context) {
        return "We have encountered an error";
    }
}