using System.Collections.Generic;
using System.Text.Json;
using Pulumi;
using Aws = Pulumi.Aws;
using Awsx = Pulumi.Awsx;

return await Deployment.RunAsync(() => 
{
    var vpc = new Awsx.Ec2.Vpc("vpc", new()
    {
        CidrBlock = "10.0.0.0/16",
        NumberOfAvailabilityZones = 2,
        SubnetSpecs = new List<Awsx.Ec2.Inputs.SubnetSpecArgs>
        {
            new Awsx.Ec2.Inputs.SubnetSpecArgs
            {
                Type = Awsx.Ec2.SubnetType.Public,
                Name = "public-lb-subnet",
            },
        },
        NatGateways = new Awsx.Ec2.Inputs.NatGatewayConfigurationArgs
        {
            Strategy = Awsx.Ec2.NatGatewayStrategy.None,
        },
    });

    var securityGroup = new Aws.Ec2.SecurityGroup("securityGroup", new()
    {
        VpcId = vpc.VpcId,
        Ingress = new[]
        {
            new Aws.Ec2.Inputs.SecurityGroupIngressArgs
            {
                Protocol = "tcp",
                FromPort = 80,
                ToPort = 80,
                CidrBlocks = new[]
                {
                    "0.0.0.0/0",
                },
            },
        },
    });

    var loadBalancer = new Aws.LB.LoadBalancer("loadBalancer", new()
    {
        SecurityGroups = new[]
        {
            securityGroup.Id,
        },
        Subnets = vpc.PublicSubnetIds,
    });

    var targetGroup = new Aws.LB.TargetGroup("targetGroup", new()
    {
        TargetType = "lambda",
        VpcId = vpc.VpcId,
    });

    var listener = new Aws.LB.Listener("listener", new()
    {
        LoadBalancerArn = loadBalancer.Arn,
        Port = 80,
        DefaultActions = new[]
        {
            new Aws.LB.Inputs.ListenerDefaultActionArgs
            {
                Type = "forward",
                TargetGroupArn = targetGroup.Arn,
            },
        },
    });

    var lambdaRole = new Aws.Iam.Role("lambdaRole", new()
    {
        AssumeRolePolicy = JsonSerializer.Serialize(new Dictionary<string, object?>
        {
            ["Version"] = "2012-10-17",
            ["Statement"] = new[]
            {
                new Dictionary<string, object?>
                {
                    ["Action"] = "sts:AssumeRole",
                    ["Effect"] = "Allow",
                    ["Principal"] = new Dictionary<string, object?>
                    {
                        ["Service"] = "lambda.amazonaws.com",
                    },
                },
            },
        }),
        ManagedPolicyArns = new[]
        {
            "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole",
        },
    });

    var fn = new Aws.Lambda.Function("fn", new()
    {
        Runtime = "nodejs18.x",
        Handler = "index.handler",
        Role = lambdaRole.Arn,
        Code = new FileArchive("./lambda"),
    });

    var lambdaPermission = new Aws.Lambda.Permission("lambdaPermission", new()
    {
        Action = "lambda:InvokeFunction",
        Principal = "elasticloadbalancing.amazonaws.com",
        Function = fn.Arn,
        SourceArn = targetGroup.Arn,
    });

    var targetGroupAttachment = new Aws.LB.TargetGroupAttachment("targetGroupAttachment", new()
    {
        TargetGroupArn = targetGroup.Arn,
        TargetId = fn.Arn,
    }, new CustomResourceOptions
    {
        DependsOn = {lambdaPermission}
    });

    return new Dictionary<string, object?>
    {
        ["url"] = loadBalancer.DnsName,
    };
});

