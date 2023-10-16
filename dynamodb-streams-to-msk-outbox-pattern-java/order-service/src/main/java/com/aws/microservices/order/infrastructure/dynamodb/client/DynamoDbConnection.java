package com.aws.microservices.order.infrastructure.dynamodb.client;

import software.amazon.awssdk.enhanced.dynamodb.DynamoDbEnhancedClient;
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.dynamodb.DynamoDbClient;

public class DynamoDbConnection {

    public static DynamoDbEnhancedClient getDynamoDbEnhancedClient() {

        return DynamoDbEnhancedClient.builder().dynamoDbClient(dynamoDbClient()).build();

    }

    public static DynamoDbClient dynamoDbClient() {

        //return DynamoDbClient.builder().region(Region.US_EAST_1).build();
        return DynamoDbClient.builder().build();
    }

}
