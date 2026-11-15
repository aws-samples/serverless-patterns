package com.example;

import com.amazonaws.services.lambda.runtime.Context;
import com.amazonaws.services.lambda.runtime.LambdaLogger;
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
import java.util.Map;

public class App {

    EventBridgeClient ebClient = EventBridgeClient.builder()
            .region(Region.of(System.getenv("AWS_REGION")))
            .credentialsProvider(EnvironmentVariableCredentialsProvider.create())
            .httpClient(UrlConnectionHttpClient.builder().build())
            .build();
    Gson gson = new GsonBuilder().setPrettyPrinting().create();

    public void handleRequest(final Map<String, String> event, final Context context) {
        LambdaLogger logger = context.getLogger();
        
        logger.log(String.format("Event: %s", event));
        PutEventsRequestEntry entry = PutEventsRequestEntry.builder()
                .eventBusName("default")
                .source("demo.event")
                .detailType("Message")
                .time(Instant.now())
                .detail(gson.toJson(event))
                .build();

        PutEventsRequest putEventsRequest = PutEventsRequest.builder()
                .entries(entry)
                .build();

        PutEventsResponse result = ebClient.putEvents(putEventsRequest);

        logger.log(result.toString());
    }
}