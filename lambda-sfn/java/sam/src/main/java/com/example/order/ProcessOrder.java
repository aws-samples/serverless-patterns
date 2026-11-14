package com.example.order;

import com.amazonaws.services.lambda.runtime.Context;
import com.amazonaws.services.lambda.runtime.RequestHandler;
import com.example.model.Customer;
import com.fasterxml.jackson.databind.ObjectMapper;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public class ProcessOrder implements RequestHandler<Customer, Customer>  {

    private static final ObjectMapper MAPPER = new ObjectMapper();
    private static final Logger LOGGER = LoggerFactory.getLogger(ProcessOrder.class);

    @Override
    public Customer handleRequest(Customer input, Context context) {

        Customer customer = MAPPER.convertValue(input,Customer.class);

        return customer;
    }
}
