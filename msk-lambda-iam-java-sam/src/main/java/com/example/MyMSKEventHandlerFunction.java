package com.example;

import com.amazonaws.services.lambda.runtime.Context;
import com.amazonaws.services.lambda.runtime.LambdaLogger;
import com.amazonaws.services.lambda.runtime.RequestHandler;
import com.amazonaws.services.lambda.runtime.events.KafkaEvent;

import java.util.Base64;
import java.util.Optional;


public class MyMSKEventHandlerFunction implements RequestHandler<KafkaEvent, Void> {

    public Void handleRequest(KafkaEvent event, Context context) {

        LambdaLogger logger = context.getLogger();
        logger.log("Received MSK event: " + event);

        event.getRecords().forEach((key, value) -> {
            logger.log("Key: " + key);
            value.forEach(record -> {
                logger.log("Topic: " + record.getTopic());
                logger.log("Partition: " + record.getPartition());
                logger.log("Offset: " + record.getOffset());
                logger.log("Timestamp: " + record.getTimestamp());
                logger.log("TimestampType: " + record.getTimestampType());
                if (record.getKey() != null) {
                    logger.log("Record Key: " + new String(Base64.getDecoder().decode(record.getKey())));
                }
                logger.log("Record Value: " + new String(Base64.getDecoder().decode(record.getValue())));
            });
        });
        return null;
    }
}