# AWS App Mesh with ECS Utilizing Two Services

This pattern will setup an ECS Cluster with two services and then stand up App Mesh so that one can achieve a circuit
breaker pattern and retry policy with only infrastructure.

To demonstrate how to implement App Mesh, a sample application will be utilized that was built from the ground up. This application consists of two ECS services: Service B and Service C. B, once executed, will then call C. A two word sentence will then be constructed. In short, this is a more complex version of Hello, World.

The technology stack that will drive our application is a Fargate ECS Cluster with two task definitions. Further, a new VPC with two public subnets and two private subnets will be created. This solution is rounded out with a bastion host in one of the private subnets that utilizes Systems Manager (SSM) in order to communicate with the endpoints.

An App Mesh is then created along with a virtual gateway, virtual services, virtual routes, and virtual nodes. In the backend, AWS Cloud Map and Route53 is utilized in order to provide service discovery.

Finally, a self-signed certificate will be generated so that SSL termination can be demonstrated with this solution. While the AWS CLI is necessary to generate the certificate, one can utilize either the CloudFormation service or SAM (Serverless Application Model) in order to execute the CF template located below.


Learn more about this pattern at Serverless Land Patterns: [https://serverlessland.com/patterns](https://serverlessland.com/patterns)

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) (AWS SAM) installed

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ``` 
    git clone https://github.com/aws-samples/serverless-patterns
    ```
2. Change directory to the pattern directory:
    ```
    cd _patterns-model
    ```
3. Setup the security certificate and export the ARN so that the CloudFormation template can utilize it.
   1. First, create a root Certificate Authority (CA):
   ```
   export ROOT_CA_ARN=`aws acm-pca create-certificate-authority \
    --certificate-authority-type ROOT \
    --certificate-authority-configuration \
    "KeyAlgorithm=RSA_2048,
    SigningAlgorithm=SHA256WITHRSA,
    Subject={
        Country=US,
        State=WA,
        Locality=Seattle,
        Organization=App Mesh Examples,
        OrganizationalUnit=Ingress Example,
        CommonName=${SERVICES_DOMAIN}}" \
        --query CertificateAuthorityArn --output text`
   ```
   2. Next, we’ll need to self-sign this root CA. First fetch the CSR:
   ```
   ROOT_CA_CSR=`aws acm-pca get-certificate-authority-csr \
    --certificate-authority-arn ${ROOT_CA_ARN} \
    --query Csr --output text`
   ```
   3. Then sign the CSR as the issuer:
   ```
   AWS_CLI_VERSION=$(aws --version 2>&1 | cut -d/ -f2 | cut -d. -f1)
   [[ ${AWS_CLI_VERSION} -gt 1 ]] && ROOT_CA_CSR="$(echo ${ROOT_CA_CSR} | base64)"

   ROOT_CA_CERT_ARN=`aws acm-pca issue-certificate \
   --certificate-authority-arn ${ROOT_CA_ARN} \
   --template-arn arn:aws:acm-pca:::template/RootCACertificate/V1 \
   --signing-algorithm SHA256WITHRSA \
   --validity Value=10,Type=YEARS \
   --csr "${ROOT_CA_CSR}" \
   --query CertificateArn --output text`
   ```
   4. Import this signed certificate as the root CA:
   ```
   ROOT_CA_CERT=`aws acm-pca get-certificate \
    --certificate-arn ${ROOT_CA_CERT_ARN} \
    --certificate-authority-arn ${ROOT_CA_ARN} \
    --query Certificate --output text`
   [[ ${AWS_CLI_VERSION} -gt 1 ]] && ROOT_CA_CERT="$(echo ${ROOT_CA_CERT} | base64)"
   ```
   5. Then import the certificate:
   ```
   aws acm-pca import-certificate-authority-certificate \
    --certificate-authority-arn $ROOT_CA_ARN \
    --certificate "${ROOT_CA_CERT}"
   ```
   6. We also want permissions to allow the CA to renew the certificate:
   ```
   aws acm-pca create-permission \
    --certificate-authority-arn $ROOT_CA_ARN \
    --actions IssueCertificate GetCertificate ListPermissions \
    --principal acm.amazonaws.com
   ```
   7. Finally, we can request a managed certificate using the CA:
   ```
   export CERTIFICATE_ARN=`aws acm request-certificate \
    --domain-name "*.${SERVICES_DOMAIN}" \
    --certificate-authority-arn ${ROOT_CA_ARN} \
    --query CertificateArn --output text`
   ```
4. Build and Upload the Container Images to ECR
   1. First, authenticate to ECR via the AWS CLI. Make sure to replace <ACCOUNT_ID> and <REGION> with the appropriate values.
   ```
   aws ecr get-login-password --region <REGION> \
   | docker login --username AWS --password-stdin \
   <ACCOUNT_ID>.dkr.ecr.<REGION>.amazonaws.com
   ```
   2. Next, build the images with
   ```
   cd src/serviceB
   docker build -t <ACCOUNT_ID>.dkr.ecr.<REGION>.amazonaws.com/serviceb .
   ```
   3. Then push it to ECR:
   ```
   docker push <ACCOUNT_ID>.dkr.ecr.<REGION>.amazonaws.com/serviceb:latest
   ```
   4. Repeat steps ii and iii for serviceC.
5. Modify the parameters in the CloudFormation template. 
   
6. From the command line, use AWS SAM to deploy the AWS resources for the pattern as specified in the template.yml file:
    ```
    sam deploy --guided
    ```
7. During the prompts:
    * Enter a stack name
    * Enter the desired AWS Region
    * Allow SAM CLI to create IAM roles with the required permissions.

    Once you have run `sam deploy --guided` mode once and saved arguments to a configuration file (samconfig.toml), you can use `sam deploy` in future to use these defaults.

8. Note the outputs from the SAM deployment process. These contain the resource names and/or ARNs which are used for testing.

## How it works

App Mesh is a service mesh that provides application-level networking and improves observability by providing consistent visibility and traffic controls.

App Mesh utilizes [Envoy](https://www.envoyproxy.io (https://www.envoyproxy.io/)) as a proxy to monitor and control communications to a container as a sidecar. With this control plane, one can achieve both circuit breaker and retry patterns in addition to service discovery.


## Testing

From the SAM output, take the `oServiceAppEndpoint` URL and paste that into a browser. One should see the output from 
the services that are being called through App Mesh.

## Cleanup
 
1. Delete the stack
    ```bash
    aws cloudformation delete-stack --stack-name STACK_NAME
    ```
2. Confirm the stack has been deleted
    ```bash
    aws cloudformation list-stacks --query "StackSummaries[?contains(StackName,'STACK_NAME')].StackStatus"
    ```
3. Delete the security certificate through ACM.   
----
Copyright 2021 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
