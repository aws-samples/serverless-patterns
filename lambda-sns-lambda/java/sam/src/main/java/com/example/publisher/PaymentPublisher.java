package com.example.publisher;

import com.amazonaws.services.lambda.runtime.Context;
import com.amazonaws.services.lambda.runtime.RequestHandler;
import com.example.publisher.model.PaymentCreated;
import com.google.gson.Gson;
import software.amazon.awssdk.auth.credentials.EnvironmentVariableCredentialsProvider;
import software.amazon.awssdk.core.SdkSystemSetting;
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.sns.SnsClient;
import software.amazon.awssdk.services.sns.model.PublishRequest;
import software.amazon.awssdk.services.sns.model.PublishResponse;

import java.util.UUID;

public class PaymentPublisher implements RequestHandler<PaymentCreated, String> {

    private final Gson GSON = new Gson();
    private static final String TOPIC_ARN = System.getenv("TOPIC_ARN");

    private final SnsClient snsClient = SnsClient.builder()
            .credentialsProvider(EnvironmentVariableCredentialsProvider.create())
            .region(Region.of(System.getenv(SdkSystemSetting.AWS_REGION.environmentVariable())))
            .build();

    @Override
    public String handleRequest(PaymentCreated payment, Context context) {

        return publishSNSMessage(GSON.toJson(payment));
    }

    private String publishSNSMessage(String message) {

        PublishRequest request = PublishRequest.builder()
                .message(message)
                .topicArn(TOPIC_ARN)
                .build();
        PublishResponse result = snsClient.publish(request);

        return result.messageId();
    }
}