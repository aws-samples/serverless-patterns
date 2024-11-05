package com.example.flashcards.services;

import com.example.flashcards.FlashcardsLambdaApplicationUtils;
import com.fasterxml.jackson.databind.JsonNode;
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.secretsmanager.SecretsManagerClient;
import software.amazon.awssdk.services.secretsmanager.model.GetSecretValueRequest;
import software.amazon.awssdk.services.secretsmanager.model.GetSecretValueResponse;
import software.amazon.awssdk.utils.StringUtils;

import java.util.NoSuchElementException;
import java.util.Optional;

public class SecretsManagerService {

    public String readPasswordFromSecret(String region, String secretId) {
        if (StringUtils.isNotBlank(region) && StringUtils.isNotBlank(secretId)) {
            try (
                    SecretsManagerClient secretsManagerClient = SecretsManagerClient.builder()
                            .region(Region.of(region))
                            .build()
            ) {
                return Optional.of(GetSecretValueRequest.builder())
                        .map(builder -> builder.secretId(secretId))
                        .map(GetSecretValueRequest.Builder::build)
                        .map(secretsManagerClient::getSecretValue)
                        .map(GetSecretValueResponse::secretString)
                        .map(FlashcardsLambdaApplicationUtils::readTree)
                        .map(jsonNode -> jsonNode.get("password"))
                        .map(JsonNode::asText)
                        .filter(StringUtils::isNotBlank)
                        .orElseThrow(() -> new NoSuchElementException("Can't find database password field in secret."));
            }
        } else {
            throw new IllegalArgumentException("The region and/or secretId are/is blank. Can't find secret.");
        }
    }
}
