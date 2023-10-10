package com.example;

import com.amazonaws.services.lambda.runtime.Context;
import com.amazonaws.services.lambda.runtime.LambdaLogger;
import com.amazonaws.services.lambda.runtime.events.ScheduledEvent;
import com.google.gson.Gson;
import com.google.gson.GsonBuilder;

import java.io.IOException;
import java.util.Map;

public class App {

    private final Gson gson = new GsonBuilder().setPrettyPrinting().create();

    public void handleRequest(final ScheduledEvent event, final Context context) throws IOException {
        LambdaLogger logger = context.getLogger();

        logger.log("Received event");
        logger.log(gson.toJson(event));

        Map<String, Object> eventDetail = event.getDetail();
        String bucketName = (String) ((Map<?, ?>)eventDetail.get("bucket")).get("name");
        String key = (String) ((Map<?, ?>)eventDetail.get("object")).get("key");

        logger.log(String.format("Bucket name is %s", bucketName));
        logger.log(String.format("Object key is %s", key));

    }
}