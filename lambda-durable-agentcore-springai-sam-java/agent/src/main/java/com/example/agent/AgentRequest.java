/*! Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
 *  SPDX-License-Identifier: MIT-0
 */
package com.example.agent;

/**
 * Payload sent by the durable function to {@code POST /invocations}.
 *
 * <p>A single agent runtime serves both workflow steps. {@code mode} selects which system
 * prompt to apply:
 *
 * <ul>
 *   <li>{@code analyze}  - summarise {@code document} and produce a draft for review.
 *   <li>{@code finalize} - polish {@code draft}, taking {@code reviewerComments} into account.
 * </ul>
 *
 * @param mode             either {@code analyze} or {@code finalize}
 * @param document         the original document text (used by {@code analyze})
 * @param draft            the approved draft (used by {@code finalize})
 * @param reviewerComments free-text comments captured at the approval gate; may be null
 */
public record AgentRequest(
        String mode,
        String document,
        String draft,
        String reviewerComments) {
}
