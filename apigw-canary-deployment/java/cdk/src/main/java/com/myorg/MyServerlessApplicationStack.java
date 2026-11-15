package com.myorg;

import software.amazon.awscdk.*;
import software.amazon.awscdk.services.apigateway.*;
import software.amazon.awscdk.services.iam.ServicePrincipal;
import software.amazon.awscdk.services.lambda.Runtime;
import software.amazon.awscdk.services.lambda.*;
import software.amazon.awscdk.services.s3.assets.AssetOptions;
import software.constructs.Construct;

import java.util.Arrays;
import java.util.List;
import java.util.Map;

import static java.util.Collections.singletonList;
import static software.amazon.awscdk.BundlingOutput.ARCHIVED;

public class MyServerlessApplicationStack extends Stack {
    public MyServerlessApplicationStack(final Construct scope, final String id) {
        this(scope, id, null);
    }

    public Function deployDevLambda(){
        List<String> functionOnePackagingInstructions = Arrays.asList(
                "/bin/sh",
                "-c",
                "cd FunctionDev " +
                        "&& mvn clean install " +
                        "&& cp /asset-input/FunctionDev/target/myfunction.jar /asset-output/"
        );


        BundlingOptions.Builder builderOptions = BundlingOptions.builder()
                .command(functionOnePackagingInstructions)
                .image(Runtime.JAVA_11.getBundlingImage())
                .volumes(singletonList(
                        // Mount local .m2 repo to avoid download all the dependencies again inside the container
                        DockerVolume.builder()
                                .hostPath(System.getProperty("user.home") + "/.m2/")
                                .containerPath("/root/.m2/")
                                .build()
                ))
                .user("root")
                .outputType(ARCHIVED);

        Function lambdaFn = Function.Builder.create(this,"MyFunction")
                .currentVersionOptions(VersionOptions.builder().removalPolicy(RemovalPolicy.RETAIN).build())
                .runtime(Runtime.JAVA_11)
                .handler("com.example.MyFunction")
                .timeout(Duration.seconds(300))
                .code(Code.fromAsset("software/", AssetOptions.builder()
                        .bundling(builderOptions
                                .command(functionOnePackagingInstructions)
                                .build())

                        .build()))
                .build();
        return lambdaFn;
    }

    public Function deployProdLambda(){
        List<String> functionOnePackagingInstructions = Arrays.asList(
                "/bin/sh",
                "-c",
                "cd FunctionOne " +
                        "&& mvn clean install " +
                        "&& cp /asset-input/FunctionOne/target/myfunction.jar /asset-output/"
        );


        BundlingOptions.Builder builderOptions = BundlingOptions.builder()
                .command(functionOnePackagingInstructions)
                .image(Runtime.JAVA_11.getBundlingImage())
                .volumes(singletonList(
                        // Mount local .m2 repo to avoid download all the dependencies again inside the container
                        DockerVolume.builder()
                                .hostPath(System.getProperty("user.home") + "/.m2/")
                                .containerPath("/root/.m2/")
                                .build()
                ))
                .user("root")
                .outputType(ARCHIVED);

        Function lambdaFn = Function.Builder.create(this,"MyFunction")
                .currentVersionOptions(VersionOptions.builder().removalPolicy(RemovalPolicy.RETAIN).build())
                .runtime(Runtime.JAVA_11)
                .handler("com.example.MyFunction")
                .timeout(Duration.seconds(300))
                .code(Code.fromAsset("software/", AssetOptions.builder()
                        .bundling(builderOptions
                                .command(functionOnePackagingInstructions)
                                .build())
                        .build()))
                .build();


        return lambdaFn;
    }

    public MyServerlessApplicationStack(final Construct scope, final String id, final StackProps props) {
        super(scope, id, props);

        String env = (String)this.getNode().tryGetContext("env");

        Function lambdaFn=null;
        Version version=null;
        Alias alias = null;
        IAlias prodAlias=null;
        if("dev".equals(env)) {
            lambdaFn = deployDevLambda();
            version= lambdaFn.getCurrentVersion();
            version.applyRemovalPolicy(RemovalPolicy.RETAIN);
            alias=new Alias(this,"LambdaDevAlias", AliasProps.builder().aliasName("Dev").version(version).build());

            IVersion existingVersion = Version.fromVersionArn(this,"version",lambdaFn.getFunctionArn()+":1");
            prodAlias= new Alias(this,"LambdaProdAlias",AliasProps.builder().aliasName("Prod").version(existingVersion).build());
        }
        else {

            lambdaFn = deployProdLambda();
            version= lambdaFn.getCurrentVersion();
            alias=new Alias(this,"LambdaProdAlias", AliasProps.builder().aliasName("Prod").version(version).build());

        }




        RestApi api =
                RestApi.Builder.create(this, "RestApi")
                        .restApiName("RestApi Service")
                        .description("Rest Api Service for Canary Deployment Demo")
                        .endpointTypes(singletonList(EndpointType.REGIONAL))
                        .retainDeployments(Boolean.FALSE)
                       .deployOptions(StageOptions.builder().stageName("prod").variables(Map.of("lambdaAlias","Prod")).build())
                        .build();

        String StageUri= "arn:aws:apigateway:"+this.getRegion()+":lambda:path/2015-03-31/functions/"+lambdaFn.getFunctionArn()+":${stageVariables.lambdaAlias}/invocations";

        Integration integration = new Integration(IntegrationProps.builder().type(IntegrationType.AWS_PROXY)
                .integrationHttpMethod("POST")
                .uri(StageUri).build() );

        Method method=api.getRoot().addMethod("GET",integration);

        lambdaFn.addPermission("lambdaPermission", Permission.builder()
                .action("lambda:InvokeFunction")
                .principal(new ServicePrincipal("apigateway.amazonaws.com"))
                .sourceArn(method.getMethodArn()).build());

        Permission build = Permission.builder()
                .action("lambda:InvokeFunction")
                .principal(new ServicePrincipal("apigateway.amazonaws.com"))
                .sourceArn(method.getMethodArn())
                .build();



        alias.addPermission("lambdaPermission", build);
        if(prodAlias != null)
          prodAlias.addPermission("lambdaPermission",build);


        new CfnOutput(this,"LambdaFunction", CfnOutputProps.builder().exportName("MyLambdaFunction").value(lambdaFn.getFunctionArn()).build());
        new CfnOutput(this,"LambdaFunctionVersionArn", CfnOutputProps.builder().exportName("MyLambdaFunctionVersionArn").value(version.getFunctionArn()).build());
        new CfnOutput(this,"LambdaFunctionAlias", CfnOutputProps.builder().exportName("MyLambdaFunctionAlias").value(alias.getAliasName()).build());
        new CfnOutput(this,"ApigwId", CfnOutputProps.builder().exportName("MyAPIGWID").value(api.getRestApiId()).build());
        new CfnOutput(this,"MethodArn", CfnOutputProps.builder().exportName("MyMethodArn").value(method.getMethodArn()).build());

    }
}
