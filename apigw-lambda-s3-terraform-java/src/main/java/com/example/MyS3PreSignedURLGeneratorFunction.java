package com.example;

import static software.amazon.lambda.powertools.utilities.EventDeserializer.extractDataFrom;

import com.amazonaws.services.lambda.runtime.Context;
import com.amazonaws.services.lambda.runtime.LambdaLogger;
import com.amazonaws.services.lambda.runtime.RequestHandler;
import com.amazonaws.services.lambda.runtime.events.APIGatewayV2HTTPEvent;
import com.amazonaws.services.lambda.runtime.events.APIGatewayV2HTTPResponse;

import com.amazonaws.services.s3.AmazonS3;
import com.amazonaws.services.s3.AmazonS3ClientBuilder;
import com.amazonaws.HttpMethod;
import com.amazonaws.services.s3.model.GeneratePresignedUrlRequest;

import java.net.URL;
import java.util.Date;

public class MyS3PreSignedURLGeneratorFunction implements RequestHandler<APIGatewayV2HTTPEvent, APIGatewayV2HTTPResponse> {

    private final AmazonS3 s3Client;
    private final String bucketName; 

    record Request(String fileName) { }

    public MyS3PreSignedURLGeneratorFunction() {
        s3Client = AmazonS3ClientBuilder.defaultClient();
        bucketName = System.getenv("BUCKET_NAME");
    }

    public APIGatewayV2HTTPResponse handleRequest(final APIGatewayV2HTTPEvent event, final Context context) {
        LambdaLogger logger = context.getLogger();
        logger.log("Processing request for: " + event.getBody());

        Request content = extractDataFrom(event).as(Request.class);

        Date expiration = new Date();
        // Set expiration to 60 minutes from now
        expiration.setTime(expiration.getTime() + (60 * 60 * 1000));

        // Generate a pre-signed URL for uploading an object to the specified folder
        GeneratePresignedUrlRequest request = new GeneratePresignedUrlRequest(bucketName, content.fileName)
                .withMethod(HttpMethod.PUT)
                .withExpiration(expiration);

        URL presignedUrl = s3Client.generatePresignedUrl(request);

        return APIGatewayV2HTTPResponse.builder()
                .withStatusCode(200)
                .withBody(presignedUrl.toString())
                .build();
    }

}