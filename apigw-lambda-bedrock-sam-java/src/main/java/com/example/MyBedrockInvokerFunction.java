package com.example;

import static software.amazon.lambda.powertools.utilities.EventDeserializer.extractDataFrom;

import java.nio.charset.Charset;

import org.json.JSONObject;

import com.amazonaws.services.lambda.runtime.Context;
import com.amazonaws.services.lambda.runtime.LambdaLogger;
import com.amazonaws.services.lambda.runtime.RequestHandler;
import com.amazonaws.services.lambda.runtime.events.APIGatewayV2HTTPEvent;
import com.amazonaws.services.lambda.runtime.events.APIGatewayV2HTTPResponse;

import software.amazon.awssdk.core.SdkBytes;
import software.amazon.awssdk.services.bedrockruntime.BedrockRuntimeClient;
import software.amazon.awssdk.services.bedrockruntime.model.InvokeModelRequest;
import software.amazon.awssdk.services.bedrockruntime.model.InvokeModelResponse;


public class MyBedrockInvokerFunction implements RequestHandler<APIGatewayV2HTTPEvent, APIGatewayV2HTTPResponse> {

    private static final String MODEL_ID = "mistral.mistral-7b-instruct-v0:2";
    private final BedrockRuntimeClient bedrockClient;

    record Request(String prompt) { }

    public MyBedrockInvokerFunction() {
        bedrockClient = BedrockRuntimeClient.builder().build();
    }

    public APIGatewayV2HTTPResponse handleRequest(final APIGatewayV2HTTPEvent event, final Context context) {
        LambdaLogger logger = context.getLogger();
        logger.log("Processing request for: " + event.getBody());

        Request content = extractDataFrom(event).as(Request.class);
        JSONObject response = sendRequest(content.prompt);
        logger.log("Response =" + response);

        return APIGatewayV2HTTPResponse.builder()
                .withStatusCode(200)
                .withBody(response.toString())
                .build();
    }

    private JSONObject sendRequest(String prompt) {
        Body body = new Body(prompt);
        InvokeModelRequest request = InvokeModelRequest.builder()
                .modelId(MODEL_ID)
                .body(SdkBytes.fromString(body.toJson(), Charset.defaultCharset()))
                .build();

        InvokeModelResponse invokeModelResponse = bedrockClient.invokeModel(request);

        return new JSONObject(invokeModelResponse.body().asUtf8String());

    }
}