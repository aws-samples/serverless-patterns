package com.example.subscriber.model;

import com.fasterxml.jackson.annotation.JsonProperty;

import java.util.Date;
import java.util.List;
import java.util.Objects;

public class AWSEvent<T> {

  @JsonProperty("detail")
  private T detail = null;

  @JsonProperty("detail-type")
  private String detailType = null;

  @JsonProperty("resources")
  private List resources = null;

  @JsonProperty("id")
  private String id = null;

  @JsonProperty("source")
  private String source = null;

  @JsonProperty("time")
  private Date time = null;

  @JsonProperty("region")
  private String region = null;

  @JsonProperty("version")
  private String version = null;

  @JsonProperty("account")
  private String account = null;

  public AWSEvent<T> detail(T detail) {
    this.detail = detail;
    return this;
  }

  public T getDetail() {
    return detail;
  }

  public void setDetail(T detail) {
    this.detail = detail;
  }

  public AWSEvent<T> detailType(String detailType) {
    this.detailType = detailType;
    return this;
  }

  public String getDetailType() {
    return detailType;
  }

  public void setDetailType(String detailType) {
    this.detailType = detailType;
  }

  public AWSEvent<T> resources(List resources) {
    this.resources = resources;
    return this;
  }

  public List getResources() {
    return resources;
  }

  public void setResources(List resources) {
    this.resources = resources;
  }

  public AWSEvent<T> id(String id) {
    this.id = id;
    return this;
  }

  public String getId() {
    return id;
  }

  public void setId(String id) {
    this.id = id;
  }

  public AWSEvent<T> source(String source) {
    this.source = source;
    return this;
  }

  public String getSource() {
    return source;
  }

  public void setSource(String source) {
    this.source = source;
  }

  public AWSEvent<T> time(Date time) {
    this.time = time;
    return this;
  }

  public Date getTime() {
    return time;
  }

  public void setTime(Date time) {
    this.time = time;
  }

  public AWSEvent<T> region(String region) {
    this.region = region;
    return this;
  }

  public String getRegion() {
    return region;
  }

  public void setRegion(String region) {
    this.region = region;
  }

  public AWSEvent<T> version(String version) {
    this.version = version;
    return this;
  }

  public String getVersion() {
    return version;
  }

  public void setVersion(String version) {
    this.version = version;
  }

  public AWSEvent<T> account(String account) {
    this.account = account;
    return this;
  }

  public String getAccount() {
    return account;
  }

  public void setAccount(String account) {
    this.account = account;
  }

  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    AWSEvent awSEvent = (AWSEvent) o;
    return Objects.equals(this.detail, awSEvent.detail) &&
        Objects.equals(this.detailType, awSEvent.detailType) &&
        Objects.equals(this.resources, awSEvent.resources) &&
        Objects.equals(this.id, awSEvent.id) &&
        Objects.equals(this.source, awSEvent.source) &&
        Objects.equals(this.time, awSEvent.time) &&
        Objects.equals(this.region, awSEvent.region) &&
        Objects.equals(this.version, awSEvent.version) &&
        Objects.equals(this.account, awSEvent.account);
  }

  @Override
  public int hashCode() {
    return Objects.hash(detail, detailType, resources, id, source, time, region, version, account);
  }


  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class AWSEvent {\n");

    sb.append("    detail: ").append(toIndentedString(detail)).append("\n");
    sb.append("    detailType: ").append(toIndentedString(detailType)).append("\n");
    sb.append("    resources: ").append(toIndentedString(resources)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    source: ").append(toIndentedString(source)).append("\n");
    sb.append("    time: ").append(toIndentedString(time)).append("\n");
    sb.append("    region: ").append(toIndentedString(region)).append("\n");
    sb.append("    version: ").append(toIndentedString(version)).append("\n");
    sb.append("    account: ").append(toIndentedString(account)).append("\n");
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
