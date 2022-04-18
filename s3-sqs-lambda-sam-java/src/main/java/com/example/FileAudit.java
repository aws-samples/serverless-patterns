package com.example;

import com.amazonaws.services.lambda.runtime.Context;
import com.amazonaws.services.lambda.runtime.RequestHandler;
import com.amazonaws.services.lambda.runtime.events.SQSEvent;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public class FileAudit implements  RequestHandler<SQSEvent, String> {

    private static final Logger LOGGER = LoggerFactory.getLogger(FileAudit.class);

    @Override
    public String handleRequest(SQSEvent event, Context context) {

        event.getRecords()
                .forEach(record -> {
                    LOGGER.info(record.getBody());
                });

        return "Done";
    }
}

