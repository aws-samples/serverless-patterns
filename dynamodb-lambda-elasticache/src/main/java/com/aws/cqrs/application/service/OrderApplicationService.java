package com.aws.cqrs.application.service;

import com.aws.cqrs.application.dto.OrderRequest;
import com.aws.cqrs.domain.event.OrderCreatedEvent;

public interface OrderApplicationService {

    String createOrder(OrderRequest orderRequest);

    void processOrderUpdates(OrderCreatedEvent orderCreatedEvent);

    String getOrder(String orderId);
}
