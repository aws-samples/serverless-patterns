/*! Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
 *  SPDX-License-Identifier: MIT-0
 */
package com.example.durableagent.model;

/**
 * Workflow input, submitted through {@code POST /documents}.
 *
 * @param documentId  caller-supplied identifier, used to derive a stable AgentCore session ID
 * @param title       short human-readable label included in the approval notification
 * @param documentText the content the agent should review
 */
public record ReviewRequest(String documentId, String title, String documentText) {
}
