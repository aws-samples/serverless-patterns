package com.example;

import java.io.StringReader;

import com.amazonaws.services.lambda.runtime.Context;
import com.amazonaws.services.lambda.runtime.LambdaLogger;
import com.amazonaws.services.lambda.runtime.RequestHandler;
import com.amazonaws.services.lambda.runtime.events.APIGatewayProxyRequestEvent;
import com.amazonaws.services.lambda.runtime.events.APIGatewayProxyResponseEvent;
import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import com.google.gson.JsonObject;
import com.google.gson.JsonParser;
import com.google.gson.stream.JsonReader;

import software.amazon.awssdk.awscore.exception.AwsServiceException;

public class ConfirmUserFunction implements RequestHandler<APIGatewayProxyRequestEvent, APIGatewayProxyResponseEvent> {

    private final UserService userService;
    private final String appClientId;
    private final String appClientSecret;
    private static final Gson GSON = new GsonBuilder().serializeNulls().create();

    public ConfirmUserFunction() {
        this.userService = new UserService(System.getenv("AWS_REGION"));
        this.appClientId = System.getenv("MY_COGNITO_POOL_APP_CLIENT_ID");
        this.appClientSecret = System.getenv("MY_COGNITO_POOL_APP_CLIENT_SECRET");
    }

    @Override
    public APIGatewayProxyResponseEvent handleRequest(APIGatewayProxyRequestEvent input, Context context) {
        LambdaLogger logger = context.getLogger();

        JsonObject requestBody;
        try (JsonReader reader = new JsonReader(new StringReader(input.getBody()))) {
            requestBody = JsonParser.parseReader(reader).getAsJsonObject();
            String email = requestBody.get("email").getAsString();
            String confirmationCode = requestBody.get("code").getAsString();

            JsonObject confirmUserResult = userService.confirmUser(appClientId, appClientSecret, email, confirmationCode);
            return new APIGatewayProxyResponseEvent()
                    .withStatusCode(200)
                    .withBody(GSON.toJson(confirmUserResult, JsonObject.class));
        } catch (AwsServiceException ex) {
            return handleException(logger, ex.awsErrorDetails().errorMessage(), ex.awsErrorDetails().sdkHttpResponse().statusCode());
        } catch (Exception ex) {
            return handleException(logger, ex.getMessage(), 500);
        }
    }

    private APIGatewayProxyResponseEvent handleException(LambdaLogger logger, String errorMessage, int statusCode) {
        logger.log(errorMessage);
        ErrorResponse errorResponse = new ErrorResponse(errorMessage);
        return new APIGatewayProxyResponseEvent()
                .withBody(GSON.toJson(errorResponse, ErrorResponse.class))
                .withStatusCode(statusCode);
    }
}