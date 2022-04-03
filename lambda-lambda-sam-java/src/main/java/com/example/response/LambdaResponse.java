package com.example.response;

import com.amazonaws.services.lambda.runtime.Context;
import com.amazonaws.services.lambda.runtime.RequestHandler;
import com.example.response.model.Response;

public class LambdaResponse implements RequestHandler<String, Response> {

    @Override
    public Response handleRequest(String s, Context context) {

        return new Response("I´m doing fine!");
    }
}
