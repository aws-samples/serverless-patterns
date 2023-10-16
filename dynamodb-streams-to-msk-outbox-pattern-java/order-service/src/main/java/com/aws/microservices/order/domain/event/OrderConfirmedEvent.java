package com.aws.microservices.order.domain.event;

import com.aws.microservices.order.infrastructure.dynamodb.model.Order;

import java.util.Date;

public class OrderConfirmedEvent extends OrderEvent{

    public OrderConfirmedEvent(Order order, Date createdAt) {
        super(order, createdAt);
    }
}
