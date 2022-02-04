package com.example.utils;

import com.example.model.Ticket;
import software.amazon.awssdk.enhanced.dynamodb.DynamoDbEnhancedClient;
import software.amazon.awssdk.enhanced.dynamodb.DynamoDbTable;
import software.amazon.awssdk.enhanced.dynamodb.TableSchema;
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.dynamodb.DynamoDbClient;

import java.util.UUID;

public class DDBUtils {

    public static String persistTicket(Ticket ticket){

        DynamoDbClient ddb = DynamoDbClient.builder()
                .region(Region.EU_CENTRAL_1)
                .build();

        DynamoDbEnhancedClient enhancedClient = DynamoDbEnhancedClient.builder()
                .dynamoDbClient(ddb)
                .build();

        DynamoDbTable<Ticket> mappedTable = enhancedClient
                .table("tickets", TableSchema.fromBean(Ticket.class));

        String ticketId = UUID.randomUUID().toString();

        ticket.setTicketId(ticketId);

        mappedTable.putItem(ticket);

        return ticketId;
    }
}
