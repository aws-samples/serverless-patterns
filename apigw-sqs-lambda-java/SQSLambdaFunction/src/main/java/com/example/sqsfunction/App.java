package com.example.sqsfunction;

import com.amazonaws.services.lambda.runtime.Context;
import com.amazonaws.services.lambda.runtime.LambdaLogger;
import com.amazonaws.services.lambda.runtime.RequestHandler;
import com.amazonaws.services.lambda.runtime.events.SQSEvent;
import com.amazonaws.services.lambda.runtime.events.SQSBatchResponse;

import java.util.ArrayList;

/**
 * Handler for requests to Lambda function.
 */
public class App implements RequestHandler<SQSEvent, SQSBatchResponse> {

    public SQSBatchResponse handleRequest(final SQSEvent input, final Context context) {

        LambdaLogger logger = context.getLogger();

        for (SQSEvent.SQSMessage record : input.getRecords()) {
            logger.log(record.getBody());
        }

        return new SQSBatchResponse(new ArrayList<>());
    }
}
