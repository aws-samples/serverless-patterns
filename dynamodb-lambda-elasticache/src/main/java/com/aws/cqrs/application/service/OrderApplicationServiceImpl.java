package com.aws.cqrs.application.service;

import com.aws.cqrs.application.dto.OrderRequest;
import com.aws.cqrs.domain.event.OrderCreatedEvent;
import com.aws.cqrs.domain.model.Order;
import com.aws.cqrs.infrastructure.dynamodb.OrderRepository;
import com.aws.cqrs.infrastructure.redis.OrderReadRepository;

public class OrderApplicationServiceImpl implements OrderApplicationService {

    @Override
    public String createOrder(OrderRequest orderRequest) {

        /**
         * Write your business logic here
         */

        //Save to dynamoDB
        OrderRepository repository = new OrderRepository();
        return repository.saveOrder(buildOrder(orderRequest));
    }

    @Override
    public void processOrderUpdates(OrderCreatedEvent orderCreatedEvent) {
        /**
         * Write your business logic here
         */

        //Save to Redis cache
        OrderReadRepository repository = new OrderReadRepository();
        repository.saveOrder(orderCreatedEvent.toOrder());
    }

    @Override
    public String getOrder(String orderId) {
        /**
         * Write your business logic here
         */

        //Save to Redis cache
        OrderReadRepository repository = new OrderReadRepository();
        return repository.getOrder(orderId);
    }

    private Order buildOrder(OrderRequest orderRequest) {
        return Order.builder()
                .productId(orderRequest.getProductId())
                .clientId(orderRequest.getClientId())
                .build();
    }

}
