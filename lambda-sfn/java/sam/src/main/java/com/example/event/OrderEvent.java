package com.example.event;

import com.amazonaws.services.lambda.runtime.Context;
import com.amazonaws.services.lambda.runtime.RequestHandler;
import com.example.model.Customer;
import com.example.model.OrderCreated;
import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.sfn.SfnClient;
import software.amazon.awssdk.services.sfn.model.StartExecutionRequest;
import software.amazon.awssdk.services.sfn.model.StartExecutionResponse;

import java.util.UUID;

public class OrderEvent implements RequestHandler<OrderCreated, Customer>  {

    private static final ObjectMapper MAPPER = new ObjectMapper();

    @Override
    public Customer handleRequest(OrderCreated orderCreated, Context context) {

        Customer customer = MAPPER.convertValue(orderCreated.getCustomer(), Customer.class);

        //read StateMachineArn fron template.yml environment variables
        String stateMachineArn = System.getenv("StateMachineArn");

        SfnClient sfnClient = SfnClient.builder()
                .region(Region.EU_CENTRAL_1)
                .build();

        try {
            StartExecutionRequest executionRequest = StartExecutionRequest.builder()
                    .input(MAPPER.writeValueAsString(customer))
                    .stateMachineArn(stateMachineArn)
                    .name(UUID.randomUUID().toString())
                    .build();

            StartExecutionResponse response = sfnClient.startExecution(executionRequest);

            String execution = response.executionArn();

            System.out.println("[execution ]" + execution);

        } catch (JsonProcessingException e) {
            e.printStackTrace();
        }
        return customer;
    }
}
