package com.aws.cqrs.infrastructure.lambda;

import com.amazonaws.services.lambda.runtime.Context;
import com.amazonaws.services.lambda.runtime.RequestHandler;
import com.aws.cqrs.application.service.OrderApplicationService;
import com.aws.cqrs.application.service.OrderApplicationServiceImpl;

import java.util.Map;

public class OrderQueryHandler implements RequestHandler<Map<String, String>, String> {

    @Override
    public String handleRequest(Map<String, String> requestMap, Context context) {
        OrderApplicationService service = new OrderApplicationServiceImpl();
        return service.getOrder(requestMap.get("orderId"));
    }
}
