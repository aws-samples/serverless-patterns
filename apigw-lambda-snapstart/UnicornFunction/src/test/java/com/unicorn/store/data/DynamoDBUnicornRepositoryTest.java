package com.unicorn.store.data;

import com.unicorn.store.exceptions.ResourceNotFoundException;
import com.unicorn.store.model.Unicorn;
import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
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

import java.net.URI;
import java.util.Optional;
import java.util.UUID;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertNotNull;
import static org.junit.jupiter.api.Assertions.assertNull;
import static org.junit.jupiter.api.Assertions.assertThrows;
import static org.junit.jupiter.api.Assertions.assertTrue;

@Testcontainers
@DisplayName("DynamoDBUnicornRepository Unit Test")
class DynamoDBUnicornRepositoryTest {

    @Container
    public static final GenericContainer DYNAMODB_CONTAINER = new GenericContainer(DockerImageName.parse("amazon/dynamodb-local:2.0.0"))
            .withExposedPorts(8000);

    private DynamoDBUnicornRepository dynamoDBUnicornRepository;

    @BeforeAll
    static void setupAllTests() {
        unicornAsyncTable().createTable().join();
    }

    private static DynamoDbAsyncTable<Unicorn> unicornAsyncTable() {
        DynamoDbAsyncClient dynamoDbAsyncClient = DynamoDbAsyncClient.builder()
                .region(Region.EU_WEST_1)
                .endpointOverride(URI.create(String.format("http://%s:%d", DYNAMODB_CONTAINER.getHost(), DYNAMODB_CONTAINER.getFirstMappedPort())))
                .httpClient(AwsCrtAsyncHttpClient.create())
                .credentialsProvider(StaticCredentialsProvider.create(AwsBasicCredentials.create("fakeMyKeyId", "fakeSecretAccessKey")))
                .build();
        DynamoDbEnhancedAsyncClient dynamoDbEnhancedAsyncClient = DynamoDbEnhancedAsyncClient.builder()
                .dynamoDbClient(dynamoDbAsyncClient)
                .build();
        return dynamoDbEnhancedAsyncClient.table("Unicorn-Local", TableSchema.fromClass(Unicorn.class));
    }

    @BeforeEach
    void setup() {
        this.dynamoDBUnicornRepository = new DynamoDBUnicornRepository(unicornAsyncTable());
    }

    @Test
    @DisplayName("Unicorn is saved to DynamoDB")
    void testSave() {
        Unicorn unicornToSave = createTestUnicorn();
        assertNull(unicornAsyncTable().getItem(Key.builder().partitionValue(unicornToSave.getId()).build()).join());
        Unicorn savedUnicorn = dynamoDBUnicornRepository.save(unicornToSave);
        assertNotNull(unicornAsyncTable().getItem(Key.builder().partitionValue(unicornToSave.getId()).build()).join());
        assertEquals(unicornToSave.getId(), savedUnicorn.getId());
        assertEquals(unicornToSave.getName(), savedUnicorn.getName());
        assertEquals(unicornToSave.getAge(), savedUnicorn.getAge());
        assertEquals(unicornToSave.getType(), savedUnicorn.getType());
        assertEquals(unicornToSave.getSize(), savedUnicorn.getSize());
    }

    @Test
    @DisplayName("Unicorn is found in DynamoDB")
    void testFindByIdFound() {
        Unicorn existingUnicorn = createTestUnicorn();
        unicornAsyncTable().putItem(existingUnicorn).join();

        Optional<Unicorn> unicornFound = dynamoDBUnicornRepository.findById(existingUnicorn.getId());
        assertTrue(unicornFound.isPresent());
        Unicorn unicornRetrieved = unicornFound.get();
        assertEquals(existingUnicorn.getId(), unicornRetrieved.getId());
        assertEquals(existingUnicorn.getName(), unicornRetrieved.getName());
        assertEquals(existingUnicorn.getAge(), unicornRetrieved.getAge());
        assertEquals(existingUnicorn.getType(), unicornRetrieved.getType());
        assertEquals(existingUnicorn.getSize(), unicornRetrieved.getSize());
    }

    @Test
    @DisplayName("Unicorn is not found in DynamoDB")
    void testFindByIdNotFound() {
        Optional<Unicorn> unicornFound = dynamoDBUnicornRepository.findById("zzz");
        assertTrue(unicornFound.isEmpty());
    }

    @Test
    @DisplayName("Unicorn is not deleted in DynamoDB")
    void testDelete() {
        Unicorn existingUnicorn = createTestUnicorn();
        unicornAsyncTable().putItem(existingUnicorn).join();

        assertNotNull(unicornAsyncTable().getItem(Key.builder().partitionValue(existingUnicorn.getId()).build()).join());
        dynamoDBUnicornRepository.deleteById(existingUnicorn.getId());
        assertNull(unicornAsyncTable().getItem(Key.builder().partitionValue(existingUnicorn.getId()).build()).join());
    }

    @Test
    @DisplayName("Unicorn is updated if found in DynamoDB")
    void testUpdateFound() {
        Unicorn existingUnicorn = createTestUnicorn();
        unicornAsyncTable().putItem(existingUnicorn).join();

        Unicorn fromDynamoBeforeUpdate = unicornAsyncTable().getItem(Key.builder().partitionValue(existingUnicorn.getId()).build()).join();
        assertEquals("Something", fromDynamoBeforeUpdate.getName());

        existingUnicorn.setName("Changed Name");
        dynamoDBUnicornRepository.update(existingUnicorn);

        Unicorn fromDynamoAfterUpdate = unicornAsyncTable().getItem(Key.builder().partitionValue(existingUnicorn.getId()).build()).join();
        assertEquals("Changed Name", fromDynamoAfterUpdate.getName());
    }

    @Test
    @DisplayName("ResourceNotFoundException if Unicorn not found in DynamoDB during Update")
    void testUpdateNotFound() {
        Unicorn unicorn = createTestUnicorn();
        assertNull(unicornAsyncTable().getItem(Key.builder().partitionValue(unicorn.getId()).build()).join());
        assertThrows(ResourceNotFoundException.class, () -> dynamoDBUnicornRepository.update(unicorn));
    }

    private Unicorn createTestUnicorn() {
        Unicorn unicorn = new Unicorn();
        unicorn.setId(UUID.randomUUID().toString());
        unicorn.setName("Something");
        unicorn.setAge("Older");
        unicorn.setSize("Very big");
        unicorn.setType("Animal");
        return unicorn;
    }

}