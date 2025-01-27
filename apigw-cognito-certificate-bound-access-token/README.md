# Certificate-Bound Access Tokens using Amazon API Gateway and Amazon Cognito

This pattern makes use of API Gateway and Cognito to implement certificate-bound access tokens. For more on certificate-boud access tokens, review the [RFC](https://datatracker.ietf.org/doc/html/rfc8705). This solution has some manual steps which will be discussed later.

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html)~ if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)~
* [AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html)~ (AWS SAM) installed
* [Docker installed](https://docs.docker.com/engine/install/).
* A domain that you own.
* A certificate issued under the domain you own.
* Create client certificate as per the [mTLS blogpost](https://aws.amazon.com/blogs/compute/introducing-mutual-tls-authentication-for-amazon-api-gateway/).

Place the trust store in the S3 bucket that you will specfiy when deploying in the solution.

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
```
git clone https://github.com/aws-samples/serverless-patterns
```

2. Change directory to the pattern directory:
```
cd apigw-cognito-certificate-bound-access-token
```

3. Build the solution:
```
sam build --use-container
```

3. Deploy the solution:
```
sam deploy --guided
```

Parameter_overrides:
  * BucketName - to store client certificate and trust store.
  * CACertKey - trust store.
  * ClientCertKey - client certificate Amazon S3 object key.
  * CustomDomainCertArn - custom domain AWS Certificate Manager certficate ARN.
  * CustomDomainName - custom domain name for API Gateway. Must match CustomDomainCertArn.

## How it works

This pattern creates an Amazon API Gateway REST API with a custom domain name and enables mTLS. Further, it creates a Cognito User Pool. The Cognito User Pool is used to issue certificate-bound access tokens. The REST API makes use of an authorizer to compare the "cnf" claim in the access token to the fingerprint of the client certificate sent as part of the mutual authentication TLS handshake. 

## Testing

1. Determine the fingerprint of the client certificate and base64 encode it:
```
openssl x509 -in client-cert.crt -noout -fingerprint -sha256 | cut -d'=' -f2 | tr -d ':' | xxd -r -p | base64 | tr -d '='
```

2. Navigate to the Cognito User Pool created in the solution. [Then create and verify](https://docs.aws.amazon.com/cognito/latest/developerguide/signing-up-users-in-your-app.html) a user.

3. Add the certificate fingerprint to the `custom:cert_fingerprint` custom attribute of the user.

4. [Create a DNS record](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-to-api-gateway.html) for the custom domain.

5. [Get an access token](https://docs.aws.amazon.com/cognito/latest/developerguide/authentication-flows-public-server-side.html) from Cognito.

Example of getting an access token using the AWSCLI:
```
aws cognito-idp admin-initiate-auth \
    --user-pool-id YOUR_USER_POOL_ID \
    --client-id YOUR_CLIENT_ID \
    --auth-flow ADMIN_USER_PASSWORD_AUTH \
    --auth-parameters 'USERNAME=YOUR_USERNAME,PASSWORD=YOUR_PASSWORD' \
    --region us-east-1 \
    --query 'AuthenticationResult.AccessToken' \
    --output text
```

Notes that this requires the `ADMIN_USER_PASSWORD_AUTH` auth flow which is not enabled by default by this solution. You will need to do it on the console. This is only for testing purposes. 

6. Test the solution:

```
curl -v https://<your_custom_domain>/example --cert client-cert.crt --key client-cert.key -H "Authorization: <certificate_bound_access_token>"
```

You should see output as follows:
```
{"message": "Hello from the example function!", "event": {"resource": "/example", "path": "/example"...
```

## Cleanup
 
1. Delete the stack
    ```bash
    sam delete
    ```
1. Confirm the stack has been deleted
    ```bash
    aws cloudformation list-stacks --query "StackSummaries[?contains(StackName,'STACK_NAME')].StackStatus"
    ```
----
Copyright 2024 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
