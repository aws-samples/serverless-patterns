package com.unicorn.store;

import com.amazonaws.services.lambda.runtime.Context;
import com.amazonaws.services.lambda.runtime.events.APIGatewayProxyRequestEvent;
import com.amazonaws.services.lambda.runtime.events.APIGatewayProxyResponseEvent;
import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.unicorn.store.model.Unicorn;
import io.micronaut.context.ApplicationContext;
import io.micronaut.function.aws.proxy.MockLambdaContext;
import io.micronaut.function.aws.proxy.payload1.ApiGatewayProxyRequestEventFunction;
import io.micronaut.http.HttpHeaders;
import io.micronaut.http.HttpMethod;
import io.micronaut.http.MediaType;
import org.junit.jupiter.api.Test;
import java.util.Map;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertNotNull;

class UnicornControllerTest {

    private static final Context lambdaContext = new MockLambdaContext();

    @Test
    void unicornCrud() throws JsonProcessingException {
        ApiGatewayProxyRequestEventFunction handler = new ApiGatewayProxyRequestEventFunction();
        Unicorn unicorn = pojo();
        ObjectMapper objectMapper = handler.getApplicationContext().getBean(ObjectMapper.class);
        APIGatewayProxyRequestEvent createRequest = create(unicorn, objectMapper);
        APIGatewayProxyResponseEvent response = handler.handleRequest(createRequest, lambdaContext);
        assertEquals(201, response.getStatusCode());
        String path = response.getHeaders().get(HttpHeaders.LOCATION);
        assertNotNull(path);

        APIGatewayProxyRequestEvent getRequest = get(path);
        APIGatewayProxyResponseEvent getResponse = handler.handleRequest(getRequest, lambdaContext);
        assertEquals(200, getResponse.getStatusCode());

        unicorn.setId(path.substring("/unicorns/".length()));
        Unicorn received = objectMapper.readValue(getResponse.getBody(), Unicorn.class);
        assertEquals(unicorn.getId(), received.getId());
        assertEquals(unicorn.getAge(), received.getAge());
        assertEquals(unicorn.getName(), received.getName());
        assertEquals(unicorn.getType(), received.getType());
        assertEquals(unicorn.getSize(), received.getSize());
        handler.close();
    }

    APIGatewayProxyRequestEvent create(Unicorn unicorn, ObjectMapper objectMapper) throws JsonProcessingException {
        APIGatewayProxyRequestEvent proxyRequest = new APIGatewayProxyRequestEvent();
        proxyRequest.setBody(sampleBody(unicorn, objectMapper));
        proxyRequest.setHeaders(Map.of(HttpHeaders.CONTENT_TYPE, MediaType.APPLICATION_JSON));
        proxyRequest.setPath("/unicorns");
        proxyRequest.setHttpMethod(HttpMethod.POST.toString());
        return proxyRequest;
    }

    APIGatewayProxyRequestEvent get(String path) {
        APIGatewayProxyRequestEvent proxyRequest = new APIGatewayProxyRequestEvent();
        proxyRequest.setHeaders(Map.of(HttpHeaders.ACCEPT, MediaType.APPLICATION_JSON));
        proxyRequest.setPath(path);
        proxyRequest.setHttpMethod(HttpMethod.GET.toString());
        return proxyRequest;
    }

    private Unicorn pojo() {
        Unicorn unicorn = new Unicorn();
        unicorn.setName("John");
        unicorn.setAge("8");
        unicorn.setSize("XL");
        unicorn.setType("White");
        return unicorn;
    }

    private String sampleBody(Unicorn unicorn, ObjectMapper objectMapper) throws JsonProcessingException {
        return objectMapper.writeValueAsString(unicorn);
    }
}
