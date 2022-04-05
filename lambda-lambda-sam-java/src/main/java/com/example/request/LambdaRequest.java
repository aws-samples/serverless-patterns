package com.example.request;

import com.amazonaws.services.lambda.runtime.Context;
import com.amazonaws.services.lambda.runtime.RequestHandler;
import com.example.request.model.Payload;
import com.google.gson.Gson;
import software.amazon.awssdk.core.SdkBytes;
import software.amazon.awssdk.core.SdkSystemSetting;
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.lambda.LambdaClient;
import software.amazon.awssdk.services.lambda.model.InvokeRequest;
import software.amazon.awssdk.services.lambda.model.InvokeResponse;

public class LambdaRequest implements RequestHandler<Payload, String> {

    private final Gson gson = new Gson();
    private final String response = System.getenv("RESPONSE_FUNC_NAME");
    private final LambdaClient awsLambda = LambdaClient.builder()
            .region(Region.of(System.getenv(SdkSystemSetting.AWS_REGION.environmentVariable())))
            .build();

    @Override
    public String handleRequest(Payload payload, Context context) {

        return invokeLambdaResponse(payload.getMessage());
    }

    private String invokeLambdaResponse(String message) {
        SdkBytes payload = SdkBytes.fromUtf8String(gson.toJson(message)) ;
        InvokeRequest request = InvokeRequest.builder()
                .functionName(response)
                .payload(payload)
                .build();

        InvokeResponse response = awsLambda.invoke(request);
        return response.payload().asUtf8String() ;
    }
}
