package com.example.utils;

import com.example.model.Ticket;
import software.amazon.awssdk.auth.credentials.EnvironmentVariableCredentialsProvider;
import software.amazon.awssdk.enhanced.dynamodb.DynamoDbEnhancedClient;
import software.amazon.awssdk.enhanced.dynamodb.DynamoDbTable;
import software.amazon.awssdk.enhanced.dynamodb.TableSchema;
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.dynamodb.DynamoDbClient;

import java.util.UUID;

public class DDBUtils {

    private final DynamoDbClient ddb = DynamoDbClient.builder()
            .credentialsProvider(EnvironmentVariableCredentialsProvider.create())
            .region(Region.EU_CENTRAL_1)
            .build();
    private final DynamoDbEnhancedClient enhancedClient = DynamoDbEnhancedClient.builder()
            .dynamoDbClient(ddb)
            .build();

    public String persistTicket(Ticket ticket){

        DynamoDbTable<Ticket> mappedTable = enhancedClient
                .table("tickets", TableSchema.fromBean(Ticket.class));

        String ticketId = UUID.randomUUID().toString();

        ticket.setTicketId(ticketId);

        mappedTable.putItem(ticket);

        return ticketId;
    }
}
