// Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: MIT-0

package com.example.orders;

import com.example.orders.proto.OrderPlaced;
import software.amazon.awssdk.core.SdkBytes;
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.eventbridgev2.EventBridgeV2Client;
import software.amazon.awssdk.services.eventbridgev2.model.PutRawEventsRequest;
import software.amazon.awssdk.services.eventbridgev2.model.PutRawEventsRequestEntry;
import software.amazon.awssdk.services.eventbridgev2.model.PutRawEventsResponse;
import software.amazon.awssdk.services.eventbridgev2.model.PutRawEventsResultEntry;
import software.amazon.awssdk.services.eventbridgev2.model.PutRawEventsSystemMetadata;
import software.amazon.awssdk.services.eventbridgev2.model.SchemaRegistryConfiguration;
import software.amazon.awssdk.services.glue.GlueClient;
import software.amazon.awssdk.services.glue.model.GetSchemaVersionRequest;
import software.amazon.awssdk.services.glue.model.GetSchemaVersionResponse;
import software.amazon.awssdk.services.glue.model.SchemaId;
import software.amazon.awssdk.services.glue.model.SchemaVersionNumber;

import java.util.ArrayList;
import java.util.List;
import java.util.Map;

/**
 * Publish a rich OrderPlaced domain event to an EventBridge custom event bus
 * (the eventsv2 API) in Protobuf binary format, decoded against an AWS Glue
 * Schema Registry.
 *
 * <p>Usage:
 * <pre>
 *   java -jar publisher.jar \
 *       --bus-arn arn:aws:events:&lt;region&gt;:&lt;account&gt;:event-busv2/proto-orders-bus/&lt;id&gt; \
 *       --registry-arn arn:aws:glue:&lt;region&gt;:&lt;account&gt;:registry/proto-orders-registry \
 *       [--region &lt;region&gt;] [--order-id order-123]
 * </pre>
 *
 * <p>Both ARNs can also be supplied via the BUS_ARN and REGISTRY_ARN environment
 * variables, and the region via AWS_REGION. The IAM action for publishing is
 * {@code events:PutRawEvents} (never {@code eventsv2:}).
 */
public final class Publisher {

    static final String CONTENT_TYPE_PROTOBUF = "application/protobuf";

    private Publisher() {
    }

    /**
     * Build a single PutRawEvents entry from a domain message.
     *
     * <p>{@code Data} is Protobuf bytes wrapped in the Glue Schema Registry wire
     * format (header, schema-version UUID, message index, then the Protobuf
     * bytes). {@code Metadata} carries the custom keys a METADATA-scoped
     * subscriber filter can route on.
     */
    static PutRawEventsRequestEntry buildEntry(OrderPlaced order, String schemaVersionId) {
        byte[] framed = ProtoIo.encodeFramed(order, schemaVersionId);
        return PutRawEventsRequestEntry.builder()
            .data(SdkBytes.fromByteArray(framed))
            .systemMetadata(PutRawEventsSystemMetadata.builder()
                .contentType(CONTENT_TYPE_PROTOBUF)
                .build())
            .metadata(Map.of(
                "eventType", "OrderPlaced",
                "source", "com.example.orders",
                "schemaVersion", "1"))
            .build();
    }

    /** Look up the latest schema-version UUID for OrderPlaced. */
    static String resolveSchemaVersionId(GlueClient glue, String registryArn) {
        String registryName = registryArn.substring(registryArn.lastIndexOf('/') + 1);
        GetSchemaVersionResponse resp = glue.getSchemaVersion(GetSchemaVersionRequest.builder()
            .schemaId(SchemaId.builder()
                .registryName(registryName)
                .schemaName("OrderPlaced")
                .build())
            .schemaVersionNumber(SchemaVersionNumber.builder().latestVersion(true).build())
            .build());
        return resp.schemaVersionId();
    }

    /** Return the indexes of failed per-entry results (an entry with an errorCode). */
    static List<Integer> findFailures(PutRawEventsResponse response) {
        List<Integer> failures = new ArrayList<>();
        List<PutRawEventsResultEntry> entries = response.entries();
        for (int i = 0; i < entries.size(); i++) {
            if (entries.get(i).errorCode() != null) {
                failures.add(i);
            }
        }
        return failures;
    }

    /** Call PutRawEvents, retrying ThrottlingException with backoff + jitter. */
    static PutRawEventsResponse putRawWithBackoff(
            EventBridgeV2Client client, String busArn, String registryArn,
            List<PutRawEventsRequestEntry> entries, int attempts) {
        long delayMs = 200;
        for (int attempt = 0; attempt < attempts; attempt++) {
            try {
                return client.putRawEvents(PutRawEventsRequest.builder()
                    .eventBusArn(busArn)
                    .entries(entries)
                    .schemaRegistryConfiguration(SchemaRegistryConfiguration.builder()
                        .registryUri(registryArn)
                        .build())
                    .build());
            } catch (RuntimeException error) {
                if (!isThrottling(error) || attempt == attempts - 1) {
                    throw error;
                }
                sleep(delayMs + (long) (Math.random() * delayMs));
                delayMs *= 2;
            }
        }
        throw new IllegalStateException("exhausted retry attempts without a response");
    }

    private static boolean isThrottling(RuntimeException error) {
        String name = error.getClass().getSimpleName();
        return name.contains("Throttling")
            || (error.getMessage() != null && error.getMessage().contains("ThrottlingException"));
    }

    private static void sleep(long ms) {
        try {
            Thread.sleep(ms);
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        }
    }

    /** Encode one domain message and publish it to the bus; throw on any failure. */
    static PutRawEventsResponse publish(
            EventBridgeV2Client client, String busArn, String registryArn,
            OrderPlaced order, String schemaVersionId) {
        List<PutRawEventsRequestEntry> entries = List.of(buildEntry(order, schemaVersionId));
        PutRawEventsResponse response = putRawWithBackoff(client, busArn, registryArn, entries, 5);
        Integer failedCount = response.failedEntryCount();
        if (!findFailures(response).isEmpty() || (failedCount != null && failedCount > 0)) {
            throw new RuntimeException("publish had failed entries: " + response.entries());
        }
        return response;
    }

    static final class Args {
        String busArn = System.getenv("BUS_ARN");
        String registryArn = System.getenv("REGISTRY_ARN");
        String region = System.getenv("AWS_REGION");
        String orderId = "order-" + (System.currentTimeMillis() / 1000);
    }

    static Args parseArgs(String[] argv) {
        Args args = new Args();
        for (int i = 0; i < argv.length; i++) {
            switch (argv[i]) {
                case "--bus-arn" -> args.busArn = argv[++i];
                case "--registry-arn" -> args.registryArn = argv[++i];
                case "--region" -> args.region = argv[++i];
                case "--order-id" -> args.orderId = argv[++i];
                default -> { /* ignore unknown args */ }
            }
        }
        return args;
    }

    public static void main(String[] argv) {
        Args args = parseArgs(argv);
        if (args.busArn == null || args.busArn.isBlank()
                || args.registryArn == null || args.registryArn.isBlank()) {
            System.err.println(
                "error: --bus-arn and --registry-arn are required (or set BUS_ARN and REGISTRY_ARN).");
            System.exit(2);
        }

        Region region = (args.region != null && !args.region.isBlank())
            ? Region.of(args.region) : null;

        var ebBuilder = EventBridgeV2Client.builder();
        var glueBuilder = GlueClient.builder();
        if (region != null) {
            ebBuilder.region(region);
            glueBuilder.region(region);
        }

        try (EventBridgeV2Client client = ebBuilder.build();
             GlueClient glue = glueBuilder.build()) {
            String schemaVersionId = resolveSchemaVersionId(glue, args.registryArn);
            OrderPlaced order = ProtoIo.buildOrder(args.orderId);
            PutRawEventsResponse response =
                publish(client, args.busArn, args.registryArn, order, schemaVersionId);
            PutRawEventsResultEntry entry = response.entries().get(0);
            System.out.printf("Published orderId=%s -> SuccessCode=%s EventId=%s%n",
                args.orderId, entry.successCodeAsString(), entry.eventId());
        }
    }
}
