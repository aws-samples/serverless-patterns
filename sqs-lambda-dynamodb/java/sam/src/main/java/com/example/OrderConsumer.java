package com.example;

import com.amazonaws.services.lambda.runtime.Context;
import com.amazonaws.services.lambda.runtime.RequestHandler;
import com.example.model.Message;
import com.example.model.Order;
import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;
import software.amazon.awssdk.enhanced.dynamodb.DynamoDbEnhancedClient;
import software.amazon.awssdk.enhanced.dynamodb.DynamoDbTable;
import software.amazon.awssdk.enhanced.dynamodb.TableSchema;
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.dynamodb.DynamoDbClient;
import software.amazon.awssdk.services.sqs.SqsClient;
import software.amazon.awssdk.services.sqs.model.DeleteMessageRequest;
import software.amazon.awssdk.services.sqs.model.DeleteMessageResponse;
import software.amazon.awssdk.services.sqs.model.ReceiveMessageRequest;

import java.util.ArrayList;
import java.util.List;

public class OrderConsumer implements RequestHandler {

    private final ObjectMapper MAPPER = new ObjectMapper();
    private final String QUEUE_URL = System.getenv("QUEUE_URL");
    private final String REGION = System.getenv("REGION");
    private final String TABLE_NAME = System.getenv("TABLE_NAME");

    @Override
    public Object handleRequest(Object o, Context context) {

        List<Message> messages = readSQSMessages();

        List<String> messageReceipts = ddbPersist(messages);

        List<DeleteMessageResponse> response = deleteSQSMessages(messageReceipts);

        return String.format("%s %d","Messages persisted and deleted:", response.size());
    }

    private List<Message> readSQSMessages(){

        SqsClient sqsClient = SqsClient.builder()
                .region(Region.of(REGION))
                .build();

        ReceiveMessageRequest receiveMessageRequest = ReceiveMessageRequest.builder()
                .queueUrl(QUEUE_URL)
                .maxNumberOfMessages(3)
                .build();

        List<Message> messages = new ArrayList<>();
        sqsClient.receiveMessage(receiveMessageRequest).messages().stream()
                .forEach(m -> {
                    messages.add(new Message(m.messageId(), m.receiptHandle(), m.body()));
                });

        return messages;
    }

    private List<String> ddbPersist(List<Message> messages) {

        List<String> messageReceipts = new ArrayList<>();

        messages.forEach(message -> {

            DynamoDbClient ddb = DynamoDbClient.builder()
                    .region(Region.of(REGION))
                    .build();

            DynamoDbEnhancedClient enhancedClient = DynamoDbEnhancedClient.builder()
                    .dynamoDbClient(ddb)
                    .build();

            System.out.println(TABLE_NAME);

            DynamoDbTable<Order> mappedTable = enhancedClient
                    .table(TABLE_NAME, TableSchema.fromBean(Order.class));

            try {
                Order order = MAPPER.readValue(message.getBody(), Order.class);
                mappedTable.putItem(order);

                messageReceipts.add(message.getReceiptHandle());

            } catch (JsonProcessingException e) {
                e.printStackTrace();
            }
        });

        return messageReceipts;
    }

    private List<DeleteMessageResponse> deleteSQSMessages(List<String> messageReceipts) {

        List<DeleteMessageResponse> deletedMessages = new ArrayList<>();

        SqsClient sqsClient = SqsClient.builder()
                .region(Region.EU_CENTRAL_1)
                .build();

        messageReceipts.forEach(mr -> {
            DeleteMessageRequest deleteMessageRequest = DeleteMessageRequest.builder()
                    .queueUrl(QUEUE_URL)
                    .receiptHandle(mr)
                    .build();

            DeleteMessageResponse response = sqsClient.deleteMessage(deleteMessageRequest);

            System.out.println("response " + response.sdkHttpResponse().isSuccessful() + " " + response.sdkHttpResponse().statusCode() + " " + response.sdkHttpResponse().statusText().get());
            deletedMessages.add(response);
        });

        return deletedMessages;
    }

}
