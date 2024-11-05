package com.example.flashcards.model.dto;

import lombok.Builder;

import java.util.Map;
import java.util.Optional;

@Builder(setterPrefix = "with", builderClassName = "FindFlashcardsRequestBuilder")
public record FindFlashcardsRequest(Long categoryId, Integer maxItems) {

    public static Optional<FindFlashcardsRequest> fromQueryStringParameters(Map<String, String> queryParameters) {
        return Optional.of(FindFlashcardsRequest.builder())
                .flatMap(
                        builder -> Optional.ofNullable(queryParameters)
                                .map(parameters -> parameters.get("categoryId"))
                                .map(Long::valueOf)
                                .map(builder::withCategoryId)
                )
                .flatMap(
                        builder -> Optional.of(queryParameters)
                                .map(parameters -> parameters.get("maxItems"))
                                .map(Integer::valueOf)
                                .map(builder::withMaxItems)
                )
                .map(FindFlashcardsRequest.FindFlashcardsRequestBuilder::build);
    }

}
