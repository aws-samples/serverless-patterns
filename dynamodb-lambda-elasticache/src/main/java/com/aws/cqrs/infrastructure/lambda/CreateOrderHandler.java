package com.aws.cqrs.infrastructure.lambda;

import com.amazonaws.services.lambda.runtime.Context;
import com.amazonaws.services.lambda.runtime.RequestHandler;
import com.aws.cqrs.application.dto.OrderRequest;
import com.aws.cqrs.application.service.OrderApplicationService;
import com.aws.cqrs.application.service.OrderApplicationServiceImpl;

public class CreateOrderHandler implements RequestHandler<OrderRequest, String> {

    @Override
    public String handleRequest(OrderRequest orderRequest, Context context) {
        OrderApplicationService service = new OrderApplicationServiceImpl();
        return service.createOrder(orderRequest);
    }
}
