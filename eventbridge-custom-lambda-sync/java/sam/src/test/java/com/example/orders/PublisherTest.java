// Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: MIT-0

package com.example.orders;

import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;
import org.junit.jupiter.api.Test;
import software.amazon.awssdk.services.eventbridgev2.EventBridgeV2Client;
import software.amazon.awssdk.services.eventbridgev2.model.PutEventsRequest;
import software.amazon.awssdk.services.eventbridgev2.model.PutEventsRequestEntry;
import software.amazon.awssdk.services.eventbridgev2.model.PutEventsResponse;
import software.amazon.awssdk.services.eventbridgev2.model.PutEventsResultEntry;

import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.concurrent.atomic.AtomicInteger;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertThrows;
import static org.junit.jupiter.api.Assertions.assertTrue;
import static org.mockito.ArgumentMatchers.any;
import static org.mockito.Mockito.mock;
import static org.mockito.Mockito.when;

/**
 * Unit tests for the publisher's entry-building, grouping, and result-checking.
 *
 * <p>Uses a Mockito-mocked {@link EventBridgeV2Client}, so the tests run fully
 * offline and never call AWS. The captured request lets us assert the exact
 * PutEvents entry shape (including the SystemMetadata.EventGroupId nesting).
 */
class PublisherTest {

    private static final String TEST_REGION = "aws-region-1";
    private static final String BUS_ARN =
        "arn:aws:events:" + TEST_REGION + ":111122223333:event-busv2/sync-orders-bus/abc123def456";

    private static final ObjectMapper MAPPER = new ObjectMapper();

    @Test
    void buildOrderCarriesGroupAndSeq() {
        Map<String, Object> order = Publisher.buildOrder("grp", 3);
        assertEquals("grp", order.get("orderGroup"));
        assertEquals(3, order.get("seq"));
        assertEquals("grp-003", order.get("orderId"));
    }

    @Test
    void buildEntrySetsEventGroupId() throws Exception {
        PutEventsRequestEntry entry = Publisher.buildEntry(Publisher.buildOrder("grp", 1), "grp");
        assertEquals("com.example.orders", entry.source());
        assertEquals("OrderPlaced", entry.detailType());
        assertEquals("grp", entry.systemMetadata().eventGroupId());
        JsonNode detail = MAPPER.readTree(entry.detail());
        assertEquals(1, detail.get("seq").asInt());
    }

    @Test
    void findFailuresEmptyOnSuccess() {
        PutEventsResponse resp = PutEventsResponse.builder()
            .failedEntryCount(0)
            .entries(PutEventsResultEntry.builder().eventId("e1").build())
            .build();
        assertTrue(Publisher.findFailures(resp).isEmpty());
    }

    @Test
    void findFailuresReportsErrors() {
        PutEventsResponse resp = PutEventsResponse.builder()
            .failedEntryCount(1)
            .entries(PutEventsResultEntry.builder()
                .errorCode("ValidationError").errorMessage("bad").build())
            .build();
        List<Integer> failures = Publisher.findFailures(resp);
        assertEquals(1, failures.size());
        assertEquals(0, failures.get(0));
    }

    @Test
    void publishSequencePublishesEachInOrder() {
        EventBridgeV2Client client = mock(EventBridgeV2Client.class);
        List<PutEventsRequest> sent = new ArrayList<>();
        AtomicInteger call = new AtomicInteger(0);
        when(client.putEvents(any(PutEventsRequest.class))).thenAnswer(inv -> {
            sent.add(inv.getArgument(0));
            int n = call.incrementAndGet();
            return PutEventsResponse.builder()
                .failedEntryCount(0)
                .entries(PutEventsResultEntry.builder().eventId("e" + n).build())
                .build();
        });

        List<String> eventIds = Publisher.publishSequence(client, BUS_ARN, "grp", 3);
        assertEquals(List.of("e1", "e2", "e3"), eventIds);

        // Each call sent one entry carrying the shared EventGroupId, in order.
        assertEquals(3, sent.size());
        for (int i = 0; i < sent.size(); i++) {
            PutEventsRequest req = sent.get(i);
            assertEquals(BUS_ARN, req.eventBusArn());
            PutEventsRequestEntry entry = req.entries().get(0);
            assertEquals("grp", entry.systemMetadata().eventGroupId());
        }
    }

    @Test
    void publishOneThrowsOnFailedEntry() {
        EventBridgeV2Client client = mock(EventBridgeV2Client.class);
        when(client.putEvents(any(PutEventsRequest.class))).thenReturn(
            PutEventsResponse.builder()
                .failedEntryCount(1)
                .entries(PutEventsResultEntry.builder()
                    .errorCode("ValidationError").errorMessage("bad").build())
                .build());

        RuntimeException ex = assertThrows(RuntimeException.class,
            () -> Publisher.publishOne(client, BUS_ARN, Publisher.buildOrder("grp", 1), "grp"));
        assertTrue(ex.getMessage().contains("failed entries"));
    }
}
