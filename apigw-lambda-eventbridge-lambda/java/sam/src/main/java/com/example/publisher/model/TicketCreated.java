package com.example.publisher.model;

import com.fasterxml.jackson.annotation.JsonProperty;

import java.io.Serializable;
import java.util.Objects;

public class TicketCreated implements Serializable {
  private static final long serialVersionUID = 1L;

  @JsonProperty("data")
  private Data data = null;

  @JsonProperty("medatada")
  private Medatada medatada = null;

  public TicketCreated data(Data data) {
    this.data = data;
    return this;
  }
  

  public Data getData() {
    return data;
  }

  public void setData(Data data) {
    this.data = data;
  }

  public TicketCreated medatada(Medatada medatada) {
    this.medatada = medatada;
    return this;
  }
  

  public Medatada getMedatada() {
    return medatada;
  }

  public void setMedatada(Medatada medatada) {
    this.medatada = medatada;
  }

  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    TicketCreated ticketCreated = (TicketCreated) o;
    return Objects.equals(this.data, ticketCreated.data) &&
        Objects.equals(this.medatada, ticketCreated.medatada);
  }

  @Override
  public int hashCode() {
    return Objects.hash(data, medatada);
  }


  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class TicketCreated {\n");
    
    sb.append("    data: ").append(toIndentedString(data)).append("\n");
    sb.append("    medatada: ").append(toIndentedString(medatada)).append("\n");
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
