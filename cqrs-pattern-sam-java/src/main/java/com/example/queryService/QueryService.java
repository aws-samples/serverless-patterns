package com.example.queryService;

import com.amazonaws.services.lambda.runtime.Context;
import com.amazonaws.services.lambda.runtime.RequestHandler;
import com.example.queryService.model.QueryCustomer;
import com.example.queryService.utils.QueryDDBUtils;

import java.util.List;

public class QueryService implements RequestHandler {

    private QueryDDBUtils ddbUtils;

    @Override
    public List<QueryCustomer> handleRequest(Object o, Context context) {

        String queryTableName = System.getenv("QUERY_TABLE_NAME");
        String region = System.getenv("REGION");

        ddbUtils = new QueryDDBUtils(region);

        List<QueryCustomer> customers = ddbUtils.getAllCustomers(queryTableName);

        customers.stream().forEach(System.out::println);

        return customers;
    }
}
