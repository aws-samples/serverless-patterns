package com.example;

import com.amazonaws.services.lambda.runtime.Context;
import com.amazonaws.services.lambda.runtime.LambdaLogger;
import software.amazon.awssdk.auth.credentials.EnvironmentVariableCredentialsProvider;
import software.amazon.awssdk.http.urlconnection.UrlConnectionHttpClient;
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.eventbridge.EventBridgeClient;
import software.amazon.awssdk.services.eventbridge.model.PutEventsRequest;
import software.amazon.awssdk.services.eventbridge.model.PutEventsRequestEntry;
import software.amazon.awssdk.services.eventbridge.model.PutEventsResponse;

import java.time.Instant;

public class App {

    EventBridgeClient EBClient = EventBridgeClient.builder()
            .region(Region.of(System.getenv("AWS_REGION")))
            .credentialsProvider(EnvironmentVariableCredentialsProvider.create())
            .httpClient(UrlConnectionHttpClient.builder().build())
            .build();

    public void handleRequest(final Context context) {
        LambdaLogger logger = context.getLogger();

        PutEventsRequestEntry entry = PutEventsRequestEntry.builder()
                .eventBusName("default")
                .source("demo.event")
                .detailType("Message")
                .time(Instant.now())
                .detail("{ \"message\": \"Hello from publisher\", \"state\": \"new\" }")
                .build();

        PutEventsRequest putEventsRequest = PutEventsRequest.builder()
                .entries(entry)
                .build();

        PutEventsResponse result = EBClient.putEvents(putEventsRequest);

        logger.log(result.toString());
    }
}