package com.example;

import com.amazonaws.services.lambda.runtime.Context;
import com.amazonaws.services.lambda.runtime.LambdaLogger;
import com.amazonaws.services.lambda.runtime.RequestHandler;
import com.amazonaws.services.lambda.runtime.events.APIGatewayV2HTTPEvent;
import com.amazonaws.services.lambda.runtime.events.APIGatewayV2HTTPResponse;
import org.json.JSONObject;
import software.amazon.awssdk.services.bedrockruntime.BedrockRuntimeClient;
import software.amazon.awssdk.services.bedrockruntime.model.ContentBlock;
import software.amazon.awssdk.services.bedrockruntime.model.ConversationRole;
import software.amazon.awssdk.services.bedrockruntime.model.ConverseResponse;
import software.amazon.awssdk.services.bedrockruntime.model.Message;

import java.util.Objects;
import java.util.stream.Collectors;

import static software.amazon.lambda.powertools.utilities.EventDeserializer.extractDataFrom;


public class BedrockClient implements RequestHandler<APIGatewayV2HTTPEvent, APIGatewayV2HTTPResponse> {

    // Inference profile ID, set by the stack (global.anthropic.claude-haiku-5-5)
    private static final String MODEL_ID = System.getenv("MODEL_ID");
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
        Message message = Message.builder()
                .role(ConversationRole.USER)
                .content(ContentBlock.fromText(prompt))
                .build();

        // The Converse API uses the same request shape for every model that supports it.
        // maxTokens covers the model's thinking and its answer.
        ConverseResponse response = bedrockClient.converse(request -> request
                .modelId(MODEL_ID)
                .messages(message)
                .inferenceConfig(config -> config.maxTokens(1024)));

        // Keep the text blocks only; reasoning blocks have no text
        return response.output().message().content().stream()
                .map(ContentBlock::text)
                .filter(Objects::nonNull)
                .collect(Collectors.joining());
    }

    private static String toJson(String response) {
        return new JSONObject().put("response", response).toString();
    }
}
