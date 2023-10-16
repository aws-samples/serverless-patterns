package com.aws.microservices.order.application.dto;

import com.aws.microservices.order.domain.valueobject.OrderStatus;
import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Getter;

import java.util.UUID;

@Getter
@Builder
@AllArgsConstructor
public class OrderConfirmedResponse {

    private final String orderId;

    private final String orderStatus;

    private final String message;

}