# Amazon APIGW Private Custom Domain API with Internet-Enabled Lambda using NAT Gateway in Terraform

This architecture demonstrates how to build a private API accessible only from within a VPC using API Gateway private endpoints, where the API is protected by custom domain names and SSL certificates. The solution includes a Lambda function running in private subnets that can access the internet through NAT Gateways, and an EC2 instance configured with Systems Manager Session Manager for secure management, all while maintaining network isolation and security best practices through VPC endpoints.

User only needs to provide the following 2 variables, rest of the things will be handled by the code:
[1]. `aws_region`
[2]. `private_custom_domain_name`

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [Terraform](https://learn.hashicorp.com/tutorials/terraform/install-cli?in=terraform/aws-get-started) installed

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
CMD : git clone https://github.com/aws-samples/serverless-patterns

2. Change directory to the pattern directory:
CMD : cd serverless-patterns/private-apigw-custom-domain-private-restapi-public-lambda-terraform

3. From the command line, initialize terraform to download and install the providers defined in the configuration:
CMD : terraform init

4. Review the resources that will be created:
CMD : terraform plan

5. From the command line, apply the configuration in the main.tf file:
CMD : terraform apply -auto-approve 

6. Wait for the deployment to complete. This may take 10-15 minutes due to ACM certificate validation and API Gateway deployment.

7. After deployment, note the outputs for testing.

## How it works

The architecture works by routing API requests through a VPC Endpoint (PrivateLink) to API Gateway, ensuring all traffic stays within AWS's private network. When a request is made to the private API using the private custom domain (e.g., mydomain@example.com), it's resolved through a private hosted zone in Route 53, which directs traffic to the VPC Endpoint. The request then flows to the API Gateway, which invokes a Lambda function running in private subnets, this Lambda can access the internet via NAT Gateways while maintaining security. For testing and management, an EC2 instance in the private subnet can access the API and be managed securely using Systems Manager Session Manager without requiring any public IP or bastion host.

## Testing

Once the terraform apply command is completed and resources are created, you will able to see the output of the script in the terminal. The output will contain the following information:
1. api_gateway_configuration
2. dns_and_certificates
3. ec2_instance
4. network_infrastructure 
5. security
6. ssm_endpoints
7. vpc_endpoint_details

Now, copy the "endpoint_url" from the api_gateway_configuration and run it in the ec2 instance(created by the terraform) by connecting it through the session manager. Below is the format of the commmand : 

CMD : curl -X GET <endpoint_url>

# Sample Output :

{
  "timestamp": "2025-04-03T04:21:07.426825",
  "function_name": "private-api-lambda-egwvbbtf",
  "internet_connectivity_test": {
    "status": "Success",
    "message": "Successfully connected to external website",
    "aws_status_code": 200,
    "aws_page_title": "Cloud Computing Services - Amazon Web Services (AWS)",
    "test_time": "2025-04-03 04:21:07"
    }
}

## Cleanup

1. Make sure you are in the "private-apigw-custom-domain-private-restapi-public-lambda-terraform" directory.

2. Run the following command to destroy the infrastructure:
CMD : terraform destroy -auto-approve

