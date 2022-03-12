package com.example.commandService;

import com.amazonaws.services.lambda.runtime.Context;
import com.amazonaws.services.lambda.runtime.RequestHandler;
import com.example.commandService.model.Customer;
import com.example.commandService.utils.DDBUtils;
import com.fasterxml.jackson.databind.ObjectMapper;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.util.UUID;

public class CommandService implements RequestHandler<Customer, String> {

    private static final Logger LOGGER = LoggerFactory.getLogger(CommandService.class);
    private ObjectMapper mapper = new ObjectMapper();
    private DDBUtils ddbUtils;

    @Override
    public String handleRequest(Customer customer, Context context) {

        String commandTableName = System.getenv("COMMAND_TABLE_NAME");
        String region = System.getenv("REGION");

        ddbUtils = new DDBUtils(region);

        LOGGER.info("[customer] " +  customer);

        String customerId = ddbUtils.save(customer, commandTableName);

        return customerId;
    }
}
