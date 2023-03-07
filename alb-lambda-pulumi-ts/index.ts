import * as aws from "@pulumi/aws";
import * as awsx from "@pulumi/awsx";
import * as lambda from "./lambda";

const vpc = new awsx.ec2.Vpc("vpc", {
    cidrBlock: "10.0.0.0/16",
    numberOfAvailabilityZones: 2,
    subnetSpecs: [{
        type: awsx.ec2.SubnetType.Public,
        name: "public-ecs-subnet",
    }],
    natGateways: {
        strategy: "None"
    }
});

const securityGroup = new aws.ec2.SecurityGroup("loadBalancerSg", {
    vpcId: vpc.vpcId,
    ingress: [{
        protocol: "tcp",
        fromPort: 80,
        toPort: 80,
        cidrBlocks: ["0.0.0.0/0"]
    }]
});

const loadBalancer = new aws.lb.LoadBalancer("loadbalancer", {
    securityGroups: [securityGroup.id],
    subnets: vpc.publicSubnetIds
});

const targetGroup = new aws.lb.TargetGroup("targetGroup", {
    targetType: "lambda",
    vpcId: vpc.vpcId
}, {dependsOn: loadBalancer});

const listener = new aws.lb.Listener("listener", {
    loadBalancerArn: loadBalancer.arn,
    port: 80,
    defaultActions: [{
        type: "forward",
        targetGroupArn: targetGroup.arn
    }]
});

const lambdaFunction = new aws.lambda.CallbackFunction("lambdaFunction", {
    runtime: aws.lambda.Runtime.NodeJS18dX,
    callback: lambda.handler,
});

const lambdaPermission = new aws.lambda.Permission("permission", {
    action: "lambda:InvokeFunction",
    principal: "elasticloadbalancing.amazonaws.com",
    function: lambdaFunction.arn,
    sourceArn: targetGroup.arn
})

const targetGroupAttachment = new aws.lb.TargetGroupAttachment("targetGroupAttachment", {
    targetGroupArn: targetGroup.arn,
    targetId: lambdaFunction.arn
}, {dependsOn: [lambdaPermission]});

export const url = loadBalancer.dnsName;