// Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: MIT-0

package com.unicorn.store.data;

import com.unicorn.store.exceptions.ResourceDeletionException;
import com.unicorn.store.exceptions.ResourceNotFoundException;
import com.unicorn.store.exceptions.ResourceRetrievalException;
import com.unicorn.store.exceptions.ResourceSaveException;
import com.unicorn.store.exceptions.ResourceUpdateException;
import com.unicorn.store.model.Unicorn;
import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;
import org.springframework.stereotype.Repository;
import software.amazon.awssdk.enhanced.dynamodb.DynamoDbTable;
import software.amazon.awssdk.enhanced.dynamodb.Expression;
import software.amazon.awssdk.enhanced.dynamodb.Key;
import software.amazon.awssdk.enhanced.dynamodb.model.UpdateItemEnhancedRequest;
import software.amazon.awssdk.services.dynamodb.model.ConditionalCheckFailedException;
import software.amazon.awssdk.services.dynamodb.model.DynamoDbException;

import java.util.Optional;

@Repository
public class DynamoDBUnicornRepository implements UnicornRepository {

    private static final Logger logger = LogManager.getLogger();

    private final DynamoDbTable<Unicorn> unicornDynamoDbTable;

    public DynamoDBUnicornRepository(DynamoDbTable<Unicorn> unicornDynamoDbTable) {
        this.unicornDynamoDbTable = unicornDynamoDbTable;
    }

    @Override
    public Unicorn save(Unicorn unicorn) {
        logger.info("Saving unicorn with id {} to DynamoDB", unicorn.getId());
        try {
            unicornDynamoDbTable.putItem(unicorn);
            logger.info("Unicorn with id {} saved successfully", unicorn.getId());
            return unicorn;
        } catch (DynamoDbException e) {
            logger.error("Unicorn with id {} could not be saved to DynamoDB", unicorn.getId(), e);
            throw new ResourceSaveException(e.getMessage());
        }
    }

    @Override
    public Optional<Unicorn> findById(String unicornId) {
        try {
            Unicorn unicorn = unicornDynamoDbTable.getItem(Key.builder().partitionValue(unicornId).build());
            if (unicorn == null) {
                logger.info("Unicorn with id {} not found in DynamoDB", unicornId);
                return Optional.empty();
            }
            logger.info("Unicorn with id {} found in DynamoDB", unicornId);
            return Optional.of(unicorn);
        } catch (DynamoDbException e) {
            logger.error("Unicorn with id {} could not be retrieved from DynamoDB", unicornId, e);
            throw new ResourceRetrievalException(e.getMessage());
        }
    }

    @Override
    public void deleteById(String unicornId) {
        try {
            unicornDynamoDbTable.deleteItem(Key.builder().partitionValue(unicornId).build());
            logger.info("Unicorn with id {} deleted successfully", unicornId);
        } catch (DynamoDbException e) {
            logger.error("Unicorn with id {} could not be deleted from DynamoDB", unicornId, e);
            throw new ResourceDeletionException(e.getMessage());
        }
    }

    @Override
    public Unicorn update(Unicorn unicorn) {
        UpdateItemEnhancedRequest<Unicorn> updateItemEnhancedRequest = UpdateItemEnhancedRequest.builder(Unicorn.class)
                .item(unicorn)
                .conditionExpression(Expression.builder().expression("attribute_exists(id)").build())
                .build();
        try {
            unicornDynamoDbTable.updateItem(updateItemEnhancedRequest);
            logger.info("Unicorn with id {} updated successfully", unicorn.getId());
            return unicorn;
        } catch (ConditionalCheckFailedException e) {
            logger.error("Unicorn with id {} could not be updated in DynamoDB", unicorn.getId(), e);
            throw new ResourceNotFoundException(String.format("Unicorn with id %s not found", unicorn.getId()));
        } catch (DynamoDbException e) {
            logger.error("Unicorn with id {} could not be updated in DynamoDB", unicorn.getId(), e);
            throw new ResourceUpdateException(e.getMessage());
        }
    }

}
