package com.example;

import com.amazonaws.services.lambda.runtime.Context;
import com.amazonaws.services.lambda.runtime.RequestHandler;
import com.amazonaws.services.lambda.runtime.events.SNSEvent;

public class FileAudit implements RequestHandler<SNSEvent, String> {

    @Override
    public String handleRequest(SNSEvent snsEvent, Context context) {

        snsEvent.getRecords()
                .forEach(record -> {
                    System.out.println(record.getSNS().getMessage());
                });
        return "Done";
    }
}
