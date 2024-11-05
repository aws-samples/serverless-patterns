package com.example.flashcards;

import com.amazonaws.services.lambda.runtime.Context;
import com.amazonaws.services.lambda.runtime.RequestHandler;
import com.amazonaws.services.lambda.runtime.events.APIGatewayV2HTTPEvent;
import com.amazonaws.services.lambda.runtime.events.APIGatewayV2HTTPResponse;
import com.example.flashcards.model.dto.FindFlashcardsRequest;
import com.example.flashcards.services.CategoryService;
import com.example.flashcards.services.FlashcardService;
import lombok.extern.slf4j.Slf4j;
import software.amazon.awssdk.http.HttpStatusCode;
import software.amazon.awssdk.utils.StringUtils;

import java.sql.SQLException;
import java.util.Optional;

import static com.example.flashcards.FlashcardsLambdaApplicationUtils.writeValue;

@Slf4j
public class FlashcardsLambdaApplication implements RequestHandler<APIGatewayV2HTTPEvent, APIGatewayV2HTTPResponse> {

    private final CategoryService categoryService;
    private final FlashcardService flashcardService;

    // constructor used for testing
    public FlashcardsLambdaApplication(FlashcardsLambdaApplicationInitializer flashcardsLambdaApplicationInitializer) {
        categoryService = flashcardsLambdaApplicationInitializer.getCategoryService();
        flashcardService = flashcardsLambdaApplicationInitializer.getFlashcardService();
    }

    //no args constructor for aws
    public FlashcardsLambdaApplication() {
        var flashcardsLambdaApplicationContext = new FlashcardsLambdaApplicationInitializer();
        categoryService = flashcardsLambdaApplicationContext.getCategoryService();
        flashcardService = flashcardsLambdaApplicationContext.getFlashcardService();
    }

    @Override
    public APIGatewayV2HTTPResponse handleRequest(APIGatewayV2HTTPEvent apiGatewayV2HTTPEvent, Context context) {
        return Optional.ofNullable(apiGatewayV2HTTPEvent)
                .map(APIGatewayV2HTTPEvent::getRawPath)
                .map(String::trim)
                .filter(StringUtils::isNotBlank)
                .filter(path -> !path.equals("/"))
                .map(function -> {
                    switch (function) {
                        case "/categories" -> {
                            return invokeFindCategories();
                        }
                        case "/flashcards" -> {
                            return Optional.of(apiGatewayV2HTTPEvent)
                                    .map(APIGatewayV2HTTPEvent::getQueryStringParameters)
                                    .flatMap(FindFlashcardsRequest::fromQueryStringParameters)
                                    .map(this::invokeFindFlashcards)
                                    .orElseGet(
                                            () -> APIGatewayV2HTTPResponse.builder()
                                                    .withStatusCode(HttpStatusCode.BAD_REQUEST)
                                                    .withBody(writeValue("Bad request."))
                                                    .build()
                                    );
                        }
                        default -> {
                            return APIGatewayV2HTTPResponse.builder()
                                    .withBody(writeValue("Not found."))
                                    .withStatusCode(HttpStatusCode.NOT_FOUND)
                                    .build();
                        }
                    }
                }).orElseGet(
                        () -> APIGatewayV2HTTPResponse.builder()
                                .withBody(writeValue("Not found."))
                                .withStatusCode(HttpStatusCode.NOT_FOUND)
                                .build()
                );
    }

    private APIGatewayV2HTTPResponse invokeFindCategories() {
        try {
            log.info("Started invoking findCategories.");
            var findCategoriesResponse = categoryService.findCategories();
            var response = APIGatewayV2HTTPResponse.builder()
                    .withStatusCode(HttpStatusCode.OK)
                    .withBody(writeValue(findCategoriesResponse))
                    .build();
            log.info("Done invoking findCategories.");
            return response;
        } catch (SQLException e) {
            return APIGatewayV2HTTPResponse.builder()
                    .withStatusCode(HttpStatusCode.INTERNAL_SERVER_ERROR)
                    .withBody(writeValue(e.getMessage()))
                    .build();
        }
    }

    private APIGatewayV2HTTPResponse invokeFindFlashcards(FindFlashcardsRequest request) {
        try {
            log.info("Started invoking findFindFlashcards.");
            var findFlashcardsResponse = flashcardService.findFlashcards(request);
            var response = APIGatewayV2HTTPResponse.builder()
                    .withStatusCode(HttpStatusCode.OK)
                    .withBody(writeValue(findFlashcardsResponse))
                    .build();
            log.info("Done invoking findFindFlashcards.");
            return response;
        } catch (SQLException e) {
            return APIGatewayV2HTTPResponse.builder()
                    .withStatusCode(HttpStatusCode.INTERNAL_SERVER_ERROR)
                    .withBody(writeValue(e.getMessage()))
                    .build();
        }
    }

}
