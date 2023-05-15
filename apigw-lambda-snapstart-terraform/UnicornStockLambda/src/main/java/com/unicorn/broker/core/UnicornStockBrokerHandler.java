package com.unicorn.broker.core;

import com.amazonaws.services.lambda.runtime.events.APIGatewayProxyResponseEvent;
import com.unicorn.broker.model.Transaction;
import org.springframework.stereotype.Component;

import java.util.function.Function;

@Component
public class UnicornStockBrokerHandler implements Function<Transaction, APIGatewayProxyResponseEvent> {

    private final TransactionService transactionService;
    private static final int END_OF_FIRST_UUID_GROUP = 8;

    public UnicornStockBrokerHandler(TransactionService transactionService) {
        this.transactionService = transactionService;
    }

    public APIGatewayProxyResponseEvent apply(final Transaction transaction) {
        if (!transaction.isValid()) {
            return createAPIGwResponse(400, "Invalid request body.");
        }

        var transactionResponse = transactionService.writeTransaction(transaction);
        return transactionResponse
                .map(it -> createAPIGwResponse(200, generateJSONResponse(it)))
                .orElseGet(() ->  createAPIGwResponse(500, "Unexpected error while writing transaction."));
    }

    private APIGatewayProxyResponseEvent createAPIGwResponse(Integer statusCode, String message){
        return new APIGatewayProxyResponseEvent()
                .withStatusCode(statusCode)
                .withBody(String.format("%s%n", message));
    }

    private String generateJSONResponse(Transaction transaction) {
        return String.format("Broker %s successfully created transaction %s", transaction.brokerId.toString().substring(0,END_OF_FIRST_UUID_GROUP), transaction.transactionId);
    }

}
