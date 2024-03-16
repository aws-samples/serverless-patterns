package com.example;

import com.amazonaws.services.lambda.runtime.Context;
import com.amazonaws.services.lambda.runtime.LambdaLogger;
import com.amazonaws.services.lambda.runtime.RequestHandler;
import com.amazonaws.services.lambda.runtime.events.APIGatewayV2HTTPEvent;
import com.amazonaws.services.lambda.runtime.events.APIGatewayV2HTTPResponse;
import org.json.JSONObject;
import software.amazon.awssdk.auth.credentials.ProfileCredentialsProvider;
import software.amazon.awssdk.core.SdkBytes;
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.bedrockruntime.BedrockRuntimeClient;
import software.amazon.awssdk.services.bedrockruntime.model.InvokeModelRequest;
import software.amazon.awssdk.services.bedrockruntime.model.InvokeModelResponse;
import software.amazon.lambda.powertools.utilities.EventDeserializer;

import java.nio.charset.Charset;
import java.text.MessageFormat;

import static software.amazon.lambda.powertools.utilities.EventDeserializer.extractDataFrom;


public class BedrockClient implements RequestHandler<APIGatewayV2HTTPEvent, APIGatewayV2HTTPResponse> {

    private final static String MODEL = "anthropic.claude-v2";
    private final BedrockRuntimeClient bedrockClient;

    record Request(String prompt) { }

    public BedrockClient() {
        bedrockClient = BedrockRuntimeClient.builder().build();
    }

    public APIGatewayV2HTTPResponse handleRequest(final APIGatewayV2HTTPEvent event, final Context context) {
        LambdaLogger logger = context.getLogger();
        logger.log("Processing request for: " + event.getBody());

        Request content = extractDataFrom(event).as(Request.class);
        String response = sendRequest(content.prompt);

        logger.log("Response: " + response);
        return APIGatewayV2HTTPResponse.builder()
                .withStatusCode(200)
                .withBody(toJson(response))
                .build();
    }

    private String sendRequest(String prompt) {
        Body body = new Body(prompt);
        InvokeModelRequest request = InvokeModelRequest.builder()
                .modelId(MODEL)
                .body(SdkBytes.fromString(body.toJson(), Charset.defaultCharset()))
                .build();

        InvokeModelResponse invokeModelResponse = bedrockClient.invokeModel(request);

        JSONObject responseAsJson = new JSONObject(invokeModelResponse.body().asUtf8String());
        return String.valueOf(responseAsJson.get("completion"));
    }

    private static String toJson(String response) {
        return new JSONObject().put("response", response).toString();
    }
}