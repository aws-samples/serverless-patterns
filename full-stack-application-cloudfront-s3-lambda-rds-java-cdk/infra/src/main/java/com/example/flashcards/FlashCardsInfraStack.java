package com.example.flashcards;

import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;
import software.amazon.awscdk.*;
import software.amazon.awscdk.services.cloudfront.BehaviorOptions;
import software.amazon.awscdk.services.cloudfront.Distribution;
import software.amazon.awscdk.services.cloudfront.OriginAccessIdentity;
import software.amazon.awscdk.services.cloudfront.ViewerProtocolPolicy;
import software.amazon.awscdk.services.cloudfront.origins.S3BucketOrigin;
import software.amazon.awscdk.services.cloudfront.origins.S3BucketOriginWithOAIProps;
import software.amazon.awscdk.services.ec2.InstanceType;
import software.amazon.awscdk.services.ec2.*;
import software.amazon.awscdk.services.iam.PolicyStatement;
import software.amazon.awscdk.services.lambda.Runtime;
import software.amazon.awscdk.services.lambda.*;
import software.amazon.awscdk.services.rds.*;
import software.amazon.awscdk.services.s3.BlockPublicAccess;
import software.amazon.awscdk.services.s3.Bucket;
import software.amazon.awscdk.services.s3.assets.AssetOptions;
import software.amazon.awscdk.services.s3.deployment.BucketDeployment;
import software.amazon.awscdk.services.s3.deployment.Source;
import software.amazon.awscdk.services.secretsmanager.ISecret;
import software.constructs.Construct;

import java.util.List;
import java.util.Map;
import java.util.NoSuchElementException;
import java.util.Optional;

import static java.util.Collections.singletonList;
import static software.amazon.awscdk.BundlingOutput.ARCHIVED;

public class FlashCardsInfraStack extends Stack {

    private static final String DB_USER = "postgres";
    private static final Integer DB_PORT = 5432;
    private static final String DB_NAME = "flashcards";
    private static final String WEBSITE_INDEX_DOCUMENT = "index.html";

    @lombok.Builder
    private record Configuration(String host, Boolean mock) {
    }

    private IVpc createVPC() {
        return Vpc.Builder.create(this, "FlashcardsVPC")
                .vpcName("FlashcardsVPC")
                // If set to true then a lambda will be created to remove all inbound & outbound rules from the default security group.
                .restrictDefaultSecurityGroup(false)
                .build();
    }

    private SecurityGroup createLambdaSecurityGroup(IVpc vpc) {
        return SecurityGroup.Builder.create(this, "FlashcardsLambdaSecurityGroup")
                .securityGroupName("FlashcardsLambdaSecurityGroup")
                .vpc(vpc)
                .allowAllOutbound(true)
                .build();
    }

    private Credentials createDatabaseCredentials() {
        var databaseSecret = DatabaseSecret.Builder.create(this, "FlashcardsDatabaseSecret")
                .secretName("FlashcardsDatabaseSecret")
                .username(DB_USER)
                .build();
        return Credentials.fromSecret(databaseSecret);
    }

    private DatabaseInstance createDatabase(IVpc vpc, SecurityGroup lambdaSecurityGroup, Credentials databaseCredentials) {
        var postgresEngineProps = PostgresInstanceEngineProps.builder()
                .version(PostgresEngineVersion.VER_16_4)
                .build();
        var databaseSecurityGroup = SecurityGroup.Builder.create(this, "FlashcardsDatabaseSecurityGroup")
                .securityGroupName("FlashcardsDatabaseSecurityGroup")
                .vpc(vpc)
                .allowAllOutbound(false)
                .build();
        databaseSecurityGroup.addIngressRule(
                Peer.securityGroupId(lambdaSecurityGroup.getSecurityGroupId()),
                Port.tcp(DB_PORT),
                "Allow database traffic from the lambda function security group."
        );
        return DatabaseInstance.Builder.create(this, "FlashcardsDatabase")
                .engine(DatabaseInstanceEngine.postgres(postgresEngineProps))
                .vpc(vpc)
                .databaseName(DB_NAME)
                .port(DB_PORT)
                .instanceType(InstanceType.of(InstanceClass.T3, InstanceSize.MICRO))
                .allocatedStorage(20)
                .backupRetention(Duration.days(0))
                .monitoringInterval(Duration.seconds(0))
                .storageType(StorageType.GP2)
                .securityGroups(List.of(databaseSecurityGroup))
                .credentials(databaseCredentials)
                .vpcSubnets(SubnetSelection.builder()
                        .subnetType(SubnetType.PRIVATE_WITH_EGRESS)
                        .build())
                .removalPolicy(RemovalPolicy.DESTROY)
                .build();
    }

    private Function createLambda(IVpc vpc, SecurityGroup lambdaSecurityGroup, Credentials databaseCredentials, DatabaseInstance databaseInstance) {
        List<String> packagingInstructions = List.of(
                "/bin/sh",
                "-c",
                "mvn -e -q clean package && cp /asset-input/target/backend-1.0-SNAPSHOT.jar /asset-output/"
        );
        var builderOptions = BundlingOptions.builder()
                .command(packagingInstructions)
                .image(Runtime.JAVA_17.getBundlingImage())
                .volumes(
                        singletonList(
                                DockerVolume.builder()
                                        .hostPath(System.getProperty("user.home") + "/.m2/")
                                        .containerPath("/root/.m2/")
                                        .build()
                        ))
                .user("root")
                .outputType(ARCHIVED)
                .build();
        PolicyStatement secretsManagerPolicy = PolicyStatement.Builder.create()
                .actions(List.of("secretsmanager:GetSecretValue"))
                .resources(List.of("*"))
                .build();
        return Function.Builder.create(this, "FlashcardsLambdaFunction")
                .runtime(Runtime.JAVA_17)
                .initialPolicy(List.of(secretsManagerPolicy))
                .functionName("FlashcardsLambdaFunction")
                .memorySize(2048)
                .timeout(Duration.seconds(29))
                .code(
                        Code.fromAsset(
                                "../backend/",
                                AssetOptions.builder().bundling(builderOptions).build()
                        )
                )
                .handler("com.example.flashcards.FlashcardsLambdaApplication::handleRequest")
                .vpc(vpc)
                .securityGroups(List.of(lambdaSecurityGroup))
                .environment(Map.of(
                        "DB_ENDPOINT", getDatabaseEndpoint(databaseInstance),
                        "DB_NAME", DB_NAME,
                        "DB_USER", DB_USER,
                        "DB_PORT", DB_PORT.toString(),
                        "DB_CREDENTIALS_SECRET_NAME", getDatabaseCredentialsSecretName(databaseCredentials)
                ))
                .build();
    }

    private FunctionUrl createLambdaFunctionUrl(Alias lambdaFunctionAlias) {
        return FunctionUrl.Builder.create(this, "FlashcardsLambdaFunctionUrl")
                .function(lambdaFunctionAlias)
                .authType(FunctionUrlAuthType.NONE)
                .invokeMode(InvokeMode.BUFFERED)
                .cors(
                        FunctionUrlCorsOptions.builder()
                                .allowedOrigins(List.of("*"))
                                .allowedMethods(List.of(HttpMethod.GET))
                                .allowedHeaders(List.of("*"))
                                .build()
                )
                .build();
    }

    private Bucket createBucket(String url) {
        var flashcardsBucket = Bucket.Builder.create(this, "FlashcardsBucket")
                .websiteIndexDocument(WEBSITE_INDEX_DOCUMENT)
                // If set to DESTROY then if the S3 bucket is empty it will be deleted when the stack is destroyed.
                // As it is configured now the S3 bucket will remain after the stack is destroyed, and it has to be emptied and removed manually.
                .removalPolicy(RemovalPolicy.RETAIN)
                // If set to true then a lambda will be created to empty the S3 bucket so that it may be deleted when the stack is destroyed.
                // If so, the removal policy needs to be DESTROY.
                .autoDeleteObjects(false)
                .blockPublicAccess(BlockPublicAccess.BLOCK_ALL)
                .build();
        // This will also create a lambda that will be used to put the assets in the S3 bucket.
        BucketDeployment.Builder.create(this, "FlashcardsBucketDeployment")
                .sources(List.of(
                        Source.asset("../frontend/"),
                        Source.jsonData("config.json", createConfig(url))
                ))
                .destinationBucket(flashcardsBucket)
                .build();
        return flashcardsBucket;
    }

    private Distribution createDistribution(Bucket bucket) {
        var flashCardsOriginAccessIdentity = OriginAccessIdentity.Builder.create(this, "FlashCardsOriginAccessIdentity")
                .comment("OAI for accessing the flashcards frontend S3 bucket.")
                .build();
        bucket.grantRead(flashCardsOriginAccessIdentity.getGrantPrincipal());
        var flashchcardsS3BucketOriginWithOAIProps = S3BucketOriginWithOAIProps.builder()
                .originAccessIdentity(flashCardsOriginAccessIdentity)
                .build();
        var flashcardsS3BucketOrigin = S3BucketOrigin.withOriginAccessIdentity(bucket, flashchcardsS3BucketOriginWithOAIProps);
        return Distribution.Builder.create(this, "FlashcardsDistribution")
                .defaultBehavior(BehaviorOptions.builder()
                        .origin(flashcardsS3BucketOrigin)
                        .viewerProtocolPolicy(ViewerProtocolPolicy.REDIRECT_TO_HTTPS)
                        .build())
                .build();
    }

    private String getDatabaseEndpoint(DatabaseInstance databaseInstance) {
        return Optional.ofNullable(databaseInstance)
                .map(DatabaseInstance::getDbInstanceEndpointAddress)
                .orElseThrow(() -> new NoSuchElementException("Database endpoint is not available."));
    }

    private String getDatabaseCredentialsSecretName(Credentials databaseCredentials) {
        return Optional.ofNullable(databaseCredentials)
                .map(Credentials::getSecret)
                .map(ISecret::getSecretName)
                .orElseThrow(() -> new NoSuchElementException("Database credentials secret is not available."));
    }

    private JsonNode createConfig(String host) {
        return Optional.of(new ObjectMapper())
                .flatMap(
                        objectMapper -> Optional.of(Configuration.builder())
                                .flatMap(
                                        configurationBuilder -> Optional.ofNullable(host)
                                                .map(configurationBuilder::host)
                                ).map(configurationBuilder -> configurationBuilder.mock(false))
                                .map(Configuration.ConfigurationBuilder::build)
                                .map(objectMapper::<JsonNode>valueToTree)
                ).orElseThrow(() -> new NoSuchElementException("Unable to create the frontend config file. Frontend config file is not available."));
    }

    public FlashCardsInfraStack(final Construct scope, final String id, final StackProps props) {
        super(scope, id, props);
        var vpc = createVPC();
        var lambdaSecurityGroup = createLambdaSecurityGroup(vpc);
        var databaseCredentials = createDatabaseCredentials();
        var databaseInstance = createDatabase(vpc, lambdaSecurityGroup, databaseCredentials);
        var lambdaFunction = createLambda(vpc, lambdaSecurityGroup, databaseCredentials, databaseInstance);
        var lambdaFunctionAlias = Alias.Builder.create(this, "FlashcardsProdAlias")
                .aliasName("Prod")
                .version(lambdaFunction.getCurrentVersion())
                .build();
        var lambdaFunctionUrl = createLambdaFunctionUrl(lambdaFunctionAlias);
        var bucket = createBucket(lambdaFunctionUrl.getUrl());
        var distribution = createDistribution(bucket);
        CfnOutput.Builder.create(this, "FlashcardsLambdaFunctionUrlOutput")
                .value(lambdaFunctionUrl.getUrl())
                .description("The URL of the flashcards lambda function. This can be used to invoke the lambda with curl or postman.")
                .build();
        CfnOutput.Builder.create(this, "FlashcardsCloudFrontURLOutput")
                .value(distribution.getDistributionDomainName() + "/" + WEBSITE_INDEX_DOCUMENT)
                .description("The URL of the flashcards frontend CloudFront distribution. This can be used to access the frontend of the app from the browser.")
                .build();
    }
}