// Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: MIT-0

package com.example.orders;

import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;
import software.amazon.awssdk.services.eventbridgev2.EventBridgeV2Client;
import software.amazon.awssdk.services.eventbridgev2.model.PutEventsRequest;
import software.amazon.awssdk.services.eventbridgev2.model.PutEventsRequestEntry;
import software.amazon.awssdk.services.eventbridgev2.model.PutEventsResponse;
import software.amazon.awssdk.services.eventbridgev2.model.PutEventsResultEntry;
import software.amazon.awssdk.services.eventbridgev2.model.PutEventsSystemMetadata;

import java.util.ArrayList;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;

/**
 * Publish an ordered sequence of OrderPlaced events to an EventBridge custom
 * event bus (the eventsv2 API) with PutEvents. Every event in a run shares one
 * SystemMetadata.EventGroupId, so the FIFO subscriber orders them relative to
 * one another and — invoking the consumer synchronously — processes them one at
 * a time, in sequence.
 *
 * <p>Usage:
 * <pre>
 *   java -jar publisher.jar \
 *       --bus-arn arn:aws:events:&lt;region&gt;:&lt;account&gt;:event-busv2/sync-orders-bus/&lt;id&gt; \
 *       [--region &lt;region&gt;] [--count 5] [--group order-group-&lt;ts&gt;]
 * </pre>
 *
 * <p>The bus ARN can also come from the BUS_ARN environment variable, and the
 * region from AWS_REGION. The IAM action needed is {@code events:PutEvents} on
 * the bus (the action namespace is {@code events:}, never {@code eventsv2:}).
 */
public final class Publisher {

    static final String SOURCE = "com.example.orders";
    static final String DETAIL_TYPE = "OrderPlaced";

    private static final ObjectMapper MAPPER = new ObjectMapper();

    private Publisher() {
    }

    /** Construct one OrderPlaced record in a group with a sequence number. */
    static Map<String, Object> buildOrder(String group, int seq) {
        Map<String, Object> order = new LinkedHashMap<>();
        order.put("orderId", String.format("%s-%03d", group, seq));
        order.put("orderGroup", group);
        order.put("seq", seq);
        order.put("customerId", "cust-987");
        order.put("amount", 100.0 + seq);
        order.put("currency", "USD");
        order.put("placedAt", "2026-09-21T12:00:00Z");
        return order;
    }

    /**
     * Build a PutEvents entry, grouping the event for FIFO ordering.
     *
     * <p>SystemMetadata.EventGroupId is what the FIFO subscriber orders within.
     */
    static PutEventsRequestEntry buildEntry(Map<String, Object> order, String group) {
        return PutEventsRequestEntry.builder()
            .source(SOURCE)
            .detailType(DETAIL_TYPE)
            .detail(toJson(order))
            .systemMetadata(PutEventsSystemMetadata.builder().eventGroupId(group).build())
            .build();
    }

    static String toJson(Map<String, Object> order) {
        try {
            return MAPPER.writeValueAsString(order);
        } catch (JsonProcessingException e) {
            throw new RuntimeException("failed to serialize order", e);
        }
    }

    /** Return the indexes of failed per-entry results (an entry with an errorCode). */
    static List<Integer> findFailures(PutEventsResponse response) {
        List<Integer> failures = new ArrayList<>();
        List<PutEventsResultEntry> entries = response.entries();
        for (int i = 0; i < entries.size(); i++) {
            if (entries.get(i).errorCode() != null) {
                failures.add(i);
            }
        }
        return failures;
    }

    /** Call PutEvents, retrying ThrottlingException with backoff + jitter. */
    static PutEventsResponse putEventsWithBackoff(
            EventBridgeV2Client client, String busArn, List<PutEventsRequestEntry> entries, int attempts) {
        long delayMs = 200;
        for (int attempt = 0; attempt < attempts; attempt++) {
            try {
                return client.putEvents(PutEventsRequest.builder()
                    .eventBusArn(busArn)
                    .entries(entries)
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
        // AWS SDK v2 surfaces throttling as an AwsServiceException whose error code
        // is "ThrottlingException"; match by simple name to avoid a hard import.
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

    /** Publish a single grouped order; throw on a per-entry failure. */
    static PutEventsResponse publishOne(
            EventBridgeV2Client client, String busArn, Map<String, Object> order, String group) {
        PutEventsResponse response =
            putEventsWithBackoff(client, busArn, List.of(buildEntry(order, group)), 5);
        Integer failedCount = response.failedEntryCount();
        if (!findFailures(response).isEmpty() || (failedCount != null && failedCount > 0)) {
            throw new RuntimeException("publish had failed entries: " + response.entries());
        }
        return response;
    }

    /** Publish {@code count} ordered events sharing {@code group}. Returns the event ids. */
    static List<String> publishSequence(
            EventBridgeV2Client client, String busArn, String group, int count) {
        List<String> eventIds = new ArrayList<>();
        for (int seq = 1; seq <= count; seq++) {
            Map<String, Object> order = buildOrder(group, seq);
            PutEventsResponse response = publishOne(client, busArn, order, group);
            PutEventsResultEntry entry = response.entries().get(0);
            eventIds.add(entry.eventId());
            System.out.printf(
                "Published seq=%d orderId=%s -> SuccessCode=%s EventId=%s%n",
                seq, order.get("orderId"), entry.successCode(), entry.eventId());
        }
        return eventIds;
    }

    static final class Args {
        String busArn = System.getenv("BUS_ARN");
        String region = System.getenv("AWS_REGION");
        int count = 5;
        String group;
    }

    static Args parseArgs(String[] argv) {
        Args args = new Args();
        for (int i = 0; i < argv.length; i++) {
            switch (argv[i]) {
                case "--bus-arn" -> args.busArn = argv[++i];
                case "--region" -> args.region = argv[++i];
                case "--count" -> args.count = Integer.parseInt(argv[++i]);
                case "--group" -> args.group = argv[++i];
                default -> { /* ignore unknown args */ }
            }
        }
        return args;
    }

    public static void main(String[] argv) {
        Args args = parseArgs(argv);
        if (args.busArn == null || args.busArn.isBlank()) {
            System.err.println("error: --bus-arn is required (or set BUS_ARN).");
            System.exit(2);
        }
        if (args.count < 1) {
            System.err.println("error: --count must be >= 1.");
            System.exit(2);
        }

        String group = (args.group != null) ? args.group
            : "order-group-" + (System.currentTimeMillis() / 1000);

        var clientBuilder = EventBridgeV2Client.builder();
        if (args.region != null && !args.region.isBlank()) {
            clientBuilder.region(software.amazon.awssdk.regions.Region.of(args.region));
        }

        try (EventBridgeV2Client client = clientBuilder.build()) {
            System.out.printf("Publishing %d ordered events in group '%s'...%n", args.count, group);
            publishSequence(client, args.busArn, group, args.count);
            System.out.printf(
                "%nThe FIFO subscriber invokes the consumer synchronously and processes "
                + "group '%s' in order. Check the consumer log to see seq=1..%d "
                + "processed in sequence.%n", group, args.count);
        }
    }
}
