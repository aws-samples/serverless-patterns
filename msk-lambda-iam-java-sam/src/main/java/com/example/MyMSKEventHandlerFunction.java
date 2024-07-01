package com.example;

import com.amazonaws.services.lambda.runtime.Context;
import com.amazonaws.services.lambda.runtime.LambdaLogger;
import com.amazonaws.services.lambda.runtime.RequestHandler;
import com.amazonaws.services.lambda.runtime.events.KafkaEvent;
import com.amazonaws.services.lambda.runtime.logging.LogLevel;

import java.util.Base64;


public class MyMSKEventHandlerFunction implements RequestHandler<KafkaEvent, Void> {

    public Void handleRequest(KafkaEvent event, Context context) {

        LambdaLogger logger = context.getLogger();
        logger.log("Received MSK event: " + event, LogLevel.INFO);

        event.getRecords().forEach((key, value) -> {
            logger.log("Key: " + key, LogLevel.INFO);
            value.forEach(record -> {
                logger.log("Topic: " + record.getTopic(), LogLevel.INFO);
                logger.log("Partition: " + record.getPartition(), LogLevel.INFO);
                logger.log("Offset: " + record.getOffset(), LogLevel.INFO);
                logger.log("Timestamp: " + record.getTimestamp(), LogLevel.INFO);
                logger.log("TimestampType: " + record.getTimestampType(), LogLevel.INFO);
                if (record.getKey() != null) {
                    logger.log("Record Key: " + new String(Base64.getDecoder().decode(record.getKey())), LogLevel.INFO);
                }
                logger.log("Record Value: " + new String(Base64.getDecoder().decode(record.getValue())), LogLevel.INFO);
            });
        });
        return null;
    }
}