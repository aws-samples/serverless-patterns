import {
  LambdaClient,
  SendDurableExecutionCallbackSuccessCommand,
  SendDurableExecutionCallbackFailureCommand,
} from "@aws-sdk/client-lambda";
import { DynamoDBClient } from "@aws-sdk/client-dynamodb";
import { DynamoDBDocumentClient, GetCommand, UpdateCommand } from "@aws-sdk/lib-dynamodb";

const lambdaClient = new LambdaClient({});
const ddbClient = new DynamoDBClient({});
const docClient = DynamoDBDocumentClient.from(ddbClient);

// Valid actions — no default. Must be explicit.
const VALID_ACTIONS = new Set(['approve', 'reject']);

/**
 * Renders the confirmation page for GET requests.
 * This two-step pattern protects against email prefetchers (Outlook Safe Links,
 * Slack unfurl) silently triggering approvals on the GET.
 */
const renderConfirmationPage = (approvalId, action) => {
  const actionLabel = action === 'approve' ? 'Approve' : 'Reject';
  const actionColor = action === 'approve' ? '#2e7d32' : '#c62828';
  const actionMessage = action === 'approve'
    ? 'Are you sure you want to <strong>approve</strong> this request?'
    : 'Are you sure you want to <strong>reject</strong> this request?';

  return {
    statusCode: 200,
    headers: { 'Content-Type': 'text/html' },
    body: `<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Confirm Decision</title>
  <style>
    body { font-family: Arial, sans-serif; max-width: 600px; margin: 80px auto; padding: 0 20px; }
    .card { border: 1px solid #ddd; border-radius: 8px; padding: 32px; text-align: center; }
    .btn { display: inline-block; padding: 12px 32px; border-radius: 4px; border: none;
           color: white; font-size: 16px; cursor: pointer; text-decoration: none;
           background-color: ${actionColor}; }
    .cancel { margin-left: 16px; color: #555; text-decoration: none; font-size: 14px; }
  </style>
</head>
<body>
  <div class="card">
    <h2>Confirm Your Decision</h2>
    <p>${actionMessage}</p>
    <form method="POST" action="/prod/verify">
      <input type="hidden" name="id" value="${approvalId}">
      <input type="hidden" name="action" value="${action}">
      <button type="submit" class="btn">${actionLabel}</button>
    </form>
    <br>
    <a href="javascript:window.close()" class="cancel">Cancel</a>
  </div>
</body>
</html>`,
  };
};

export const handler = async (event) => {
  const method = event.httpMethod || event.requestContext?.http?.method || 'GET';

  // Route GET to confirmation page, POST to decision execution
  if (method === 'GET') {
    return handleGetRequest(event);
  } else if (method === 'POST') {
    return handlePostRequest(event);
  }

  return {
    statusCode: 405,
    headers: { 'Content-Type': 'text/html' },
    body: '<html><body><h1>Method Not Allowed</h1></body></html>',
  };
};

/**
 * GET /verify?id=<approvalId>&action=<approve|reject>
 * Renders a confirmation page — never executes the decision.
 * This prevents email prefetchers from silently approving/rejecting.
 */
const handleGetRequest = async (event) => {
  const approvalId = event.queryStringParameters?.id;
  const action = event.queryStringParameters?.action;

  if (!approvalId) {
    return {
      statusCode: 400,
      headers: { 'Content-Type': 'text/html' },
      body: '<html><body><h1>Bad Request</h1><p>Missing approval ID.</p></body></html>',
    };
  }

  // Validate action strictly — no defaulting
  if (!action || !VALID_ACTIONS.has(action)) {
    return {
      statusCode: 400,
      headers: { 'Content-Type': 'text/html' },
      body: '<html><body><h1>Bad Request</h1><p>Invalid or missing action. Must be "approve" or "reject".</p></body></html>',
    };
  }

  return renderConfirmationPage(approvalId, action);
};

/**
 * POST /verify
 * Executes the actual approval decision. Enforces single-use via a conditional
 * DynamoDB update — only the first POST succeeds; subsequent clicks are rejected.
 */
const handlePostRequest = async (event) => {
  // Parse body — API Gateway REST sends URL-encoded form data by default
  let approvalId, action;
  try {
    const body = event.isBase64Encoded
      ? Buffer.from(event.body, 'base64').toString('utf-8')
      : event.body || '';
    const params = new URLSearchParams(body);
    approvalId = params.get('id');
    action = params.get('action');
  } catch (err) {
    console.error('Failed to parse POST body:', err);
    return {
      statusCode: 400,
      headers: { 'Content-Type': 'text/html' },
      body: '<html><body><h1>Bad Request</h1><p>Could not parse request body.</p></body></html>',
    };
  }

  if (!approvalId) {
    return {
      statusCode: 400,
      headers: { 'Content-Type': 'text/html' },
      body: '<html><body><h1>Bad Request</h1><p>Missing approval ID.</p></body></html>',
    };
  }

  // Validate action strictly — no defaulting, no fallthrough
  if (!action || !VALID_ACTIONS.has(action)) {
    return {
      statusCode: 400,
      headers: { 'Content-Type': 'text/html' },
      body: '<html><body><h1>Bad Request</h1><p>Invalid or missing action. Must be "approve" or "reject".</p></body></html>',
    };
  }

  // Look up the callback token from Amazon DynamoDB
  let callbackId;
  try {
    const result = await docClient.send(new GetCommand({
      TableName: process.env.CALLBACK_TABLE_NAME,
      Key: { approvalId: approvalId },
    }));

    if (!result.Item) {
      return {
        statusCode: 404,
        headers: { 'Content-Type': 'text/html' },
        body: '<html><body><h1>Not Found</h1><p>Approval request not found or has expired.</p></body></html>',
      };
    }

    callbackId = result.Item.callbackId;
  } catch (error) {
    console.error('DynamoDB lookup failed:', { approvalId, error: error.message });
    return {
      statusCode: 500,
      headers: { 'Content-Type': 'text/html' },
      body: '<html><body><h1>Error</h1><p>Failed to look up approval request. Please try again.</p></body></html>',
    };
  }

  // Enforce single-use: atomically mark the token as consumed.
  // If another request already consumed it, the condition fails — return 409.
  try {
    await docClient.send(new UpdateCommand({
      TableName: process.env.CALLBACK_TABLE_NAME,
      Key: { approvalId: approvalId },
      UpdateExpression: 'SET consumedAt = :now',
      ConditionExpression: 'attribute_not_exists(consumedAt)',
      ExpressionAttributeValues: {
        ':now': new Date().toISOString(),
      },
    }));
  } catch (error) {
    if (error.name === 'ConditionalCheckFailedException') {
      // Already consumed — this is a replay or duplicate click
      return {
        statusCode: 409,
        headers: { 'Content-Type': 'text/html' },
        body: '<html><body><h1>Already Processed</h1><p>This approval request has already been actioned.</p></body></html>',
      };
    }

    // Unexpected error — fail the durable execution fast rather than letting it timeout
    console.error('Failed to mark token as consumed:', { approvalId, error: error.message });
    try {
      await lambdaClient.send(new SendDurableExecutionCallbackFailureCommand({
        CallbackId: callbackId,
        Error: {
          ErrorType: 'CallbackProcessingError',
          ErrorMessage: 'Failed to process approval decision due to an internal error.',
        },
      }));
    } catch (failErr) {
      console.error('Failed to send callback failure:', { error: failErr.message });
    }
    return {
      statusCode: 500,
      headers: { 'Content-Type': 'text/html' },
      body: '<html><body><h1>Error</h1><p>Failed to process your decision. Please try again.</p></body></html>',
    };
  }

  // Send the result back to the durable execution to resume the workflow
  try {
    const callbackResult = {
      approved: action === 'approve',
      approvalId: approvalId,
      timestamp: new Date().toISOString(),
    };

    await lambdaClient.send(new SendDurableExecutionCallbackSuccessCommand({
      CallbackId: callbackId,
      Result: JSON.stringify(callbackResult),
    }));

    const message = action === 'approve'
      ? '<h1>&#10003; Request Approved</h1><p>Thank you. The request has been approved.</p>'
      : '<h1>&#10007; Request Rejected</h1><p>You have rejected this request.</p>';

    return {
      statusCode: 200,
      headers: { 'Content-Type': 'text/html' },
      body: `<html><body>${message}</body></html>`,
    };
  } catch (error) {
    console.error('Failed to send callback success:', { approvalId, error: error.message });

    // Attempt to fail the execution fast so it doesn't wait for timeout
    try {
      await lambdaClient.send(new SendDurableExecutionCallbackFailureCommand({
        CallbackId: callbackId,
        Error: {
          ErrorType: 'CallbackDeliveryError',
          ErrorMessage: 'Approval decision was recorded but failed to resume the workflow.',
        },
      }));
    } catch (failErr) {
      console.error('Failed to send callback failure signal:', { error: failErr.message });
    }

    return {
      statusCode: 500,
      headers: { 'Content-Type': 'text/html' },
      body: '<html><body><h1>Error</h1><p>Your decision was recorded but failed to resume the workflow. Please contact support.</p></body></html>',
    };
  }
};
