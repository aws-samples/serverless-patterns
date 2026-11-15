# Amazon API Gateway (HTTP) to AWS Lambda

This pattern creates an Amazon API Gateway HTTP API and an AWS Lambda function.

## Getting started with Terraform Serverless Patterns

Read more about general requirements and deployment instructions for Terraform Serverless Patterns [here](https://github.com/aws-samples/serverless-patterns/blob/main/terraform-fixtures/docs/README.md). 

## Testing

Call the endpoint retrieved from the `apigatewayv2_api_api_endpoint` output using `curl` or Postman.

```
curl https://wargabe3ei.execute-api.eu-west-1.amazonaws.com

#sample output
{
   "hello":"Hello Python! Hello Terraform!",
   "functionName":"famous-emu-lambda",
   "event":{
      "version":"2.0",
      "routeKey":"ANY /",
      "rawPath":"/",
      "rawQueryString":"",
      "headers":{
         "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
         "accept-encoding":"gzip, deflate, br",
         "accept-language":"en-US,en;q=0.9,uk;q=0.8,es-ES;q=0.7,es;q=0.6,ru;q=0.5,no;q=0.4,nb;q=0.3",
         "content-length":"0",
         "dnt":"1",
         "host":"k4l4ajulel.execute-api.eu-west-1.amazonaws.com",
         "sec-ch-ua":"\"Google Chrome\";v=\"107\", \"Chromium\";v=\"107\", \"Not=A?Brand\";v=\"24\"",
         "sec-ch-ua-mobile":"?0",
         "sec-ch-ua-platform":"\"macOS\"",
         "sec-fetch-dest":"document",
         "sec-fetch-mode":"navigate",
         "sec-fetch-site":"none",
         "sec-fetch-user":"?1",
         "upgrade-insecure-requests":"1",
         "user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
         "x-amzn-trace-id":"Root=1-636ba988-62a696d211fcf22255036432",
         "x-forwarded-for":"79.160.217.204",
         "x-forwarded-port":"443",
         "x-forwarded-proto":"https"
      },
      "requestContext":{
         "accountId":"835367859851",
         "apiId":"k4l4ajulel",
         "domainName":"k4l4ajulel.execute-api.eu-west-1.amazonaws.com",
         "domainPrefix":"k4l4ajulel",
         "http":{
            "method":"GET",
            "path":"/",
            "protocol":"HTTP/1.1",
            "sourceIp":"79.160.217.204",
            "userAgent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
         },
         "requestId":"bVdtYjsRjoEEJ6Q=",
         "routeKey":"ANY /",
         "stage":"$default",
         "time":"09/Nov/2022:13:22:16 +0000",
         "timeEpoch":1668000136636
      },
      "isBase64Encoded":false
   }
}
```

Then check the logs for the Lambda function from the Lambda console.

<!-- BEGINNING OF PRE-COMMIT-TERRAFORM DOCS HOOK -->
## Requirements

| Name | Version |
|------|---------|
| <a name="requirement_terraform"></a> [terraform](#requirement\_terraform) | >= 1.0 |
| <a name="requirement_aws"></a> [aws](#requirement\_aws) | >= 4.9 |
| <a name="requirement_random"></a> [random](#requirement\_random) | >= 2.0 |

## Providers

| Name | Version |
|------|---------|
| <a name="provider_random"></a> [random](#provider\_random) | >= 2.0 |

## Modules

| Name | Source | Version |
|------|--------|---------|
| <a name="module_api_gateway"></a> [api\_gateway](#module\_api\_gateway) | terraform-aws-modules/apigateway-v2/aws | ~> 2.0 |
| <a name="module_lambda_function"></a> [lambda\_function](#module\_lambda\_function) | terraform-aws-modules/lambda/aws | ~> 4.0 |

## Resources

| Name | Type |
|------|------|
| [random_pet.this](https://registry.terraform.io/providers/hashicorp/random/latest/docs/resources/pet) | resource |

## Inputs

No inputs.

## Outputs

| Name | Description |
|------|-------------|
| <a name="output_apigatewayv2_api_api_endpoint"></a> [apigatewayv2\_api\_api\_endpoint](#output\_apigatewayv2\_api\_api\_endpoint) | The URI of the API |
| <a name="output_lambda_function_arn"></a> [lambda\_function\_arn](#output\_lambda\_function\_arn) | The ARN of the Lambda Function |
| <a name="output_lambda_function_invoke_arn"></a> [lambda\_function\_invoke\_arn](#output\_lambda\_function\_invoke\_arn) | The Invoke ARN of the Lambda Function |
| <a name="output_lambda_function_name"></a> [lambda\_function\_name](#output\_lambda\_function\_name) | The name of the Lambda Function |
| <a name="output_lambda_function_qualified_arn"></a> [lambda\_function\_qualified\_arn](#output\_lambda\_function\_qualified\_arn) | The ARN identifying your Lambda Function Version |
| <a name="output_lambda_function_version"></a> [lambda\_function\_version](#output\_lambda\_function\_version) | Latest published version of Lambda Function |
| <a name="output_lambda_role_arn"></a> [lambda\_role\_arn](#output\_lambda\_role\_arn) | The ARN of the IAM role created for the Lambda Function |
<!-- END OF PRE-COMMIT-TERRAFORM DOCS HOOK -->
