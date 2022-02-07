package com.example.subscriber.model;

import com.fasterxml.jackson.databind.DeserializationFeature;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.databind.type.TypeFactory;

import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;

public class Marshaller {

  private static final ObjectMapper MAPPER = createObjectMapper();

  public static <T> void marshal(OutputStream output, T value) throws IOException {
    MAPPER.writeValue(output, value);
  }

  public static <T> T unmarshal(InputStream input, Class<T> type) throws IOException {
    return MAPPER.readValue(input, type);
  }

  public static <T> AWSEvent<T> unmarshalEvent(InputStream input, Class<T> type) throws IOException {
    final TypeFactory typeFactory = MAPPER.getTypeFactory();
    return MAPPER.readValue(input, typeFactory.constructParametricType(AWSEvent.class, type));
  }

  private static ObjectMapper createObjectMapper() {
    return new ObjectMapper()
            .findAndRegisterModules()
            .disable(DeserializationFeature.FAIL_ON_UNKNOWN_PROPERTIES);
  }
}
