// Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: MIT-0

package com.example.orders;

import org.junit.jupiter.api.Test;
import software.amazon.awssdk.services.eventbridgev2.EventBridgeV2Client;
import software.amazon.awssdk.services.eventbridgev2.model.PutRawEventsRequest;
import software.amazon.awssdk.services.eventbridgev2.model.PutRawEventsRequestEntry;
import software.amazon.awssdk.services.eventbridgev2.model.PutRawEventsResponse;
import software.amazon.awssdk.services.eventbridgev2.model.PutRawEventsResultEntry;
import software.amazon.awssdk.services.glue.GlueClient;
import software.amazon.awssdk.services.glue.model.GetSchemaVersionRequest;
import software.amazon.awssdk.services.glue.model.GetSchemaVersionResponse;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertThrows;
import static org.junit.jupiter.api.Assertions.assertTrue;
import static org.mockito.ArgumentMatchers.any;
import static org.mockito.Mockito.mock;
import static org.mockito.Mockito.when;

/**
 * Unit tests for the publisher's entry-building, schema-version lookup, and
 * result-checking, using Mockito-mocked EventBridgeV2 and Glue clients (offline).
 */
class PublisherTest {

    private static final String TEST_REGION = "aws-region-1";
    private static final String BUS_ARN =
        "arn:aws:events:" + TEST_REGION + ":111122223333:event-busv2/avro-orders-bus/abc123";
    private static final String REGISTRY_ARN =
        "arn:aws:glue:" + TEST_REGION + ":111122223333:registry/avro-orders-registry";
    private static final String SCHEMA_VERSION_ID = "e424651b-7a41-405d-bf05-2cae8cdf5aea";

    @Test
    void buildEntryFramesDataAndSetsMetadata() {
        PutRawEventsRequestEntry entry =
            Publisher.buildEntry(AvroIo.buildOrder("order-abc"), SCHEMA_VERSION_ID);
        byte[] data = entry.data().asByteArray();
        // Data is Glue-framed: 0x03, 0x00, then the schema-version UUID.
        assertEquals(0x03, data[0] & 0xFF);
        assertEquals(0x00, data[1] & 0xFF);
        assertEquals("application/avro", entry.systemMetadata().contentType());
        assertEquals("OrderPlaced", entry.metadata().get("eventType"));
        // The framed UUID matches the schema version we asked for.
        assertEquals(SCHEMA_VERSION_ID, AvroIo.glueUnframe(data).schemaVersionId());
    }

    @Test
    void resolveSchemaVersionIdReadsFromGlue() {
        GlueClient glue = mock(GlueClient.class);
        when(glue.getSchemaVersion(any(GetSchemaVersionRequest.class)))
            .thenReturn(GetSchemaVersionResponse.builder().schemaVersionId(SCHEMA_VERSION_ID).build());
        String id = Publisher.resolveSchemaVersionId(glue, REGISTRY_ARN);
        assertEquals(SCHEMA_VERSION_ID, id);
    }

    @Test
    void findFailuresEmptyOnSuccess() {
        PutRawEventsResponse resp = PutRawEventsResponse.builder()
            .failedEntryCount(0)
            .entries(PutRawEventsResultEntry.builder().successCode("PUBLISHED").eventId("e1").build())
            .build();
        assertTrue(Publisher.findFailures(resp).isEmpty());
    }

    @Test
    void findFailuresReportsErrors() {
        PutRawEventsResponse resp = PutRawEventsResponse.builder()
            .failedEntryCount(1)
            .entries(PutRawEventsResultEntry.builder()
                .errorCode("ValidationError").errorMessage("bad").build())
            .build();
        assertEquals(1, Publisher.findFailures(resp).size());
    }

    @Test
    void publishSendsPutRawEventsNamingTheRegistry() {
        EventBridgeV2Client client = mock(EventBridgeV2Client.class);
        final PutRawEventsRequest[] sent = new PutRawEventsRequest[1];
        when(client.putRawEvents(any(PutRawEventsRequest.class))).thenAnswer(inv -> {
            sent[0] = inv.getArgument(0);
            return PutRawEventsResponse.builder()
                .failedEntryCount(0)
                .entries(PutRawEventsResultEntry.builder().successCode("PUBLISHED").eventId("e1").build())
                .build();
        });

        PutRawEventsResponse response = Publisher.publish(
            client, BUS_ARN, REGISTRY_ARN, AvroIo.buildOrder("order-abc"), SCHEMA_VERSION_ID);
        assertEquals("PUBLISHED", response.entries().get(0).successCodeAsString());
        assertEquals(BUS_ARN, sent[0].eventBusArn());
        assertEquals(REGISTRY_ARN, sent[0].schemaRegistryConfiguration().registryUri());
    }

    @Test
    void publishThrowsOnFailedEntry() {
        EventBridgeV2Client client = mock(EventBridgeV2Client.class);
        when(client.putRawEvents(any(PutRawEventsRequest.class))).thenReturn(
            PutRawEventsResponse.builder()
                .failedEntryCount(1)
                .entries(PutRawEventsResultEntry.builder()
                    .errorCode("ValidationError").errorMessage("bad").build())
                .build());
        RuntimeException ex = assertThrows(RuntimeException.class, () -> Publisher.publish(
            client, BUS_ARN, REGISTRY_ARN, AvroIo.buildOrder("order-abc"), SCHEMA_VERSION_ID));
        assertTrue(ex.getMessage().contains("failed entries"));
    }
}
