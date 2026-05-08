# Amazon Verified Permissions with AWS Lambda

This pattern deploys a Lambda function that authorizes requests using Amazon Verified Permissions with Cedar policies for fine-grained access control.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/lambda-verified-permissions-cdk

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details.

## Requirements

* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Node.js 22+](https://nodejs.org/en/download/) installed
* [AWS CDK v2](https://docs.aws.amazon.com/cdk/v2/guide/getting-started.html) installed

## Architecture

```
┌──────────┐     ┌──────────────────┐     ┌─────────────────────────┐
│  Client  │────▶│  AWS Lambda      │────▶│  Amazon Verified        │
│          │     │  (Authorizer)    │     │  Permissions            │
└──────────┘     └──────────────────┘     │  (Cedar Policy Store)   │
                                          └─────────────────────────┘
```

## How it works

1. Lambda receives an authorization request with user identity, action, and resource.
2. Lambda calls the Verified Permissions `IsAuthorized` API with the request context.
3. Cedar policies evaluate the request and return ALLOW or DENY.
4. The pattern includes two policies: admins can perform any action, readers can only read.

## Deployment

```bash
npm install
cdk deploy
```

## Testing

```bash
python3 -c "
import boto3, json
client = boto3.client('lambda')
# Admin can delete (ALLOW)
r = client.invoke(FunctionName='<FunctionName>', Payload=json.dumps({'body': json.dumps({'userId':'alice','role':'admin','action':'Delete','resourceId':'doc-1','classification':'confidential'})}))
print('Admin Delete:', json.loads(json.loads(r['Payload'].read())['body'])['decision'])
# Reader cannot delete (DENY)
r = client.invoke(FunctionName='<FunctionName>', Payload=json.dumps({'body': json.dumps({'userId':'bob','role':'reader','action':'Delete','resourceId':'doc-2','classification':'public'})}))
print('Reader Delete:', json.loads(json.loads(r['Payload'].read())['body'])['decision'])
"
```

## Cleanup

```bash
cdk destroy
```
