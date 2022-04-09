package com.example;

import com.amazonaws.services.lambda.runtime.Context;
import com.amazonaws.services.lambda.runtime.LambdaLogger;
import com.amazonaws.services.lambda.runtime.events.DynamodbEvent;

public class App {

    public void handleRequest(final DynamodbEvent event, final Context context) {
        LambdaLogger logger = context.getLogger();

        logger.log(String.format("Event: %s", event.toString()));
    }
}
