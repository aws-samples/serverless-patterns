package com.aws.microservices.order.infrastructure.dynamodb.persistence;


import com.aws.microservices.order.application.dto.CreateOrderCommand;
import com.aws.microservices.order.application.dto.OrderItemDto;
import com.aws.microservices.order.domain.event.OrderConfirmedEvent;
import com.aws.microservices.order.domain.util.DateUtil;
import com.aws.microservices.order.domain.valueobject.OrderStatus;
import com.aws.microservices.order.infrastructure.dynamodb.client.DynamoDbConnection;
import com.aws.microservices.order.infrastructure.dynamodb.model.Order;
import com.aws.microservices.order.infrastructure.dynamodb.model.OrderItem;
import com.aws.microservices.order.infrastructure.dynamodb.model.OrderNotificationOutbox;
import com.fasterxml.jackson.databind.ObjectMapper;
import lombok.extern.slf4j.Slf4j;
import software.amazon.awssdk.enhanced.dynamodb.MappedTableResource;
import software.amazon.awssdk.enhanced.dynamodb.TableSchema;
import software.amazon.awssdk.enhanced.dynamodb.model.TransactPutItemEnhancedRequest;
import software.amazon.awssdk.enhanced.dynamodb.model.TransactWriteItemsEnhancedRequest;
import software.amazon.awssdk.enhanced.dynamodb.model.TransactWriteItemsEnhancedRequest.Builder;

import java.util.ArrayList;
import java.util.Date;
import java.util.List;
import java.util.UUID;

@Slf4j
public class OrderRepository {

    private final ObjectMapper mapper = new ObjectMapper();

    public OrderConfirmedEvent createOrder(CreateOrderCommand createOrderCommand) throws Exception {

        /*
         * Write to DynamoDB tables order and NotificationOutbox with transactional writes...
         */

        Order order = buildOrder(createOrderCommand);

        log.debug("order..."+order);

        TransactPutItemEnhancedRequest<Order> orderRequest = TransactPutItemEnhancedRequest.builder(Order.class)
                .item(order).build();

        List<OrderItem> orderItems = buildOrderItems(createOrderCommand, order.getOrderId());

        // Build transaction request
        Builder transactRequest = TransactWriteItemsEnhancedRequest.builder();
        transactRequest.addPutItem(getOrderTable(), orderRequest);

        for (OrderItem oi : orderItems) {
            log.debug("oi.."+oi);
            transactRequest.addPutItem(getOrderItemTable(),
                    TransactPutItemEnhancedRequest.builder(OrderItem.class).item(oi).build());

        }

        // add outbox details..
        OrderNotificationOutbox orderOutbox = OrderNotificationOutbox.builder()
                .createdAt(DateUtil.getFormattedDate(new Date()))
                .id(UUID.randomUUID().toString())
                .orderId(order.getOrderId())
                .orderStatus(OrderStatus.APPROVED)
                .createdAt(DateUtil.getFormattedDate(new Date()))
                .customerId(createOrderCommand.getCustomerId())
                .payload(mapper.writeValueAsString(order))
                .build();


        transactRequest.addPutItem(getNotificationOutboxTable(), TransactPutItemEnhancedRequest.builder(OrderNotificationOutbox.class).item(orderOutbox).build());

        DynamoDbConnection.getDynamoDbEnhancedClient().transactWriteItems(transactRequest.build());

        return new OrderConfirmedEvent(order,new Date());
    }

    private Order buildOrder(CreateOrderCommand orderCommand) {
        if (null == orderCommand)
            return null;

        return Order.builder()
                .orderId(UUID.randomUUID().toString())
                .customerId(orderCommand.getCustomerId())
                .orderedDateTime(DateUtil.getFormattedDate(new Date()))
                .price(orderCommand.getPrice())
                .build();
    }

    private List<OrderItem> buildOrderItems(CreateOrderCommand orderCommand, String orderId) {
        if (null == orderCommand)
            return null;

        List<OrderItem> items = new ArrayList<>();
        for (OrderItemDto itemDto : orderCommand.getItems()) {
            items.add(OrderItem.builder().orderId(orderId).orderItemId(UUID.randomUUID().toString())
                    .price(itemDto.getPrice()).productId(itemDto.getProductId()).quantity(itemDto.getQuantity())
                    .build());
        }
        return items;
    }

    private MappedTableResource<Order> getOrderTable() {
        return DynamoDbConnection.getDynamoDbEnhancedClient().table("Order", TableSchema.fromBean(Order.class));
    }

    private MappedTableResource<OrderItem> getOrderItemTable() {
        return DynamoDbConnection.getDynamoDbEnhancedClient().table("OrderItem", TableSchema.fromBean(OrderItem.class));
    }

    private MappedTableResource<OrderNotificationOutbox> getNotificationOutboxTable() {
        return DynamoDbConnection.getDynamoDbEnhancedClient().table("OrderNotificationOutbox",
                TableSchema.fromBean(OrderNotificationOutbox.class));
    }

}
