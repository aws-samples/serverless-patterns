package resizer;

import com.amazonaws.services.lambda.runtime.Context;
import com.amazonaws.services.lambda.runtime.RequestHandler;
import com.amazonaws.services.lambda.runtime.events.S3Event;
import com.amazonaws.services.lambda.runtime.events.models.s3.S3EventNotification.S3EventNotificationRecord;
import software.amazon.awssdk.core.ResponseBytes;
import software.amazon.awssdk.core.sync.RequestBody;
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.s3.S3Client;
import software.amazon.awssdk.services.s3.model.GetObjectRequest;
import software.amazon.awssdk.services.s3.model.GetObjectResponse;
import software.amazon.awssdk.services.s3.model.PutObjectRequest;

import javax.imageio.ImageIO;
import java.awt.*;
import java.awt.image.BufferedImage;
import java.io.ByteArrayOutputStream;

public class App implements RequestHandler<S3Event, String> {
  private static final S3Client s3Client = S3Client.builder()
    .region(Region.of(System.getenv("AWS_REGION")))
    .build();
  private static final String DESTINATION_BUCKET = System.getenv("DESTINATION_BUCKET_NAME");

  public String handleRequest(final S3Event s3event, final Context context) {
    try {
      S3EventNotificationRecord record = s3event.getRecords().getFirst();
      String sourceBucket = record.getS3().getBucket().getName();
      String sourceKey = record.getS3().getObject().getUrlDecodedKey();

      // Get the image from S3 bucket
      GetObjectRequest getObjectRequest = GetObjectRequest.builder()
        .bucket(sourceBucket)
        .key(sourceKey)
        .build();
      ResponseBytes<GetObjectResponse> getObjectResponseBytes = s3Client.getObjectAsBytes(getObjectRequest);
      BufferedImage originalImage = ImageIO.read(getObjectResponseBytes.asInputStream());

      // Resize the image
      int newWidth = 800;
      int newHeight = 600;
      Image resizedImage = originalImage.getScaledInstance(newWidth, newHeight, Image.SCALE_SMOOTH);

      // Convert the resized image to a BufferedImage
      BufferedImage outputImage = new BufferedImage(newWidth, newHeight, BufferedImage.TYPE_INT_RGB);
      outputImage.getGraphics().drawImage(resizedImage, 0, 0, null);

      // Upload the resized image to the destination bucket
      ByteArrayOutputStream outputStream = new ByteArrayOutputStream();
      ImageIO.write(outputImage, "jpg", outputStream);
      PutObjectRequest putObjectRequest = PutObjectRequest.builder()
        .bucket(DESTINATION_BUCKET)
        .key("resized_%s".formatted(sourceKey))
        .build();
      s3Client.putObject(putObjectRequest, RequestBody.fromBytes(outputStream.toByteArray()));

      return "Ok";
    } catch (Exception e) {
      throw new RuntimeException(e);
    }
  }
}
