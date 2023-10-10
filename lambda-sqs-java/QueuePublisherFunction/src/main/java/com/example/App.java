package com.example;

import com.amazonaws.services.lambda.runtime.Context;
import com.amazonaws.services.lambda.runtime.LambdaLogger;
import software.amazon.awssdk.auth.credentials.EnvironmentVariableCredentialsProvider;
import software.amazon.awssdk.http.urlconnection.UrlConnectionHttpClient;
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.sqs.SqsClient;
import software.amazon.awssdk.services.sqs.model.SendMessageRequest;
import software.amazon.awssdk.services.sqs.model.SendMessageResponse;

import java.time.Instant;

public class App {

    private final SqsClient sqsClient = SqsClient.builder()
            .region(Region.of(System.getenv("AWS_REGION")))
            .credentialsProvider(EnvironmentVariableCredentialsProvider.create())
            .httpClient(UrlConnectionHttpClient.builder().build())
            .build();

    public void handleRequest(final Context context) {
        LambdaLogger logger = context.getLogger();

        SendMessageRequest sendMessageRequest = SendMessageRequest.builder()
                .messageBody(String.format("Message at %s", Instant.now().toString()))
                .queueUrl(System.getenv("SQSqueueName"))
                .build();
        SendMessageResponse result = sqsClient.sendMessage(sendMessageRequest);

        logger.log(result.toString());
    }
}