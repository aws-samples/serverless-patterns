package com.serverlessland;

import com.amazonaws.services.lambda.runtime.Context;
import com.amazonaws.services.lambda.runtime.LambdaLogger;

public class App  {

    public void handleRequest(final Context context) {
        LambdaLogger logger = context.getLogger();
        logger.log("Running scheduled task");
    }

}
