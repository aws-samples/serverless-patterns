package com.example.model;

import com.fasterxml.jackson.annotation.JsonProperty;

import java.io.Serializable;
import java.util.Objects;

public class OrderCreated implements Serializable {
  private static final long serialVersionUID = 1L;

  @JsonProperty("orderId")
  private String orderId = null;

  @JsonProperty("total")
  private String total = null;

  @JsonProperty("userId")
  private String userId = null;

  public OrderCreated orderId(String orderId) {
    this.orderId = orderId;
    return this;
  }
  

  public String getOrderId() {
    return orderId;
  }

  public void setOrderId(String orderId) {
    this.orderId = orderId;
  }

  public OrderCreated total(String total) {
    this.total = total;
    return this;
  }
  

  public String getTotal() {
    return total;
  }

  public void setTotal(String total) {
    this.total = total;
  }

  public OrderCreated userId(String userId) {
    this.userId = userId;
    return this;
  }
  

  public String getUserId() {
    return userId;
  }

  public void setUserId(String userId) {
    this.userId = userId;
  }

  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    OrderCreated orderCreated = (OrderCreated) o;
    return Objects.equals(this.orderId, orderCreated.orderId) &&
        Objects.equals(this.total, orderCreated.total) &&
        Objects.equals(this.userId, orderCreated.userId);
  }

  @Override
  public int hashCode() {
    return Objects.hash(orderId, total, userId);
  }


  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("{\n");
    
    sb.append("    orderId: ").append(toIndentedString(orderId)).append("\n");
    sb.append("    total: ").append(toIndentedString(total)).append("\n");
    sb.append("    userId: ").append(toIndentedString(userId)).append("\n");
    sb.append("}");
    return sb.toString();
  }

  private String toIndentedString(Object o) {
    if (o == null) {
      return "null";
    }
    return o.toString().replace("\n", "\n    ");
  }

}
