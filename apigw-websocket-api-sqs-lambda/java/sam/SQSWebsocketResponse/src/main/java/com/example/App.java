package com.example;

import com.amazonaws.services.lambda.runtime.Context;
import com.amazonaws.services.lambda.runtime.LambdaLogger;
import com.amazonaws.services.lambda.runtime.RequestHandler;
import com.amazonaws.services.lambda.runtime.events.SQSBatchResponse;
import com.amazonaws.services.lambda.runtime.events.SQSEvent;
import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import software.amazon.awssdk.auth.credentials.EnvironmentVariableCredentialsProvider;
import software.amazon.awssdk.core.SdkBytes;
import software.amazon.awssdk.http.crt.AwsCrtAsyncHttpClient;
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.apigatewaymanagementapi.ApiGatewayManagementApiAsyncClient;
import software.amazon.awssdk.services.apigatewaymanagementapi.model.PostToConnectionRequest;
import software.amazon.awssdk.services.apigatewaymanagementapi.model.PostToConnectionResponse;

import java.net.URI;
import java.net.URISyntaxException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;
import java.util.concurrent.ExecutionException;

public class App implements RequestHandler<SQSEvent, SQSBatchResponse> {

    ApiGatewayManagementApiAsyncClient apiGWMgtClient = ApiGatewayManagementApiAsyncClient.builder()
            .endpointOverride(new URI(System.getenv("ApiGatewayEndpoint")))
            .region(Region.of(System.getenv("AWS_REGION")))
            .credentialsProvider(EnvironmentVariableCredentialsProvider.create())
            .httpClient(AwsCrtAsyncHttpClient.builder().maxConcurrency(50).build())
            .build();

    Gson gson = new GsonBuilder().setPrettyPrinting().create();

    public App() throws URISyntaxException {
    }

    public SQSBatchResponse handleRequest(final SQSEvent event, final Context context) {
        LambdaLogger logger = context.getLogger();

        for (SQSEvent.SQSMessage record : event.getRecords()) {
            logger.log(record.toString());

            Map<String, SQSEvent.MessageAttribute> msgAttributes = record.getMessageAttributes();
            Map<String, String> responseData = new HashMap<>();

            String connId = msgAttributes.get("connectionId").getStringValue();

            responseData.put("connectionId", connId);
            responseData.put("requestId", msgAttributes.get("requestId").getStringValue());
            responseData.put("data", record.getBody());

            PostToConnectionRequest postToConnectionRequest = PostToConnectionRequest.builder()
                    .connectionId(connId)
                    .data(SdkBytes.fromUtf8String(gson.toJson(responseData)))
                    .build();

            try {
                PostToConnectionResponse resp = apiGWMgtClient.postToConnection(postToConnectionRequest).get();
            } catch (InterruptedException | ExecutionException e) {
                e.printStackTrace();
            }
        }

        return new SQSBatchResponse(new ArrayList<>());
    }
}