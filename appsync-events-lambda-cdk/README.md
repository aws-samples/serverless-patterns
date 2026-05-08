# AWS AppSync Events with Lambda

This pattern deploys an AppSync Events API for real-time WebSocket pub/sub with Lambda event processing.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/appsync-events-lambda-cdk

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details.

## Requirements

* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Node.js 22+](https://nodejs.org/en/download/) installed
* [AWS CDK v2](https://docs.aws.amazon.com/cdk/v2/guide/getting-started.html) installed

## Architecture

```
┌───────────┐     ┌─────────────────────┐     ┌──────────────┐
│ Publisher │────▶│  AppSync Events API │────▶│ Subscribers  │
│ (HTTP)    │     │  (WebSocket)        │     │ (WebSocket)  │
└───────────┘     └─────────────────────┘     └──────────────┘
                         │
                         ▼
                  ┌──────────────┐
                  │ AWS Lambda   │
                  │ (Handler)    │
                  └──────────────┘
```

## How it works

1. Publishers send events via HTTP POST to the AppSync Events endpoint.
2. AppSync Events delivers messages to all WebSocket subscribers on that channel.
3. Channel namespaces (`notifications`, `alerts`) organize topics.
4. A Lambda handler can process/enrich events before delivery.

## Deployment

```bash
npm install
cdk deploy
```

## Testing

```bash
# Publish an event (replace values from cdk deploy output)
curl -X POST "https://<HttpEndpoint>/event" \
  -H "x-api-key: <ApiKeyValue>" \
  -H "Content-Type: application/json" \
  -d '{"channel":"/notifications/general","events":["{\"message\":\"Hello from CDK\"}"]}'
```

## Cleanup

```bash
cdk destroy
```
