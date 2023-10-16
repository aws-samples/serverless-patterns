package com.aws.microservices.order.application.service;


import com.aws.microservices.order.application.dto.CreateOrderCommand;
import com.aws.microservices.order.application.dto.OrderConfirmedResponse;
import com.aws.microservices.order.domain.event.OrderConfirmedEvent;
import com.aws.microservices.order.infrastructure.dynamodb.persistence.OrderRepository;

public class OrderApplicationServiceImpl implements OrderApplicationService {

    @Override
    public OrderConfirmedResponse createOrder(CreateOrderCommand createOrderCommand) throws Exception {

        OrderRepository orderRepository = new OrderRepository();

        OrderConfirmedEvent orderConfirmedEvent = orderRepository.createOrder(createOrderCommand);

        OrderConfirmedResponse response = OrderConfirmedResponse.builder()
                .orderStatus(orderConfirmedEvent.getOrder().getStatus())
                .orderId(orderConfirmedEvent.getOrder().getOrderId())
                .message("Order Confirmed!")
                .build();

        return response;
    }

}
