package com.example.helloworld;

import com.amazonaws.serverless.proxy.model.AwsProxyRequest;
import com.amazonaws.serverless.proxy.model.AwsProxyResponse;
import com.amazonaws.serverless.proxy.model.MultiValuedTreeMap;
import com.amazonaws.services.lambda.runtime.Context;
import com.amazonaws.services.lambda.runtime.RequestStreamHandler;
import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.core.type.TypeReference;
import com.fasterxml.jackson.databind.ObjectMapper;
import org.apache.commons.pool2.impl.GenericObjectPoolConfig;
import redis.clients.jedis.HostAndPort;
import redis.clients.jedis.JedisCluster;

import java.io.*;
import java.nio.charset.StandardCharsets;
import java.util.Collections;
import java.util.Map;

/**
 * Handler for requests to Lambda function.
 */
public class App implements RequestStreamHandler {

    ObjectMapper mapper = new ObjectMapper();

    @Override
    public void handleRequest(InputStream input, OutputStream output, Context context) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(input, StandardCharsets.US_ASCII));
        AwsProxyRequest request = mapper.readValue(reader, AwsProxyRequest.class);
        AwsProxyResponse response = new AwsProxyResponse();
        response.setStatusCode(200);

        String httpMethod = request.getHttpMethod();
        if (httpMethod.equals("GET")) {
            String result = handleGet(request.getMultiValueQueryStringParameters());
            response.setBody(result);
        } else if (httpMethod.equals("POST")) {
            handlePost(request.getBody());
        }

        output.write(mapper.writeValueAsBytes(response));
    }

    private void handlePost(String body) throws JsonProcessingException {
        Map<String, String> requestBody = mapper.readValue(body, new TypeReference<Map<String, String>>() {
        });

        HostAndPort hostAndPort = new HostAndPort(System.getenv("ClusterAddress"), 6379);
        JedisCluster jedisCluster = new JedisCluster(Collections.singleton(hostAndPort), 5000, 5000, 2, null, null, new GenericObjectPoolConfig(), true);
        jedisCluster.hset(requestBody.get("key"), requestBody.get("field"), requestBody.get("value"));
    }

    private String handleGet(MultiValuedTreeMap<String, String> reqParams) throws JsonProcessingException {
        HostAndPort hostAndPort = new HostAndPort(System.getenv("ClusterAddress"), 6379);
        JedisCluster jedisCluster = new JedisCluster(Collections.singleton(hostAndPort), 5000, 5000, 2, null, null, new GenericObjectPoolConfig(), true);
        return jedisCluster.hget(reqParams.get("key").get(0), reqParams.get("field").get(0));
    }
}
