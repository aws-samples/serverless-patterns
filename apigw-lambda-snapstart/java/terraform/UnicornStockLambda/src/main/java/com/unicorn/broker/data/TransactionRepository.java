package com.unicorn.broker.data;

import com.unicorn.broker.model.Transaction;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.stereotype.Component;
import software.amazon.awssdk.core.SdkSystemSetting;
import software.amazon.awssdk.http.crt.AwsCrtAsyncHttpClient;
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.dynamodb.DynamoDbAsyncClient;
import software.amazon.awssdk.services.dynamodb.model.AttributeValue;
import software.amazon.awssdk.services.dynamodb.model.PutItemRequest;

import java.util.HashMap;
import java.util.Map;
import java.util.Optional;
import java.util.concurrent.ExecutionException;

@Component
public class TransactionRepository {

    private static final String TABLE_NAME = System.getenv("TABLE_NAME");
    private final Logger logger = LoggerFactory.getLogger(TransactionRepository.class);
    private final DynamoDbAsyncClient dynamoDbClient = DynamoDbAsyncClient.builder()
            .region(Region.of(System.getenv(SdkSystemSetting.AWS_REGION.environmentVariable())))
            .httpClientBuilder(AwsCrtAsyncHttpClient.builder())
            .build();

    public Optional<Transaction> writeTransaction(Transaction transaction) {
        try {
            dynamoDbClient.putItem(PutItemRequest.builder()
                    .tableName(TABLE_NAME)
                    .item(createTransactionDBItem(transaction))
                    .build())
                    .get();

            return Optional.of(transaction);
        } catch (ExecutionException | InterruptedException e) {
            logger.error("Error while writing transaction to DynamoDB", e);
            return Optional.empty();
        }
    }

    private static Map<String, AttributeValue> createTransactionDBItem(Transaction transaction) {
        Map<String, AttributeValue> item = new HashMap<>();

        item.put("transactionId", AttributeValue.builder().s(transaction.transactionId.toString()).build());
        item.put("stock", AttributeValue.builder().s(transaction.stockId).build());
        item.put("quantity", AttributeValue.builder().n(transaction.quantity.toString()).build());
        item.put("broker_id", AttributeValue.builder().s(transaction.brokerId.toString()).build());

        return item;
    }
}
