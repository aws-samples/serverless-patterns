package com.example.publisher.model;

import com.fasterxml.jackson.annotation.JsonProperty;

import java.io.Serializable;
import java.util.Objects;

public class Data implements Serializable {
  private static final long serialVersionUID = 1L;

  @JsonProperty("issue")
  private String issue = null;

  @JsonProperty("userId")
  private String userId = null;

  public Data issue(String issue) {
    this.issue = issue;
    return this;
  }
  

  public String getIssue() {
    return issue;
  }

  public void setIssue(String issue) {
    this.issue = issue;
  }

  public Data userId(String userId) {
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
    Data data = (Data) o;
    return Objects.equals(this.issue, data.issue) &&
        Objects.equals(this.userId, data.userId);
  }

  @Override
  public int hashCode() {
    return Objects.hash(issue, userId);
  }


  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class Data {\n");
    
    sb.append("    issue: ").append(toIndentedString(issue)).append("\n");
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
