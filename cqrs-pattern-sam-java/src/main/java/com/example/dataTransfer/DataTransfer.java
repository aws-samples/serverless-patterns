package com.example.dataTransfer;

import com.amazonaws.services.lambda.runtime.Context;
import com.amazonaws.services.lambda.runtime.RequestHandler;
import com.amazonaws.services.lambda.runtime.events.DynamodbEvent;
import com.amazonaws.services.lambda.runtime.events.models.dynamodb.AttributeValue;
import com.example.commandService.model.Customer;
import com.example.commandService.utils.DDBUtils;

import java.util.ArrayList;
import java.util.List;
import java.util.Map;

public class DataTransfer implements RequestHandler<DynamodbEvent, String> {

    private DDBUtils ddbUtils;

    @Override
    public String handleRequest(DynamodbEvent dynamodbEvent, Context context) {

        String queryTableName = System.getenv("QUERY_TABLE_NAME");
        String region = System.getenv("REGION");

        ddbUtils = new DDBUtils(region);

        List<Customer> customers = new ArrayList<>();

        dynamodbEvent.getRecords().forEach(record -> {

            System.out.println("getDescription " + record.getDynamodb().getNewImage().get("description"));

            Map<String, AttributeValue> image = record.getDynamodb().getNewImage();
            Customer ticketExpert = new Customer(image.get("id").getS(),
                    image.get("username").getS(),
                    image.get("email").getS());

            customers.add(ticketExpert);
        });

        ddbUtils.saveIntoQueryDDB(customers, queryTableName);

        return null;
    }
}
