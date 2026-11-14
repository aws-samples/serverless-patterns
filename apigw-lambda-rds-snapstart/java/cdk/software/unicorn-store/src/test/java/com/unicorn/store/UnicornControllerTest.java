package com.unicorn.store;

import com.amazonaws.serverless.exceptions.ContainerInitializationException;
import com.amazonaws.serverless.proxy.internal.testutils.MockLambdaContext;
import com.amazonaws.serverless.proxy.model.AwsProxyRequest;
import com.amazonaws.serverless.proxy.model.AwsProxyResponse;
import com.amazonaws.serverless.proxy.model.SingleValueHeaders;
import com.amazonaws.services.lambda.runtime.Context;
import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.unicorn.store.model.Unicorn;
import io.micronaut.context.ApplicationContext;
import io.micronaut.core.util.CollectionUtils;
import io.micronaut.function.aws.proxy.MicronautLambdaHandler;
import io.micronaut.http.HttpHeaders;
import io.micronaut.http.HttpMethod;
import io.micronaut.http.MediaType;
import org.junit.jupiter.api.Test;
import java.util.List;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertNotNull;
import static org.junit.jupiter.api.Assertions.assertTrue;

class UnicornControllerTest {

    private static final Context lambdaContext = new MockLambdaContext();

    @Test
    void unicornCrud() throws ContainerInitializationException, JsonProcessingException {
        MicronautLambdaHandler handler = new MicronautLambdaHandler();
        Unicorn unicorn = pojo();
        ObjectMapper objectMapper = handler.getApplicationContext().getBean(ObjectMapper.class);
        AwsProxyRequest createRequest = create(unicorn, objectMapper);
        AwsProxyResponse response = handler.handleRequest(createRequest, lambdaContext);
        assertEquals(201, response.getStatusCode());
        List<String> paths = response.getMultiValueHeaders().get(HttpHeaders.LOCATION);
        assertNotNull(paths);
        assertTrue(CollectionUtils.isNotEmpty(paths));
        String path = paths.get(0);

        AwsProxyRequest getRequest = get(path);
        AwsProxyResponse getResponse = handler.handleRequest(getRequest, lambdaContext);
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

    AwsProxyRequest create(Unicorn unicorn, ObjectMapper objectMapper) throws JsonProcessingException {
        AwsProxyRequest proxyRequest = new AwsProxyRequest();
        proxyRequest.setBody(sampleBody(unicorn, objectMapper));
        SingleValueHeaders headers = new SingleValueHeaders();
        headers.put(HttpHeaders.CONTENT_TYPE, MediaType.APPLICATION_JSON);
        proxyRequest.setHeaders(headers);
        proxyRequest.setPath("/unicorns");
        proxyRequest.setHttpMethod(HttpMethod.POST.toString());
        return proxyRequest;
    }

    AwsProxyRequest get(String path) {
        AwsProxyRequest proxyRequest = new AwsProxyRequest();
        SingleValueHeaders headers = new SingleValueHeaders();
        headers.put(HttpHeaders.ACCEPT, MediaType.APPLICATION_JSON);
        proxyRequest.setHeaders(headers);
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
