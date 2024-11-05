package com.example.flashcards;

import com.amazonaws.services.lambda.runtime.events.APIGatewayV2HTTPEvent;
import com.example.flashcards.model.dto.FindCategoriesResponse;
import com.example.flashcards.model.dto.FindFlashcardsResponse;
import com.example.flashcards.model.entities.Category;
import lombok.extern.slf4j.Slf4j;
import org.h2.jdbcx.JdbcDataSource;
import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.Test;
import software.amazon.awssdk.http.HttpStatusCode;

import javax.sql.DataSource;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.sql.SQLException;
import java.util.List;
import java.util.Map;
import java.util.Optional;

import static com.example.flashcards.FlashcardsLambdaApplicationUtils.readValue;

@Slf4j
class FlashcardsLambdaApplicationTest {

    private static FlashcardsLambdaApplication flashcardsLambdaApplication;

    @BeforeAll
    public static void setUp() throws IOException, SQLException {
        var datasource = createTestDatasource();
        flashcardsLambdaApplication = Optional.of(datasource)
                .map(FlashcardsLambdaApplicationInitializer::new)
                .map(FlashcardsLambdaApplication::new)
                .orElseThrow(() -> new RuntimeException("Can't initialise test environment."));
        initDatabase(datasource);
    }

    private static DataSource createTestDatasource() {
        var dataSource = new JdbcDataSource();
        dataSource.setURL("jdbc:h2:mem:test;MODE=PostgreSQL;DB_CLOSE_DELAY=-1");
        dataSource.setUser("sa");
        dataSource.setPassword("sa");
        return dataSource;
    }

    private static void initDatabase(DataSource dataSource) throws IOException, SQLException {
        var sql = new String(Files.readAllBytes(Paths.get("src/test/resources/data.sql")));
        try (
                var connection = dataSource.getConnection();
                var statement = connection.createStatement()
        ) {
            statement.execute(sql);
        }
        log.info("The H2 db has been successfully initialised for testing.");
    }

    @Test
    void testHandleRequestForFindCategories() {
        var apiGatewayV2HTTPEvent = APIGatewayV2HTTPEvent.builder()
                .withRawPath("/categories")
                .build();
        var apiGatewayV2HTTPResponse = flashcardsLambdaApplication.handleRequest(apiGatewayV2HTTPEvent, null);
        var actualStatusCode = apiGatewayV2HTTPResponse.getStatusCode();
        var expectedStatusCode = HttpStatusCode.OK;
        Assertions.assertEquals(expectedStatusCode, actualStatusCode);
        var actualResponse = readValue(apiGatewayV2HTTPResponse.getBody(), FindCategoriesResponse.class);
        var expectedResponse = FindCategoriesResponse.builder()
                .withCategories(
                        List.of(
                                Category.builder()
                                        .withId(1L)
                                        .withName("Geography")
                                        .build(),
                                Category.builder()
                                        .withId(2L)
                                        .withName("Science")
                                        .build()
                        )
                )
                .build();
        Assertions.assertEquals(expectedResponse, actualResponse);
    }

    @Test
    void testHandleRequestForFindFlashcards() {
        var apiGatewayV2HTTPEvent = APIGatewayV2HTTPEvent.builder()
                .withRawPath("/flashcards")
                .withQueryStringParameters(Map.of(
                        "categoryId", "1",
                        "maxItems", "2"
                ))
                .build();
        var apiGatewayV2HTTPResponse = flashcardsLambdaApplication.handleRequest(apiGatewayV2HTTPEvent, null);
        var actualStatusCode = apiGatewayV2HTTPResponse.getStatusCode();
        var expectedStatusCode = HttpStatusCode.OK;
        Assertions.assertEquals(expectedStatusCode, actualStatusCode);
        var response = readValue(apiGatewayV2HTTPResponse.getBody(), FindFlashcardsResponse.class);
        var actualFlashcardsInResponseCount = response.flashcards().size();
        var expectedFlashcardsInResponseCount = 2;
        Assertions.assertEquals(expectedFlashcardsInResponseCount, actualFlashcardsInResponseCount);
    }

    @Test
    void testHandleRequestForFindFlashcardsWithMissingQueryParameters() {
        var apiGatewayV2HTTPEvent = APIGatewayV2HTTPEvent.builder()
                .withRawPath("/flashcards")
                .build();
        var apiGatewayV2HTTPResponse = flashcardsLambdaApplication.handleRequest(apiGatewayV2HTTPEvent, null);
        var actualStatusCode = apiGatewayV2HTTPResponse.getStatusCode();
        var expectedStatusCode = HttpStatusCode.BAD_REQUEST;
        Assertions.assertEquals(expectedStatusCode, actualStatusCode);
        var actualResponse = readValue(apiGatewayV2HTTPResponse.getBody(), String.class);
        var expectedResponse = "Bad request.";
        Assertions.assertEquals(expectedResponse, actualResponse);
    }

    @Test
    void testHandleRequestWithRootPath() {
        var apiGatewayV2HTTPEvent = APIGatewayV2HTTPEvent.builder()
                .withRawPath("/")
                .build();
        var apiGatewayV2HTTPResponse = flashcardsLambdaApplication.handleRequest(apiGatewayV2HTTPEvent, null);
        var actualStatusCode = apiGatewayV2HTTPResponse.getStatusCode();
        var expectedStatusCode = HttpStatusCode.NOT_FOUND;
        Assertions.assertEquals(expectedStatusCode, actualStatusCode);
        var actualResponse = readValue(apiGatewayV2HTTPResponse.getBody(), String.class);
        var expectedResponse = "Not found.";
        Assertions.assertEquals(expectedResponse, actualResponse);
    }

    @Test
    void testHandleRequestWithBadPath() {
        var apiGatewayV2HTTPEvent = APIGatewayV2HTTPEvent.builder()
                .withRawPath("/some/path")
                .build();
        var apiGatewayV2HTTPResponse = flashcardsLambdaApplication.handleRequest(apiGatewayV2HTTPEvent, null);
        var actualStatusCode = apiGatewayV2HTTPResponse.getStatusCode();
        var expectedStatusCode = HttpStatusCode.NOT_FOUND;
        Assertions.assertEquals(expectedStatusCode, actualStatusCode);
        var actualResponse = readValue(apiGatewayV2HTTPResponse.getBody(), String.class);
        var expectedResponse = "Not found.";
        Assertions.assertEquals(expectedResponse, actualResponse);
    }

}