package com.example.inventory;

import com.amazonaws.services.lambda.runtime.Context;
import com.amazonaws.services.lambda.runtime.RequestHandler;
import com.example.model.Customer;
import com.fasterxml.jackson.databind.ObjectMapper;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public class ReserveInventory implements RequestHandler<Customer, String> {

    private static final ObjectMapper MAPPER = new ObjectMapper();
    private static final Logger LOGGER = LoggerFactory.getLogger(ReserveInventory.class);

    @Override
    public String handleRequest(Customer input, Context context) {

        Customer customer = MAPPER.convertValue(input, Customer.class);


        LOGGER.info("[customer] " + customer);


        return "Inventory reserved for customer " + customer.getCustomerId();
    }
}