# Amazon Verified Permissions with AWS Lambda

This pattern deploys a Lambda function that authorizes requests using Amazon Verified Permissions with Cedar policies for fine-grained access control.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/lambda-verified-permissions-cdk

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details.

## Requirements

* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Node.js 22+](https://nodejs.org/en/download/) installed
* [AWS CDK v2](https://docs.aws.amazon.com/cdk/v2/guide/getting-started.html) installed

## How it works

1. A client sends a SigV4-signed request to the Lambda Function URL (`AWS_IAM` auth).
2. Lambda reads the caller's IAM principal from the request context that the Function URL fills in after it verifies the signature. The request body only supplies `action` and `resourceId`.
3. Lambda maps the principal to a role (`admin` if it is listed in the `adminPrincipals` context value, otherwise `reader`) and looks up the document's owner and classification from server-side data.
4. Lambda calls the Verified Permissions `IsAuthorized` API. Cedar policies evaluate the request and return ALLOW or DENY.

Verified Permissions evaluates policies but does not authenticate callers. The principal and role are therefore never taken from the request body.

## Cedar Policies

The pattern includes four policies demonstrating different authorization patterns:

- **Admin policy** – Admins can read, write, and delete documents (scoped to explicit actions).
- **Reader policy** – Readers can only read documents.
- **Owner policy** – Document owners can write to their own documents.
- **Confidential deny policy** – Readers cannot access confidential documents.

## Deployment

```bash
cd src && npm install && cd ..
npm install
cdk deploy
```

Optional context values (comma-separated principals are matched exactly):

* `-c adminPrincipals=<principal>[,<principal>]` gives those callers the `admin` role. Without it every caller is a `reader`.
* `-c ownerPrincipal=<principal>` makes that caller the owner of the demo documents `doc-1` (confidential) and `doc-2` (public).

A principal is the IAM user ARN, or for an assumed role the ARN without the session name. Get yours with:

```bash
CALLER=$(aws sts get-caller-identity --query Arn --output text | sed -E 's#^(arn:[^:]+:sts::[0-9]+:assumed-role/[^/]+)/.+#\1#')
echo "$CALLER"
```

For example: `cdk deploy -c ownerPrincipal="$CALLER" -c adminPrincipals="$CALLER"`.

## Testing

The Lambda Function URL uses `AWS_IAM` authentication, so requests must be signed with [SigV4](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html). The simplest way is `curl` with `--aws-sigv4`. Set `AWS_REGION` to the Region you deployed to.

```bash
FUNCTION_URL=$(aws cloudformation describe-stacks \
  --stack-name LambdaVerifiedPermissionsStack \
  --query 'Stacks[0].Outputs[?OutputKey==`FunctionUrl`].OutputValue' \
  --output text)
eval "$(aws configure export-credentials --format env)"

call() {
  curl -s "$FUNCTION_URL" \
    --aws-sigv4 "aws:amz:$AWS_REGION:lambda" \
    --user "$AWS_ACCESS_KEY_ID:$AWS_SECRET_ACCESS_KEY" \
    -H "x-amz-security-token: $AWS_SESSION_TOKEN" \
    -H "Content-Type: application/json" \
    -d "$1"
}
```

Deployed with no context values, your principal is a `reader` and not an owner:

```bash
# Reader can read a public document (ALLOW)
call '{"action":"Read","resourceId":"doc-2"}'

# Reader cannot read a confidential document (DENY)
call '{"action":"Read","resourceId":"doc-1"}'

# Reader cannot delete, and claiming the admin role in the body has no effect (DENY)
call '{"action":"Delete","resourceId":"doc-2","role":"admin","userId":"alice"}'

# Not the owner, so cannot write (DENY)
call '{"action":"Write","resourceId":"doc-2"}'
```

Redeploy with `-c ownerPrincipal="$CALLER"`, then the owner can write:

```bash
call '{"action":"Write","resourceId":"doc-2"}'    # ALLOW
```

Redeploy with `-c adminPrincipals="$CALLER"` (keep `-c ownerPrincipal="$CALLER"` too, because context values are not remembered between deploys), then the admin can delete:

```bash
call '{"action":"Delete","resourceId":"doc-1"}'   # ALLOW
```

The response contains the `decision`, the `principal` and `role` that the Lambda resolved.

## Cleanup

```bash
cdk destroy
```
