/*! Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
 *  SPDX-License-Identifier: MIT-0
 */
package com.example.durableagent.model;

/**
 * The workflow's return value. Lambda checkpoints this as the durable execution's result, so it
 * is readable with {@code aws lambda get-durable-execution} for as long as the configured
 * retention period allows - the pattern stores it nowhere else.
 *
 * <p>{@code outcome} and {@code decision} answer two different questions, and keeping them apart
 * avoids conflating "the reviewer said no" with "nobody ever answered":
 *
 * <ul>
 *   <li>{@code outcome} - was a decision obtained at all? {@code DECIDED} or {@code EXPIRED}.
 *   <li>{@code decision} - what the reviewer chose: {@code APPROVED} or {@code REJECTED}.
 *       Null when {@code outcome} is {@code EXPIRED}.
 * </ul>
 *
 * @param documentId   the identifier supplied on submission
 * @param outcome      {@code DECIDED} if a human responded, {@code EXPIRED} if the callback timed out
 * @param decision     {@code APPROVED} or {@code REJECTED}; null when {@code outcome} is {@code EXPIRED}
 * @param draft        the agent's review draft, retained whatever the outcome
 * @param finalSummary the polished summary; null unless the reviewer approved
 * @param comments     reviewer notes, if any
 */
public record ReviewResult(
        String documentId,
        String outcome,
        String decision,
        String draft,
        String finalSummary,
        String comments) {

    public static final String DECIDED = "DECIDED";
    public static final String EXPIRED = "EXPIRED";
    public static final String APPROVED = "APPROVED";
    public static final String REJECTED = "REJECTED";

    /** A review a human approved. */
    public static ReviewResult approved(
            String documentId, String draft, String finalSummary, String comments) {
        return new ReviewResult(documentId, DECIDED, APPROVED, draft, finalSummary, comments);
    }

    /** A review a human rejected. Still a decision, so the outcome is {@code DECIDED}. */
    public static ReviewResult rejected(String documentId, String draft, String comments) {
        return new ReviewResult(documentId, DECIDED, REJECTED, draft, null, comments);
    }

    /** No decision arrived before the callback timed out. */
    public static ReviewResult expired(String documentId, String draft) {
        return new ReviewResult(documentId, EXPIRED, null, draft, null,
                "No decision was received before the approval window closed");
    }
}
