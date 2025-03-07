package com.example.processor;

import com.amazonaws.services.lambda.runtime.Context;
import com.amazonaws.services.lambda.runtime.RequestHandler;
import com.amazonaws.services.lambda.runtime.events.SQSEvent;
import com.amazonaws.services.lambda.runtime.events.SQSBatchResponse;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.util.ArrayList;
import java.util.List;
import java.util.Random;

public class SQSMessageProcessor implements RequestHandler<SQSEvent, SQSBatchResponse> {
    private static final Logger logger = LoggerFactory.getLogger(SQSMessageProcessor.class);
    private final Random random = new Random();

    @Override
    public SQSBatchResponse handleRequest(SQSEvent event, Context context) {
        logger.info("Received event: {}", event);
        List<SQSBatchResponse.BatchItemFailure> batchItemFailures = new ArrayList<>();

        for (SQSEvent.SQSMessage message : event.getRecords()) {
            try {
                processSQSMessage(message);
            } catch (Exception e) {
                logger.error("Failed to process message {}: {}", message.getMessageId(), e.getMessage());
                batchItemFailures.add(new SQSBatchResponse.BatchItemFailure(message.getMessageId()));
            }
        }

        return new SQSBatchResponse(batchItemFailures);
    }

    private void processSQSMessage(SQSEvent.SQSMessage message) throws Exception {
        // Randomly fail some messages for demonstration (20% failure rate)
        if (random.nextDouble() < 0.2) {
            logger.info("Randomly failing message: {}", message.getBody());
            throw new Exception("Random processing failure");
        }

        // Log the message for debugging
        logger.info("Processing message: {}", message.getMessageId());

        // Simulate some processing time
        Thread.sleep(100);

        logger.info("Successfully processed message: {}", message.getBody());
    }
} 