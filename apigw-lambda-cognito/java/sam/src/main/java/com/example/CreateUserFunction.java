package com.example;

import java.io.StringReader;
import java.util.HashMap;
import java.util.Map;

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

public class CreateUserFunction implements RequestHandler<APIGatewayProxyRequestEvent, APIGatewayProxyResponseEvent> {

    private final UserService userService;
    private final String appClientId;
    private final String appClientSecret;
    private static final Gson GSON = new GsonBuilder().serializeNulls().create();

    public CreateUserFunction(UserService cognitoUserService,
                              String appClientId,
                              String appClientSecret) {
        this.userService = cognitoUserService;
        this.appClientId = appClientId;
        this.appClientSecret = appClientSecret;
    }

    public CreateUserFunction() {
        this.userService = new UserService(System.getenv("AWS_REGION"));
        this.appClientId = System.getenv("MY_COGNITO_POOL_APP_CLIENT_ID");
        this.appClientSecret = System.getenv("MY_COGNITO_POOL_APP_CLIENT_SECRET");
    }

    public APIGatewayProxyResponseEvent handleRequest(final APIGatewayProxyRequestEvent input,
                                                       final Context context) {
        Map<String, String> headers = new HashMap<>();
        headers.put("Content-Type", "application/json");

        APIGatewayProxyResponseEvent response = new APIGatewayProxyResponseEvent()
                .withHeaders(headers);

        String requestBody = input.getBody();
        LambdaLogger logger = context.getLogger();
        logger.log("Original json body: " + requestBody);

        JsonObject userDetails;
        try (JsonReader reader = new JsonReader(new StringReader(requestBody))) {
            userDetails = JsonParser.parseReader(reader).getAsJsonObject();
            JsonObject createUserResult = userService.createUser(userDetails, appClientId, appClientSecret);
            response.withStatusCode(200);
            response.withBody(GSON.toJson(createUserResult, JsonObject.class));
        } catch (AwsServiceException ex) {
            logAndHandleException(logger, response, ex.awsErrorDetails().errorMessage(), ex.awsErrorDetails().sdkHttpResponse().statusCode());
        } catch (Exception ex) {
            logAndHandleException(logger, response, ex.getMessage(), 500);
        }

        return response;
    }

    private void logAndHandleException(LambdaLogger logger, APIGatewayProxyResponseEvent response, String errorMessage, int statusCode) {
        logger.log(errorMessage);
        ErrorResponse errorResponse = new ErrorResponse(errorMessage);
        response.withBody(GSON.toJson(errorResponse, ErrorResponse.class));
        response.withStatusCode(statusCode);
    }
}