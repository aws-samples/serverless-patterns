package com.example;

import com.amazonaws.services.lambda.runtime.Context;
import com.amazonaws.services.lambda.runtime.RequestHandler;
import software.amazon.awssdk.core.ResponseInputStream;
import software.amazon.awssdk.core.sync.RequestBody;
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.s3.S3Client;
import software.amazon.awssdk.services.s3.model.GetObjectRequest;
import software.amazon.awssdk.services.s3.model.GetObjectResponse;
import software.amazon.awssdk.services.s3.model.PutObjectRequest;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.nio.charset.StandardCharsets;
import java.util.stream.Collectors;

public class TextTransformer implements RequestHandler {

    @Override
    public Object handleRequest(Object o, Context context) {

        ResponseInputStream<GetObjectResponse> file = getFileFromS3();

        StringBuilder stringBuilder = transformFile(file);

        uploadFile(stringBuilder);

        return "Done";
    }

    private ResponseInputStream<GetObjectResponse> getFileFromS3() {
        String bucketName = System.getenv("SOURCE_BUCKET");

        Region region = Region.EU_CENTRAL_1;
        S3Client s3 = S3Client.builder()
                .region(region)
                .build();

        GetObjectRequest getObjectRequest = GetObjectRequest.builder()
                .bucket(bucketName)
                .key("input.txt")
                .build();

        ResponseInputStream<GetObjectResponse> file = s3.getObject(getObjectRequest);

        return file;
    }

    private StringBuilder transformFile(ResponseInputStream<GetObjectResponse> file) {
        BufferedReader bufferReader = new BufferedReader(
                new InputStreamReader(file, StandardCharsets.UTF_8));

        StringBuilder stringBuilder = new StringBuilder();

        bufferReader.lines()
                .collect(Collectors.toList())
                .stream()
                .forEach(line -> stringBuilder.append(line.toUpperCase() + "\n"));

        return stringBuilder;
    }

    private void uploadFile(StringBuilder stringBuilder) {
        Region region = Region.EU_CENTRAL_1;
        S3Client s3 = S3Client.builder()
                .region(region)
                .build();

        PutObjectRequest objectRequest = PutObjectRequest.builder()
                .bucket("destinationconfigbckt")
                .key("output.txt")
                .build();

        RequestBody requestBody = RequestBody.fromString(stringBuilder.toString());
        s3.putObject(objectRequest, requestBody);
    }
}
