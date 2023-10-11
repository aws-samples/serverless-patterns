package com.aws.cqrs.domain.event;

import com.amazonaws.services.lambda.runtime.events.models.dynamodb.AttributeValue;
import com.aws.cqrs.domain.model.Order;
import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;

import java.util.Map;

@Builder
@Data
@NoArgsConstructor
@AllArgsConstructor
public class OrderCreatedEvent {

    private String orderId = null;
    private String clientId = null;
    private String productId = null;

    public Order toOrder() {
        return Order.builder()
                .orderId(orderId)
                .clientId(clientId)
                .productId(productId)
                .build();
    }
}
