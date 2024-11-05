package com.example.flashcards;

import com.fasterxml.jackson.core.type.TypeReference;
import com.fasterxml.jackson.databind.ObjectMapper;
import lombok.Builder;
import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import software.amazon.awscdk.App;
import software.amazon.awscdk.StackProps;
import software.amazon.awscdk.assertions.Template;

import java.io.File;
import java.io.IOException;
import java.util.Map;
import java.util.Objects;
import java.util.Optional;
import java.util.function.BooleanSupplier;

import static org.junit.jupiter.api.Assertions.assertTrue;
import static software.amazon.awscdk.assertions.Template.fromStack;

public class FlashcardsInfraTest {

    private static final String EXPECTED_PATH = "src/test/resources/expected/";
    private static final ObjectMapper OBJECT_MAPPER = new ObjectMapper();
    private static Template template;

    @Builder(setterPrefix = "with", builderClassName = "TestSupplierBuilder")
    record TestSupplier(String fileName, String resourceType) implements BooleanSupplier {
        @Override
        public boolean getAsBoolean() {
            try {
                var expected = OBJECT_MAPPER.readValue(new File(EXPECTED_PATH + fileName), new TypeReference<>() {
                });
                var actual = template.findResources(resourceType, null);
                // Removing the Metadata item as it should not be used in the tests.
                actual.forEach(
                        (key, value) -> Optional.ofNullable(value)
                                .ifPresent(map -> map.remove("Metadata"))
                );
                // Removing the Code item for lambdas as it is changed frequently so it should not be used in the tests.
                if (resourceType.equals("AWS::Lambda::Function")) {
                    actual.forEach(
                            (key, value) -> Optional.ofNullable(value)
                                    .map(item -> item.get("Properties"))
                                    .filter(Map.class::isInstance)
                                    .map(Map.class::cast)
                                    .ifPresent(map -> map.remove("Code"))
                    );
                }
                return Objects.equals(expected, actual);
            } catch (IOException e) {
                return false;
            }
        }
    }

    @BeforeAll
    public static void setUp() {
        var app = new App();
        var stackProps = StackProps.builder().build();
        var flashcardsInfraStack = new FlashCardsInfraStack(app, "FlashcardsInfraStack", stackProps);
        template = fromStack(flashcardsInfraStack);
    }

    @Test
    @DisplayName("Test if the expected vpc is present in the resources of the stack.")
    public void testVpc() {
        assertTrue(
                TestSupplier.builder()
                        .withFileName("vpc.json")
                        .withResourceType("AWS::EC2::VPC")
                        .build()
        );
    }

    @Test
    @DisplayName("Test if the expected subnets are present in the resources of the stack.")
    public void testSubnets() {
        assertTrue(
                TestSupplier.builder()
                        .withFileName("subnets.json")
                        .withResourceType("AWS::EC2::Subnet")
                        .build()
        );
    }

    @Test
    @DisplayName("Test if the expected route tables are present in the resources of the stack.")
    public void testRouteTables() {
        assertTrue(
                TestSupplier.builder()
                        .withFileName("route-tables.json")
                        .withResourceType("AWS::EC2::RouteTable")
                        .build()
        );
    }

    @Test
    @DisplayName("Test if the expected subnet route table associations are present in the resources of the stack.")
    public void testSubnetRouteTableAssociations() {
        assertTrue(
                TestSupplier.builder()
                        .withFileName("subnet-route-table-associations.json")
                        .withResourceType("AWS::EC2::SubnetRouteTableAssociation")
                        .build()
        );
    }

    @Test
    @DisplayName("Test if the expected routes are present in the resources of the stack.")
    public void testRoutes() {
        assertTrue(
                TestSupplier.builder()
                        .withFileName("routes.json")
                        .withResourceType("AWS::EC2::Route")
                        .build()
        );
    }

    @Test
    @DisplayName("Test if the expected EIPs are present in the resources of the stack.")
    public void testEIPs() {
        assertTrue(
                TestSupplier.builder()
                        .withFileName("eips.json")
                        .withResourceType("AWS::EC2::EIP")
                        .build()
        );
    }

    @Test
    @DisplayName("Test if the expected NAT Gateways are present in the resources of the stack.")
    public void testNatGateways() {
        assertTrue(
                TestSupplier.builder()
                        .withFileName("nat-gateways.json")
                        .withResourceType("AWS::EC2::NatGateway")
                        .build()
        );
    }

    @Test
    @DisplayName("Test if the expected Internet Gateway is present in the resources of the stack.")
    public void testInternetGateway() {
        assertTrue(
                TestSupplier.builder()
                        .withFileName("internet-gateway.json")
                        .withResourceType("AWS::EC2::InternetGateway")
                        .build()
        );
    }

    @Test
    @DisplayName("Test if the expected vpc gateway attachment is present in the resources of the stack.")
    public void testVPCGatewayAttachment() {
        assertTrue(
                TestSupplier.builder()
                        .withFileName("vpc-gateway-attachment.json")
                        .withResourceType("AWS::EC2::VPCGatewayAttachment")
                        .build()
        );
    }

    @Test
    @DisplayName("Test if the expected security groups are present in the resources of the stack.")
    public void testSecurityGroups() {
        assertTrue(
                TestSupplier.builder()
                        .withFileName("security-groups.json")
                        .withResourceType("AWS::EC2::SecurityGroup")
                        .build()
        );
    }

    @Test
    @DisplayName("Test if the expected secret is present in the resources of the stack.")
    public void testSecret() {
        assertTrue(
                TestSupplier.builder()
                        .withFileName("secret.json")
                        .withResourceType("AWS::SecretsManager::Secret")
                        .build()
        );
    }

    @Test
    @DisplayName("Test if the expected secret target attachment is present in the resources of the stack.")
    public void testSecretTargetAttachment() {
        assertTrue(
                TestSupplier.builder()
                        .withFileName("secret-target-attachment.json")
                        .withResourceType("AWS::SecretsManager::SecretTargetAttachment")
                        .build()
        );
    }

    @Test
    @DisplayName("Test if the expected database subnet group is present in the resources of the stack.")
    public void testDatabaseSubnetGroup() {
        assertTrue(
                TestSupplier.builder()
                        .withFileName("database-subnet-group.json")
                        .withResourceType("AWS::RDS::DBSubnetGroup")
                        .build()
        );
    }

    @Test
    @DisplayName("Test if the expected database instance is present in the resources of the stack.")
    public void testDatabaseInstance() {
        assertTrue(
                TestSupplier.builder()
                        .withFileName("database-instance.json")
                        .withResourceType("AWS::RDS::DBInstance")
                        .build()
        );
    }

    @Test
    @DisplayName("Test if the expected roles are present in the resources of the stack.")
    public void testRole() {
        assertTrue(
                TestSupplier.builder()
                        .withFileName("roles.json")
                        .withResourceType("AWS::IAM::Role")
                        .build()
        );
    }

    @Test
    @DisplayName("Test if the expected lambda functions are present in the resources of the stack.")
    public void testFunctions() {
        assertTrue(
                TestSupplier.builder()
                        .withFileName("functions.json")
                        .withResourceType("AWS::Lambda::Function")
                        .build()
        );
    }

    @Test
    @DisplayName("Test if the expected lambda function permission is present in the resources of the stack.")
    public void testPermission() {
        assertTrue(
                TestSupplier.builder()
                        .withFileName("permission.json")
                        .withResourceType("AWS::Lambda::Permission")
                        .build()
        );
    }

    @Test
    @DisplayName("Test if the expected lambda function url is present in the resources of the stack.")
    public void testURL() {
        assertTrue(
                TestSupplier.builder()
                        .withFileName("url.json")
                        .withResourceType("AWS::Lambda::Url")
                        .build()
        );
    }

    @Test
    @DisplayName("Test if the expected S3 bucket is present in the resources of the stack.")
    public void testBucket() {
        assertTrue(
                TestSupplier.builder()
                        .withFileName("bucket.json")
                        .withResourceType("AWS::S3::Bucket")
                        .build()
        );
    }

    @Test
    @DisplayName("Test if the expected CloudFront OAI is present in the resources of the stack.")
    public void testOAI() {
        assertTrue(
                TestSupplier.builder()
                        .withFileName("oai.json")
                        .withResourceType("AWS::CloudFront::CloudFrontOriginAccessIdentity")
                        .build()
        );
    }

    @Test
    @DisplayName("Test if the expected CloudFront distribution is present in the resources of the stack.")
    public void testDistribution() {
        assertTrue(
                TestSupplier.builder()
                        .withFileName("distribution.json")
                        .withResourceType("AWS::CloudFront::Distribution")
                        .build()
        );
    }
}