// Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: MIT-0

// AgentCore Gateway passes the tool arguments as the event and the tool name,
// "<target name>___<tool name>", in the client context.
const ORDERS = new Map([['1001', 'SHIPPED'], ['1002', 'PROCESSING']]);

export const handler = async (event, context) => {
  const tool = (context.clientContext?.custom?.bedrockAgentCoreToolName ?? '').split('___').pop();
  const orderId = String(event?.orderId ?? '');
  if (!/^[0-9]{1,10}$/.test(orderId)) {
    throw new Error('orderId must be 1 to 10 digits');
  }

  if (tool === 'lookup_order') {
    return { orderId, status: ORDERS.get(orderId) ?? 'UNKNOWN' };
  }
  if (tool === 'cancel_order') {
    return { orderId, result: 'CANCELLED (demo only, no data is changed)' };
  }
  throw new Error(`Unknown tool: ${tool}`);
};
