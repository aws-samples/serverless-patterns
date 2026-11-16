// Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: MIT-0

/**
 * Consumer Lambda: the SYNCHRONOUS, ordered target of an EventBridge
 * custom-event-bus subscriber. It logs each delivered order to CloudWatch in the
 * order it is processed.
 *
 * Why this demonstrates ordered processing:
 *   - The subscriber is FIFO (Type = FIFO) and invokes this function
 *     synchronously (InvocationType = REQUEST_RESPONSE). EventBridge waits for
 *     the function to confirm successful processing of each event before
 *     acknowledging it and moving on to the next event in the same event group.
 *   - That synchronous confirmation is what makes ordered, reliable,
 *     direct-to-Lambda processing possible — it removes the pattern of putting an
 *     SQS queue between the bus and Lambda just to get reliability and
 *     back-pressure.
 *   - The publisher sends a sequence of orders that share one EventGroupId, each
 *     carrying a monotonically increasing `seq`. This handler logs `seq` as it
 *     processes each one; the log shows them in order (1, 2, 3, ...), proving the
 *     bus delivered and confirmed them one at a time, in sequence.
 *
 * Delivery shape:
 *   - A Lambda target receives a BATCH — a JSON array of delivered events — so
 *     the handler iterates it.
 *   - With the default RAW transformer and a PutEvents publish, each element is
 *     the classic envelope, so the order fields are under `detail`. The handler
 *     tolerates top-level fields too, for easy hand-invocation.
 *
 * The AWS SDK is not needed here; the handler only reads and logs the delivered
 * JSON.
 */

interface Order {
  orderId?: string;
  orderGroup?: string;
  seq?: number;
  [key: string]: unknown;
}

interface DeliveredEvent {
  detail?: Order;
  [key: string]: unknown;
}

type HandlerEvent = DeliveredEvent | DeliveredEvent[] | Order;

/** Coerce the incoming event into a list of delivered events. */
function normalizeBatch(event: HandlerEvent): DeliveredEvent[] {
  if (Array.isArray(event)) {
    return event;
  }
  if (event && typeof event === "object") {
    return [event as DeliveredEvent];
  }
  throw new Error(`unexpected event type: ${typeof event}`);
}

/**
 * Return the order fields from one delivered event.
 *
 * A RAW PutEvents payload is the classic envelope, so the order is under
 * `detail`. Fall back to the top level for hand-invocation.
 */
function extractOrder(item: DeliveredEvent): Order {
  if (item.detail && typeof item.detail === "object") {
    return item.detail;
  }
  return item as Order;
}

/** Lambda entry point. Logs each delivered order in processing order. */
export async function handler(
  event: HandlerEvent,
): Promise<{ processed: number }> {
  const delivered = normalizeBatch(event);
  const processed: Array<{ orderId?: string; group?: string; seq?: number }> = [];

  delivered.forEach((raw, batchIndex) => {
    const order = extractOrder(raw);
    const orderId = order.orderId;
    const group = order.orderGroup;
    const seq = order.seq;

    console.log(
      `Processing order group=${group} seq=${seq} orderId=${orderId} (batchIndex=${batchIndex})`,
    );
    processed.push({ orderId, group, seq });
  });

  console.log(`Processed ${processed.length} order(s): ${JSON.stringify(processed)}`);
  return { processed: processed.length };
}
