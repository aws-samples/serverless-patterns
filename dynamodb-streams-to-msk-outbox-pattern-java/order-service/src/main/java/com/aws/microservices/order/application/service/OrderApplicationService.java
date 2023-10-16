package com.aws.microservices.order.application.service;

import com.aws.microservices.order.application.dto.CreateOrderCommand;
import com.aws.microservices.order.application.dto.OrderConfirmedResponse;

public interface OrderApplicationService {

    OrderConfirmedResponse createOrder(CreateOrderCommand createOrderCommand) throws Exception;

}
