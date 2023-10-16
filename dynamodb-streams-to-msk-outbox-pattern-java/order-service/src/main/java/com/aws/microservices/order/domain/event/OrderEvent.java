package com.aws.microservices.order.domain.event;

import com.aws.microservices.order.infrastructure.dynamodb.model.Order;

import java.util.Date;


public abstract class OrderEvent implements DomainEvent<Order> {
    private final Order order;
    private final Date createdAt;

    public OrderEvent(Order order, Date createdAt) {
        this.order = order;
        this.createdAt = createdAt;
    }

    public Order getOrder() {
        return order;
    }

    public Date getCreatedAt() {
        return createdAt;
    }
}
