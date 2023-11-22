package com.unicorn.store;

import com.fasterxml.jackson.databind.ObjectMapper;
import com.unicorn.store.model.Unicorn;
import org.json.JSONException;
import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import org.skyscreamer.jsonassert.JSONAssert;
import org.skyscreamer.jsonassert.JSONCompareMode;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.TestConfiguration;
import org.springframework.boot.test.web.server.LocalServerPort;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Primary;
import org.springframework.http.HttpHeaders;
import org.springframework.http.MediaType;
import org.testcontainers.containers.GenericContainer;
import org.testcontainers.junit.jupiter.Container;
import org.testcontainers.junit.jupiter.Testcontainers;
import org.testcontainers.utility.DockerImageName;
import software.amazon.awssdk.auth.credentials.AwsBasicCredentials;
import software.amazon.awssdk.auth.credentials.StaticCredentialsProvider;
import software.amazon.awssdk.enhanced.dynamodb.DynamoDbAsyncTable;
import software.amazon.awssdk.enhanced.dynamodb.DynamoDbEnhancedAsyncClient;
import software.amazon.awssdk.enhanced.dynamodb.Key;
import software.amazon.awssdk.enhanced.dynamodb.TableSchema;
import software.amazon.awssdk.http.crt.AwsCrtAsyncHttpClient;
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.dynamodb.DynamoDbAsyncClient;

import java.io.IOException;
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertNotNull;
import static org.junit.jupiter.api.Assertions.assertNull;

@Testcontainers
@SpringBootTest(
        webEnvironment = SpringBootTest.WebEnvironment.RANDOM_PORT,
        properties = {"spring.main.allow-bean-definition-overriding=true"}
)
@DisplayName("LambdaApplication Integration Test")
class StoreApplicationTest {

    @Container
    public static final GenericContainer DYNAMODB_CONTAINER = new GenericContainer(DockerImageName.parse("amazon/dynamodb-local:2.0.0"))
            .withExposedPorts(8000);
    private final HttpClient httpClient = HttpClient.newHttpClient();

    @Autowired
    private DynamoDbAsyncTable<Unicorn> dynamoDbAsyncTable;

    @LocalServerPort
    private Integer serverPort;

    private String serverUrl;

    @BeforeEach
    void setup() {
        serverUrl = String.format("http://localhost:%d", serverPort);
        dynamoDbAsyncTable.createTable().join();
        Unicorn unicorn = new Unicorn();
        unicorn.setId("123");
        unicorn.setName("Something");
        unicorn.setAge("Older");
        unicorn.setSize("Very big");
        unicorn.setType("Animal");
        dynamoDbAsyncTable.putItem(unicorn).join();
    }

    @AfterEach
    void teardown() {
        dynamoDbAsyncTable.deleteTable().join();
    }

    @Test
    @DisplayName("GET /unicorns/{unicornId} - 200 Success")
    void testRetrieveUnicornSuccess() throws IOException, InterruptedException, JSONException {
        HttpRequest request = HttpRequest.newBuilder()
                .GET()
                .uri(URI.create(serverUrl.concat("/unicorns/123")))
                .build();
        HttpResponse<String> response = httpClient.send(request, HttpResponse.BodyHandlers.ofString());
        assertEquals(200, response.statusCode());
        JSONAssert.assertEquals("""
                {
                  "id": "123",
                  "name": "Something",
                  "age": "Older",
                  "size": "Very big",
                  "type": "Animal"
                }
                """, response.body(), JSONCompareMode.STRICT);
    }

    @Test
    @DisplayName("GET /unicorns/{unicornId} - 404 Not Found")
    void testRetrieveUnicornNotFound() throws JSONException, IOException, InterruptedException {
        HttpRequest request = HttpRequest.newBuilder()
                .GET()
                .uri(URI.create(serverUrl.concat("/unicorns/999")))
                .build();
        HttpResponse<String> response = httpClient.send(request, HttpResponse.BodyHandlers.ofString());
        assertEquals(404, response.statusCode());
        JSONAssert.assertEquals("""
                {
                   "message": "Unicorn was not found in DynamoDB.",
                   "errors": [
                     "Requested Unicorn was not found."
                   ]
                }
                """, response.body(), JSONCompareMode.STRICT);
    }

    @Test
    @DisplayName("POST /unicorns/ - 201 Created")
    void testCreateUnicornCreated() throws IOException, InterruptedException, JSONException {
        HttpRequest request = HttpRequest.newBuilder()
                .POST(HttpRequest.BodyPublishers.ofString("""
                        {
                            "name": "Test Name",
                            "age": "Test Age",
                            "size": "Test Size",
                            "type": "Test Type"
                        }
                        """))
                .header(HttpHeaders.CONTENT_TYPE, MediaType.APPLICATION_JSON_VALUE)
                .uri(URI.create(serverUrl.concat("/unicorns")))
                .build();
        HttpResponse<String> response = httpClient.send(request, HttpResponse.BodyHandlers.ofString());
        assertEquals(201, response.statusCode());
        Unicorn savedUnicorn = new ObjectMapper().readValue(response.body(), Unicorn.class);
        JSONAssert.assertEquals(String.format("""
                {
                    "id": "%s",
                    "name": "Test Name",
                    "age": "Test Age",
                    "size": "Test Size",
                    "type": "Test Type"
                }
                """, savedUnicorn.getId()), response.body(), JSONCompareMode.STRICT);
        assertNotNull(dynamoDbAsyncTable.getItem(Key.builder().partitionValue(savedUnicorn.getId()).build()));
    }

    @Test
    @DisplayName("PUT /unicorns/{unicornId} - 200 Success")
    void testPutUnicornSuccess() throws IOException, InterruptedException, JSONException {
        HttpRequest request = HttpRequest.newBuilder()
                .PUT(HttpRequest.BodyPublishers.ofString("""
                        {
                            "name": "Test Name",
                            "age": "Test Age",
                            "size": "Test Size",
                            "type": "Test Type"
                        }
                        """))
                .header(HttpHeaders.CONTENT_TYPE, MediaType.APPLICATION_JSON_VALUE)
                .uri(URI.create(serverUrl.concat("/unicorns/123")))
                .build();
        HttpResponse<String> response = httpClient.send(request, HttpResponse.BodyHandlers.ofString());
        assertEquals(200, response.statusCode());
        JSONAssert.assertEquals("""
                {
                  "id": "123",
                  "name": "Test Name",
                  "age": "Test Age",
                  "size": "Test Size",
                  "type": "Test Type"
                }
                """, response.body(), JSONCompareMode.STRICT);
        Unicorn updatedUnicorn = dynamoDbAsyncTable.getItem(Key.builder().partitionValue("123").build()).join();
        assertNotNull(updatedUnicorn);
        assertEquals("Test Name", updatedUnicorn.getName());
        assertEquals("Test Age", updatedUnicorn.getAge());
        assertEquals("Test Size", updatedUnicorn.getSize());
        assertEquals("Test Type", updatedUnicorn.getType());
    }

    @Test
    @DisplayName("PUT /unicorns/{unicornId} - 404 Not Found")
    void testPutUnicornNotFound() throws IOException, InterruptedException {
        HttpRequest request = HttpRequest.newBuilder()
                .PUT(HttpRequest.BodyPublishers.ofString("""
                        {
                            "name": "Test Name",
                            "age": "Test Age",
                            "size": "Test Size",
                            "type": "Test Type"
                        }
                        """))
                .header(HttpHeaders.CONTENT_TYPE, MediaType.APPLICATION_JSON_VALUE)
                .uri(URI.create(serverUrl.concat("/unicorns/999")))
                .build();
        HttpResponse<String> response = httpClient.send(request, HttpResponse.BodyHandlers.ofString());
        assertEquals(404, response.statusCode());
        Unicorn updatedUnicorn = dynamoDbAsyncTable.getItem(Key.builder().partitionValue("123").build()).join();
        assertNotNull(updatedUnicorn);
        assertEquals("Something", updatedUnicorn.getName());
        assertEquals("Older", updatedUnicorn.getAge());
        assertEquals("Very big", updatedUnicorn.getSize());
        assertEquals("Animal", updatedUnicorn.getType());
    }

    @Test
    @DisplayName("DELETE /unicorns/{unicornId} - 200 Success")
    void testDeleteUnicornSuccess() throws IOException, InterruptedException {
        assertNotNull(dynamoDbAsyncTable.getItem(Key.builder().partitionValue("123").build()).join());
        HttpRequest request = HttpRequest.newBuilder()
                .DELETE()
                .uri(URI.create(serverUrl.concat("/unicorns/123")))
                .build();
        HttpResponse<String> response = httpClient.send(request, HttpResponse.BodyHandlers.ofString());
        assertEquals(200, response.statusCode());
        assertNull(dynamoDbAsyncTable.getItem(Key.builder().partitionValue("123").build()).join());
    }

    @TestConfiguration
    static class StoreApplicationTestConfig {

        @Bean
        @Primary
        public DynamoDbAsyncClient dynamoDbAsyncClient() {
            return DynamoDbAsyncClient.builder()
                    .region(Region.EU_WEST_1)
                    .endpointOverride(URI.create(String.format("http://%s:%d", DYNAMODB_CONTAINER.getHost(), DYNAMODB_CONTAINER.getFirstMappedPort())))
                    .httpClient(AwsCrtAsyncHttpClient.create())
                    .credentialsProvider(StaticCredentialsProvider.create(AwsBasicCredentials.create("fakeMyKeyId", "fakeSecretAccessKey")))
                    .build();
        }

        @Bean
        @Primary
        public DynamoDbAsyncTable<Unicorn> unicornDynamoDbAsyncTable(DynamoDbEnhancedAsyncClient dynamoDbEnhancedClient) {
            return dynamoDbEnhancedClient.table("Unicorn-Local", TableSchema.fromClass(Unicorn.class));
        }
    }

}