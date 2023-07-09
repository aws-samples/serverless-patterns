// Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: MIT-0

package com.unicorn.store.data;

import com.unicorn.store.model.Unicorn;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.stereotype.Service;
import software.amazon.awssdk.core.SdkSystemSetting;
import software.amazon.awssdk.http.crt.AwsCrtAsyncHttpClient;
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.dynamodb.DynamoDbAsyncClient;
import software.amazon.awssdk.services.dynamodb.model.AttributeValue;
import software.amazon.awssdk.services.dynamodb.model.DeleteItemRequest;
import software.amazon.awssdk.services.dynamodb.model.GetItemRequest;
import software.amazon.awssdk.services.dynamodb.model.GetItemResponse;
import software.amazon.awssdk.services.dynamodb.model.PutItemRequest;

import java.util.Map;
import java.util.Optional;
import java.util.UUID;
import java.util.concurrent.ExecutionException;

@Service
public class DynamoDBUnicornRepository implements UnicornRepository {

    private static final Logger logger = LoggerFactory.getLogger(DynamoDBUnicornRepository.class);
    private static final String PRODUCT_TABLE_NAME = System.getenv("PRODUCT_TABLE_NAME");

    private final DynamoDbAsyncClient dynamoDbClient = DynamoDbAsyncClient.builder()
            .region(Region.of(System.getenv(SdkSystemSetting.AWS_REGION.environmentVariable())))
            .httpClientBuilder(AwsCrtAsyncHttpClient.builder())
            .build();

    @Override
    public Unicorn save(Unicorn unicorn) {
        String unicornId = UUID.randomUUID().toString();
        unicorn.setId(unicornId);

        try {
            dynamoDbClient.putItem(PutItemRequest.builder()
                            .tableName(PRODUCT_TABLE_NAME)
                            .item(UnicornMapper.unicornToDynamoDB(unicorn))
                            .build())
                    .get();
        } catch (InterruptedException | ExecutionException e) {
            logger.error("putItem failed with message {}", e.getMessage());
        }

        return unicorn;
    }

    @Override
    public Optional<Unicorn> findById(String unicornId) {
        try {
            GetItemResponse getItemResponse = dynamoDbClient.getItem(GetItemRequest.builder()
                            .key(Map.of("PK", AttributeValue.builder().s(unicornId).build()))
                            .tableName(PRODUCT_TABLE_NAME)
                            .build())
                    .get();
            if (getItemResponse.hasItem()) {
                return Optional.of(UnicornMapper.unicornFromDynamoDB(getItemResponse.item()));
            } else {
                return Optional.empty();
            }
        } catch (InterruptedException | ExecutionException e) {
            logger.error("getItem failed with message {}", e.getMessage());
            return Optional.empty();
        }
    }

    @Override
    public void delete(Unicorn unicorn) {
        dynamoDbClient.deleteItem(DeleteItemRequest.builder()
                .key(Map.of("PK", AttributeValue.builder().s(unicorn.getId()).build()))
                .tableName(PRODUCT_TABLE_NAME)
                .build());
    }
}
