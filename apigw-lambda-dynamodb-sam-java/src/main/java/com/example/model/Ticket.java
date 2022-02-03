package com.example.model;

import com.fasterxml.jackson.annotation.JsonProperty;
import software.amazon.awssdk.enhanced.dynamodb.mapper.annotations.DynamoDbBean;
import software.amazon.awssdk.enhanced.dynamodb.mapper.annotations.DynamoDbPartitionKey;

import java.io.Serializable;
import java.util.Objects;

@DynamoDbBean
public class Ticket implements Serializable {
  private static final long serialVersionUID = 1L;

  @JsonProperty("ticketId")
  private String ticketId = null;

  @JsonProperty("description")
  private String description = null;

  @JsonProperty("userId")
  private String userId = null;

  public Ticket() {
  }

  public Ticket(String ticketId, String description, String userId) {
    this.ticketId = ticketId;
    this.description = description;
    this.userId = userId;
  }

  @DynamoDbPartitionKey
  public String getTicketId() {
    return ticketId;
  }

  public void setTicketId(String ticketId) {
    this.ticketId = ticketId;
  }

  public String getDescription() {
    return description;
  }

  public void setDescription(String description) {
    this.description = description;
  }

  public String getUserId() {
    return userId;
  }

  public void setUserId(String userId) {
    this.userId = userId;
  }
}
