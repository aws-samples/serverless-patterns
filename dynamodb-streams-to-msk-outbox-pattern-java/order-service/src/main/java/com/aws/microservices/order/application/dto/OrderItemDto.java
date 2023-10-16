package com.aws.microservices.order.application.dto;

import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Getter;
import lombok.NoArgsConstructor;

import java.math.BigDecimal;

@Getter
@Builder
@AllArgsConstructor
@NoArgsConstructor
public class OrderItemDto {

    private String productId;

    private Integer quantity;

    private BigDecimal price;

}
