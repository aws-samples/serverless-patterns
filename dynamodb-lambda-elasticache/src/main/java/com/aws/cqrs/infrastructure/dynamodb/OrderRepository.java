package com.aws.cqrs.infrastructure.dynamodb;

import com.aws.cqrs.domain.model.Order;
import software.amazon.awssdk.enhanced.dynamodb.DynamoDbEnhancedClient;
import software.amazon.awssdk.enhanced.dynamodb.DynamoDbTable;
import software.amazon.awssdk.enhanced.dynamodb.TableSchema;
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.dynamodb.DynamoDbClient;

import java.util.UUID;

public class OrderRepository {
    public String saveOrder(Order order){

        DynamoDbClient ddb = DynamoDbClient.builder()
                .region(Region.US_EAST_1)
                .build();

        DynamoDbEnhancedClient enhancedClient = DynamoDbEnhancedClient.builder()
                .dynamoDbClient(ddb)
                .build();

        DynamoDbTable<Order> mappedTable = enhancedClient
                .table("CQRSOrders", TableSchema.fromBean(Order.class));

        String orderId = UUID.randomUUID().toString();
        order.setOrderId(orderId);
        mappedTable.putItem(order);

        return orderId;
    }
}
