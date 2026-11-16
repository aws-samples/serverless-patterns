package com.example;

import com.amazonaws.services.lambda.runtime.Context;
import com.amazonaws.services.lambda.runtime.LambdaLogger;
import com.amazonaws.services.lambda.runtime.events.ScheduledEvent;

public class App {

    public void handleRequest(final ScheduledEvent event, final Context context) {
        LambdaLogger logger = context.getLogger();

        logger.log(String.format("Received event with DetailType: %s and Detail: %s",
                event.getDetailType(),
                event.getDetail().toString()));
    }
}