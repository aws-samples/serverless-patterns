// Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: MIT-0
//
// Demo workload that loops ON PURPOSE. It invokes itself asynchronously, but only when the incoming event has
// loop === true. Events without that flag are processed once and stop.
// The hop counter is a second safety stop for the demo: a chain ends after MAX_HOPS invocations even if
// recursive loop detection does not act. This is not a design to copy into a real workload.
import { LambdaClient, InvokeCommand } from '@aws-sdk/client-lambda';

const FUNCTION_NAME = process.env.AWS_LAMBDA_FUNCTION_NAME;
const MAX_HOPS = Number(process.env.MAX_HOPS);
if (!FUNCTION_NAME || !Number.isInteger(MAX_HOPS) || MAX_HOPS < 1) {
  throw new Error('AWS_LAMBDA_FUNCTION_NAME and MAX_HOPS must be set');
}

// The SDK adds the trace header that recursive loop detection uses to count invocations in a chain.
// Two attempts of at most about 1 second each, so a slow Invoke call ends inside the 5 second function timeout.
// In current SDK versions requestTimeout only logs a warning unless throwOnRequestTimeout is true.
const client = new LambdaClient({ maxAttempts: 2, requestHandler: { connectionTimeout: 500, requestTimeout: 1000, throwOnRequestTimeout: true } });

export const handler = async (event) => {
  const loop = event?.loop === true;
  const hop = Number(event?.hop ?? 0);
  console.info(`looper hop=${hop} loop=${loop}`);
  if (!loop) return;
  // A hop that is not a whole number >= 0 would reset or defeat the counter, so the loop stops there.
  if (!Number.isInteger(hop) || hop < 0 || hop + 1 >= MAX_HOPS) return;

  try {
    await client.send(new InvokeCommand({
      FunctionName: FUNCTION_NAME,
      InvocationType: 'Event',
      Payload: JSON.stringify({ loop: true, hop: hop + 1 }),
    }));
  } catch (err) {
    console.error('looper could not invoke itself', err);
    throw err;
  }
};
