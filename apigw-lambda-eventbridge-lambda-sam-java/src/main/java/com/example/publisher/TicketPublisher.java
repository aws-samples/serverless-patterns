package com.example.publisher;

import com.amazonaws.services.lambda.runtime.Context;
import com.amazonaws.services.lambda.runtime.RequestHandler;
import com.amazonaws.services.lambda.runtime.events.APIGatewayProxyRequestEvent;
import com.amazonaws.services.lambda.runtime.events.APIGatewayProxyResponseEvent;
import com.example.publisher.model.TicketCreated;
import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.eventbridge.EventBridgeClient;
import software.amazon.awssdk.services.eventbridge.model.PutEventsRequest;
import software.amazon.awssdk.services.eventbridge.model.PutEventsRequestEntry;
import software.amazon.awssdk.services.eventbridge.model.PutEventsResponse;
import software.amazon.awssdk.services.eventbridge.model.PutEventsResultEntry;

import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class TicketPublisher implements RequestHandler<APIGatewayProxyRequestEvent, APIGatewayProxyResponseEvent> {

    Logger logger = LoggerFactory.getLogger(TicketPublisher.class);
    ObjectMapper mapper = new ObjectMapper();

    @Override
    public APIGatewayProxyResponseEvent handleRequest(APIGatewayProxyRequestEvent event, Context context) {

        APIGatewayProxyResponseEvent response = new APIGatewayProxyResponseEvent();

        try {
            TicketCreated ticketCreated = mapper.readValue(event.getBody(), TicketCreated.class);

            String eventId = publishEvent(ticketCreated);

            response.setBody(mapper.writeValueAsString(eventId));

            logger.info("[EventBridge ID] " + eventId);

        } catch (JsonProcessingException e) {
            e.printStackTrace();
        }

        return response;
    }

    private String publishEvent(TicketCreated ticketCreated) throws JsonProcessingException {

        EventBridgeClient eventBrClient = EventBridgeClient.builder().build();

        String event = mapper.writeValueAsString(ticketCreated);

        PutEventsRequestEntry reqEntry = PutEventsRequestEntry.builder()
                .source("com.example")
                .detailType("TicketCreated")
                .detail(event)
                .eventBusName("TicketEventBus")
                .build();

        List<PutEventsRequestEntry> list = new ArrayList<>();
        list.add(reqEntry);

        PutEventsRequest eventsRequest = PutEventsRequest.builder()
                .entries(reqEntry)
                .build();

        PutEventsResponse result = eventBrClient.putEvents(eventsRequest);

        String eventId = null;

        for (PutEventsResultEntry resultEntry : result.entries()) {
            if (resultEntry.eventId() != null) {
                eventId = resultEntry.eventId();
                System.out.println("Event Id: " + eventId);
            } else {
                System.out.println("Injection failed with Error Code: " + resultEntry.errorCode());
            }
        }
        eventBrClient.close();

        return eventId;
    }
}
