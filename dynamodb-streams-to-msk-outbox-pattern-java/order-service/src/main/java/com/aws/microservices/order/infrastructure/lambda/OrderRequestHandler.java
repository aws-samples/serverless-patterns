package com.aws.microservices.order.infrastructure.lambda;

import com.amazonaws.serverless.proxy.model.AwsProxyRequest;
import com.amazonaws.serverless.proxy.model.AwsProxyResponse;
import com.amazonaws.services.lambda.runtime.Context;
import com.amazonaws.services.lambda.runtime.RequestStreamHandler;
import com.aws.microservices.order.application.dto.CreateOrderCommand;
import com.aws.microservices.order.application.service.OrderApplicationService;
import com.aws.microservices.order.application.service.OrderApplicationServiceImpl;
import com.fasterxml.jackson.databind.ObjectMapper;
import lombok.extern.slf4j.Slf4j;
import software.amazon.awssdk.http.HttpStatusCode;
import software.amazon.awssdk.http.SdkHttpMethod;

import java.io.*;
import java.nio.charset.StandardCharsets;

@Slf4j
public class OrderRequestHandler implements RequestStreamHandler {

    private static final ObjectMapper mapper = new ObjectMapper();

    @Override
    public void handleRequest(InputStream input, OutputStream output, Context context) throws IOException {

        BufferedReader reader = new BufferedReader(new InputStreamReader(input, StandardCharsets.US_ASCII));
        AwsProxyRequest request = mapper.readValue(reader, AwsProxyRequest.class);

        AwsProxyResponse awsProxyResponse = new AwsProxyResponse();

        try {

            awsProxyResponse.setStatusCode(HttpStatusCode.OK);

            if (request.getHttpMethod().equalsIgnoreCase(SdkHttpMethod.POST.name())) {

                log.info("Logging:Inside POST...:::"+request.getBody());

                CreateOrderCommand createOrderCommand = mapper.readValue(request.getBody(), CreateOrderCommand.class);
                log.debug("createOrderCommand::{}", createOrderCommand);

                OrderApplicationService service = new OrderApplicationServiceImpl();
                service.createOrder(createOrderCommand);
            }

            if (request.getHttpMethod().equalsIgnoreCase(SdkHttpMethod.GET.name())) {
                log.debug("Inside GET...");
            }

        } catch (Exception e) {

            log.error("Error processing...{}", e.getMessage());

            awsProxyResponse.setStatusCode(HttpStatusCode.INTERNAL_SERVER_ERROR);
            output.write(mapper.writeValueAsString(awsProxyResponse).getBytes());
        }
        output.write(mapper.writeValueAsString(awsProxyResponse).getBytes());
    }
}
