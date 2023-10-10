package com.example.producer;

import com.amazonaws.services.lambda.runtime.Context;
import com.amazonaws.services.lambda.runtime.RequestHandler;
import com.example.producer.model.Payment;
import com.google.gson.Gson;
import software.amazon.awssdk.core.SdkSystemSetting;
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.sqs.SqsClient;
import software.amazon.awssdk.services.sqs.model.SendMessageRequest;
import software.amazon.awssdk.services.sqs.model.SendMessageResponse;

import java.util.UUID;

public class PaymentProducer implements RequestHandler<Payment,String> {
    private final SqsClient sqsClient = SqsClient.builder()
            .region(Region.of(System.getenv(SdkSystemSetting.AWS_REGION.environmentVariable())))
            .build();
    private final Gson GSON = new Gson();

    @Override
    public String handleRequest(Payment payment, Context context) {

        payment.setPaymentId(UUID.randomUUID().toString());

        return sendSQSMessage(GSON.toJson(payment),System.getenv("QUEUE_URL"));
    }

    private String sendSQSMessage(String body, String queueUrl) {

        SendMessageResponse response = sqsClient.sendMessage(SendMessageRequest.builder()
                .queueUrl(queueUrl)
                .messageBody(body)
                .delaySeconds(10)
                .build());
        return response.messageId();
    }
}
