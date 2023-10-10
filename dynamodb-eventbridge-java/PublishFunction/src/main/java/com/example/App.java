package com.example;

import com.amazonaws.services.lambda.runtime.Context;
import com.amazonaws.services.lambda.runtime.LambdaLogger;
import com.amazonaws.services.lambda.runtime.events.DynamodbEvent;
import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import software.amazon.awssdk.auth.credentials.EnvironmentVariableCredentialsProvider;
import software.amazon.awssdk.http.urlconnection.UrlConnectionHttpClient;
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.eventbridge.EventBridgeClient;
import software.amazon.awssdk.services.eventbridge.model.PutEventsRequest;
import software.amazon.awssdk.services.eventbridge.model.PutEventsRequestEntry;
import software.amazon.awssdk.services.eventbridge.model.PutEventsResponse;

import java.time.Instant;
import java.util.ArrayList;

public class App {

    private final EventBridgeClient eventBridgeClient = EventBridgeClient.builder()
            .region(Region.of(System.getenv("AWS_REGION")))
            .credentialsProvider(EnvironmentVariableCredentialsProvider.create())
            .httpClient(UrlConnectionHttpClient.builder().build())
            .build();
    private final Gson gson = new GsonBuilder().setPrettyPrinting().create();

    public void handleRequest(final DynamodbEvent event, final Context context) {
        LambdaLogger logger = context.getLogger();

        ArrayList<PutEventsRequestEntry> entries = new ArrayList<>();

        for (DynamodbEvent.DynamodbStreamRecord record : event.getRecords()) {
            logger.log(gson.toJson(record));

            PutEventsRequestEntry entry = PutEventsRequestEntry.builder()
                    .eventBusName("MyEventBus")
                    .detailType("transaction")
                    .source("MyDynamoStream")
                    .time(Instant.now())
                    .detail(gson.toJson(record))
                    .build();
            entries.add(entry);
        }

        PutEventsRequest putEventsRequest = PutEventsRequest.builder()
                .entries(entries)
                .build();
        PutEventsResponse response = eventBridgeClient.putEvents(putEventsRequest);
        logger.log(response.toString());
    }
}