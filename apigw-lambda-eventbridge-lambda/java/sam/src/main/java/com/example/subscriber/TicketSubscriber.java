package com.example.subscriber;

import com.amazonaws.services.lambda.runtime.Context;
import com.amazonaws.services.lambda.runtime.RequestStreamHandler;
import com.example.subscriber.model.AWSEvent;
import com.example.subscriber.model.Marshaller;
import com.example.subscriber.model.TicketCreated;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;

public class TicketSubscriber implements RequestStreamHandler {

    private static final Logger logger = LoggerFactory.getLogger(TicketSubscriber.class);

    public void handleRequest(InputStream input, OutputStream output, Context context) throws IOException {

        AWSEvent<TicketCreated> event = Marshaller.unmarshalEvent(input, TicketCreated.class);

        TicketCreated ticketEvent = event.getDetail();

        logger.info("[ibcd][new ticketEvent] " + ticketEvent);
    }
}