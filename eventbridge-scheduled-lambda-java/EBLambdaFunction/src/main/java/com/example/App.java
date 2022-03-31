package com.example;

import com.amazonaws.services.lambda.runtime.Context;
import com.amazonaws.services.lambda.runtime.LambdaLogger;
import com.amazonaws.services.lambda.runtime.RequestStreamHandler;
import com.google.gson.GsonBuilder;
import com.google.gson.Gson;
import com.google.gson.JsonSyntaxException;

import java.io.*;
import java.util.HashMap;

public class App implements RequestStreamHandler {

    Gson gson = new GsonBuilder().setPrettyPrinting().create();

    @Override
    public void handleRequest(InputStream input, OutputStream output, Context context) throws IOException {
        LambdaLogger logger = context.getLogger();
        BufferedReader reader = new BufferedReader(new InputStreamReader(input));

        try {
            HashMap event = gson.fromJson(reader, HashMap.class);
            logger.log(gson.toJson(event));
            logger.log(String.format("Received event (%s) from source (%s)",
                    event.get("detail-type"),
                    event.get("source")));
        } catch (JsonSyntaxException e) {
            logger.log(e.toString());
        } finally {
            reader.close();
        }

    }
}