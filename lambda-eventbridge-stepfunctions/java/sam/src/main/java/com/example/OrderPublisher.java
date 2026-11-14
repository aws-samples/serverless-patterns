package com.example;

import com.amazonaws.services.lambda.runtime.Context;
import com.amazonaws.services.lambda.runtime.RequestHandler;
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

public class OrderPublisher implements RequestHandler<OrderCreated, String> {

    Logger logger = LoggerFactory.getLogger(OrderPublisher.class);
    ObjectMapper mapper = new ObjectMapper();

    @Override
    public String handleRequest(OrderCreated event, Context context) {

        String eventId = "";
        try {
            OrderCreated orderCreated = mapper.convertValue(event, OrderCreated.class);

            eventId = publishEvent(orderCreated);

            logger.info("[EventBridge ID] " + eventId);

        } catch (JsonProcessingException e) {
            e.printStackTrace();
        }

        return eventId;
    }

    private String publishEvent(OrderCreated orderCreated) throws JsonProcessingException {

        Region region = Region.EU_CENTRAL_1;
        EventBridgeClient eventBrClient = EventBridgeClient.builder()
                .region(region)
                .build();

        String event = mapper.writeValueAsString(orderCreated);

        PutEventsRequestEntry reqEntry = PutEventsRequestEntry.builder()
                .source("com.example")
                .detailType("com.example.OrderCreated")
                .detail(event)
                .eventBusName("OrdersEventBus")
                .build();

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
