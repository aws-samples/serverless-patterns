package com.example;

import com.amazonaws.services.lambda.runtime.Context;
import com.amazonaws.services.lambda.runtime.LambdaLogger;
import software.amazon.awssdk.auth.credentials.EnvironmentVariableCredentialsProvider;
import software.amazon.awssdk.http.urlconnection.UrlConnectionHttpClient;
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.ssm.SsmClient;
import software.amazon.awssdk.services.ssm.model.GetParameterRequest;
import software.amazon.awssdk.services.ssm.model.GetParameterResponse;
import software.amazon.awssdk.services.ssm.model.PutParameterRequest;
import software.amazon.awssdk.services.ssm.model.PutParameterResponse;

import java.util.Map;

public class App {

    private final SsmClient ssmClient = SsmClient.builder()
            .region(Region.of(System.getenv("AWS_REGION")))
            .credentialsProvider(EnvironmentVariableCredentialsProvider.create())
            .httpClient(UrlConnectionHttpClient.builder().build())
            .build();
    private final String ssmParameterName = System.getenv("SSMParameterName");

    public String handleRequest(final Map<String, String> event, final Context context) {
        LambdaLogger logger = context.getLogger();
        String result;

        final String method = event.get("method");
        final String body = event.get("body");

        logger.log(String.format("Method: %s", method));
        logger.log(String.format("Body: %s", body));

        if (method.equals("PUT")) {
            PutParameterRequest request = PutParameterRequest.builder()
                    .name(ssmParameterName)
                    .value(body)
                    .overwrite(true)
                    .dataType("text")
                    .build();
            PutParameterResponse response = ssmClient.putParameter(request);
            result = response.toString();
        } else if (method.equals("GET")) {
            GetParameterRequest request = GetParameterRequest.builder()
                    .name(ssmParameterName)
                    .build();
            GetParameterResponse response = ssmClient.getParameter(request);
            result = response.toString();
        } else {
            result = "Method not supported";
        }
        logger.log(String.format("Result: %s", result));
        return result;
    }

}