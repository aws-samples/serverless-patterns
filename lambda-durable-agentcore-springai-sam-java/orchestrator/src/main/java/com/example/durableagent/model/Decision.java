/*! Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
 *  SPDX-License-Identifier: MIT-0
 */
package com.example.durableagent.model;

/**
 * The reviewer's verdict, as delivered to the waiting callback.
 *
 * <h2>Approve and reject are both callback successes</h2>
 *
 * Both are sent with {@code SendDurableExecutionCallbackSuccess}. The success/failure axis of the
 * callback API describes whether a decision was <em>obtained</em>, not whether the answer was
 * favourable - a reviewer who rejects a document has successfully decided. Reserve
 * {@code SendDurableExecutionCallbackFailure} for cases where no decision can be produced at all,
 * such as an abandoned review or an unreachable approver; that surfaces in the workflow as a
 * thrown exception rather than as a value.
 *
 * <p>Carrying the verdict as data also keeps replay deterministic: the workflow branches on this
 * checkpointed value, so every replay takes the same path.
 *
 * @param decision {@code approved} or {@code rejected}
 * @param comments optional reviewer notes, passed to the agent when finalizing
 */
public record Decision(String decision, String comments) {

    public boolean isApproved() {
        return "approved".equalsIgnoreCase(decision);
    }
}
