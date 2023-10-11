package com.aws.cqrs.infrastructure.lambda;

import com.amazonaws.services.lambda.runtime.Context;
import com.amazonaws.services.lambda.runtime.RequestHandler;
import com.amazonaws.services.lambda.runtime.events.DynamodbEvent;
import com.amazonaws.services.lambda.runtime.events.models.dynamodb.AttributeValue;
import com.aws.cqrs.application.service.OrderApplicationService;
import com.aws.cqrs.application.service.OrderApplicationServiceImpl;
import com.aws.cqrs.domain.event.OrderCreatedEvent;

import java.util.Map;

public class OrderEventHandler implements RequestHandler<DynamodbEvent, String> {

    @Override
    public String handleRequest(DynamodbEvent ddbEvent, Context context) {

        ddbEvent.getRecords().forEach(record -> {
            try {
                Map<String, AttributeValue> itemMap = record.getDynamodb().getNewImage();
                System.out.println(itemMap);

                OrderApplicationService service = new OrderApplicationServiceImpl();
                String orderId = itemMap.get("orderId").getS();
                String clientId = itemMap.get("clientId").getS();
                String productId = itemMap.get("productId").getS();
                OrderCreatedEvent event = new OrderCreatedEvent(orderId, clientId, productId);

                service.processOrderUpdates(event);
            } catch (Exception ex) {
                System.out.println("Exception occurred: " + ex.getMessage());
            }
        });

        return "Done";
    }


}
