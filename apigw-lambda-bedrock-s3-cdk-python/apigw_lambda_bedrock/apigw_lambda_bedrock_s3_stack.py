from aws_cdk import (
    Stack,
    aws_lambda as _lambda,
    aws_iam as iam,
    Duration,
    aws_apigateway as apigw,
    aws_s3 as s3,
    RemovalPolicy,
    CfnOutput
)
from constructs import Construct

class ApigwLambdaBedrockS3Stack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)


        #add policy to invoke bedrock model
        invoke_model_policy = iam.Policy(self, "InvokeModelPolicy",
            statements=[
                iam.PolicyStatement(
                    actions=["bedrock:InvokeModel"],
                    resources=[f"arn:aws:bedrock:{self.region}::foundation-model/stability.stable-diffusion-xl-v1"]
                )
            ]
        )

        #create S3 bucket to store images
        my_bucket = s3.Bucket(
            self, 
            "ImageBucket",
            versioned=True,
            removal_policy=RemovalPolicy.DESTROY,
             auto_delete_objects=True # This will delete the bucket on stack deletion
            )
        
        PIL_layer = _lambda.LayerVersion.from_layer_version_arn(self, "PIL_Layer",'arn:aws:lambda:us-east-1:770693421928:layer:Klayers-p311-Pillow:2')
        boto_layer = _lambda.LayerVersion.from_layer_version_arn(self, "Boto3Layer", 'arn:aws:lambda:us-east-1:770693421928:layer:Klayers-p311-boto3:5')
        # Create the Lambda function and attach the layer
        lambda_function = _lambda.Function(self, "MyFunction",
            runtime=_lambda.Runtime.PYTHON_3_11,
            handler="index.handler",
            code=_lambda.Code.from_asset("./function_code"),
            layers=[PIL_layer,boto_layer],
            timeout=Duration.seconds(30),
            environment={"BUCKET": my_bucket.bucket_name}
            )

        my_bucket.grant_put(lambda_function)

        invoke_model_policy.attach_to_role(lambda_function.role)

        #create api gateway
        api = apigw.RestApi(self, "ServerlessLandGenAI",)

        #create a new resource
        image_gen_resource = api.root.add_resource("image_gen")
        image_gen_resource.add_method("POST", apigw.LambdaIntegration(lambda_function))

        CfnOutput(self, "S3-Generation-Bucket", value=my_bucket.bucket_name)
