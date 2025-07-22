package resizer;

import com.amazonaws.services.lambda.runtime.events.S3Event;
import com.amazonaws.services.lambda.runtime.tests.annotations.Event;
import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.params.ParameterizedTest;
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.s3.S3Client;
import software.amazon.awssdk.services.s3.model.ListObjectsRequest;
import software.amazon.awssdk.services.s3.model.ListObjectsResponse;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertNotNull;

@Disabled("Disabled until source and destination buckets are set up")
public class AppTest {
  private static final S3Client s3Client = S3Client.builder()
    .region(Region.of(System.getenv("AWS_REGION")))
    .build();

  private static final String DESTINATION_BUCKET_NAME = System.getenv("DESTINATION_BUCKET_NAME");

  @AfterEach
  public void cleanup() {
    ListObjectsRequest listObjectRequest = ListObjectsRequest.builder()
      .bucket(DESTINATION_BUCKET_NAME)
      .build();
    ListObjectsResponse listObjectResponse = s3Client.listObjects(listObjectRequest);

    if (listObjectResponse.contents() != null) {
      listObjectResponse.contents().forEach(content ->
        s3Client.deleteObject(builder -> builder.bucket(DESTINATION_BUCKET_NAME).key(content.key()))
      );
    }
  }

  @ParameterizedTest
  @Event(value = "events/s3_event.json", type = S3Event.class)
  public void successfulResponse(S3Event input) {
    App app = new App();
    String response = app.handleRequest(input, null);
    String sourceKey = input.getRecords().getFirst().getS3().getObject().getKey();

    assertNotNull(input.getRecords().getFirst().getS3().getBucket().getName());
    assertNotNull(sourceKey);

    assertEquals("Ok", response);

    ListObjectsRequest listObjectRequest = ListObjectsRequest.builder()
      .bucket(System.getenv("DESTINATION_BUCKET_NAME"))
      .build();
    ListObjectsResponse listObjectResponse = s3Client.listObjects(listObjectRequest);

    assertNotNull(listObjectResponse);
    assertNotNull(listObjectResponse.contents());
    assertEquals(1, listObjectResponse.contents().size());
  }
}
