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
import software.amazon.awssdk.enhanced.dynamodb.DynamoDbAsyncTable;
import software.amazon.awssdk.enhanced.dynamodb.Expression;
import software.amazon.awssdk.enhanced.dynamodb.Key;
import software.amazon.awssdk.enhanced.dynamodb.model.UpdateItemEnhancedRequest;
import software.amazon.awssdk.services.dynamodb.model.ConditionalCheckFailedException;

import java.util.Optional;
import java.util.concurrent.ExecutionException;

@Repository
public class DynamoDBUnicornRepository implements UnicornRepository {

    private static final Logger logger = LogManager.getLogger();

    private final DynamoDbAsyncTable<Unicorn> unicornDynamoDbAsyncTable;

    public DynamoDBUnicornRepository(DynamoDbAsyncTable<Unicorn> unicornDynamoDbAsyncTable) {
        this.unicornDynamoDbAsyncTable = unicornDynamoDbAsyncTable;
    }

    @Override
    public Unicorn save(Unicorn unicorn) {
        logger.info("Saving unicorn with id {} to DynamoDB", unicorn.getId());
        try {
            unicornDynamoDbAsyncTable.putItem(unicorn).get();
            logger.info("Unicorn with id {} saved successfully", unicorn.getId());
            return unicorn;
        } catch (ExecutionException e) {
            logger.error("Unicorn with id {} could not be saved to DynamoDB", unicorn.getId(), e);
            throw new ResourceSaveException(e.getMessage());
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
            logger.error("Unicorn with id {} could not be saved to DynamoDB", unicorn.getId(), e);
            throw new ResourceSaveException(e.getMessage());
        }
    }

    @Override
    public Optional<Unicorn> findById(String unicornId) {
        try {
            Unicorn unicorn = unicornDynamoDbAsyncTable.getItem(Key.builder().partitionValue(unicornId).build()).get();
            if (unicorn == null) {
                logger.info("Unicorn with id {} not found in DynamoDB", unicornId);
                return Optional.empty();
            }
            logger.info("Unicorn with id {} found in DynamoDB", unicornId);
            return Optional.of(unicorn);
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
            logger.error("Unicorn with id {} could not be retrieved from DynamoDB", unicornId, e);
            throw new ResourceRetrievalException(e.getMessage());
        } catch (ExecutionException e) {
            logger.error("Unicorn with id {} could not be retrieved from DynamoDB", unicornId, e);
            throw new ResourceRetrievalException(e.getMessage());
        }
    }

    @Override
    public void deleteById(String unicornId) {
        try {
            unicornDynamoDbAsyncTable.deleteItem(Key.builder().partitionValue(unicornId).build()).get();
            logger.info("Unicorn with id {} deleted successfully", unicornId);
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
            logger.error("Unicorn with id {} could not be deleted from DynamoDB", unicornId, e);
            throw new ResourceDeletionException(e.getMessage());
        } catch (ExecutionException e) {
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
            unicornDynamoDbAsyncTable.updateItem(updateItemEnhancedRequest).get();
            logger.info("Unicorn with id {} updated successfully", unicorn.getId());
            return unicorn;
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
            logger.error("Unicorn with id {} could not be updated in DynamoDB", unicorn.getId(), e);
            throw new ResourceUpdateException(e.getMessage());
        } catch (ExecutionException e) {
            logger.error("Unicorn with id {} could not be updated in DynamoDB", unicorn.getId(), e);
            if (e.getCause() instanceof ConditionalCheckFailedException) {
                throw new ResourceNotFoundException(String.format("Unicorn with id %s not found", unicorn.getId()));
            }
            throw new ResourceUpdateException(e.getMessage());
        }
    }

}
