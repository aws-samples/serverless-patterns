package com.example;

import java.io.File;
import java.io.IOException;
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.nio.file.Files;
import java.util.Scanner;

public class S3UploadIntegrationTest {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter the REST API URL to get the pre-signed URL: ");
        String restApiUrl = scanner.nextLine();

        System.out.print("Enter the file name on S3 (key): ");
        String fileName = scanner.nextLine();

        String presignedUrl = getPresignedUrl(restApiUrl, fileName);
        if (presignedUrl == null) {
            System.out.println("Failed to retrieve pre-signed URL.");
            scanner.close();
            return;
        }

        System.out.print("Enter the path to the local file: ");
        String filePath = scanner.nextLine();

        try {
            File file = new File(filePath);
            byte[] fileData = Files.readAllBytes(file.toPath());

            HttpClient client = HttpClient.newHttpClient();
            HttpRequest request = HttpRequest.newBuilder()
                    .uri(URI.create(presignedUrl))
                    .PUT(HttpRequest.BodyPublishers.ofByteArray(fileData))
                    .build();

            HttpResponse<Void> response = client.send(request, HttpResponse.BodyHandlers.discarding());

            if (response.statusCode() == 200) {
                System.out.println("File uploaded successfully!");
            } else {
                System.out.println("Error uploading file: " + response.statusCode());
            }
        } catch (IOException | InterruptedException e) {
            e.printStackTrace();
        }

        scanner.close();
    }

    private static String getPresignedUrl(String restApiUrl, String fileName) {
        try {
            HttpClient client = HttpClient.newHttpClient();
    
            // Create the JSON request body
            String requestBody = "{\"fileName\":\"" + fileName + "\"}";
    
            HttpRequest request = HttpRequest.newBuilder()
                    .uri(URI.create(restApiUrl))
                    .POST(HttpRequest.BodyPublishers.ofString(requestBody))
                    .header("Content-Type", "application/json")
                    .build();
    
            HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
    
            if (response.statusCode() == 200) {
                return response.body();
            } else {
                System.out.println("Error retrieving pre-signed URL: " + response.statusCode());
            }
        } catch (IOException | InterruptedException e) {
            e.printStackTrace();
        }
    
        return null;
    }
}