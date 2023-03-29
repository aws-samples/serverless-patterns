package main

import (
	"encoding/json"

	"github.com/pulumi/pulumi-aws/sdk/v5/go/aws/ec2"
	"github.com/pulumi/pulumi-aws/sdk/v5/go/aws/iam"
	"github.com/pulumi/pulumi-aws/sdk/v5/go/aws/lambda"
	"github.com/pulumi/pulumi-aws/sdk/v5/go/aws/lb"
	awsxEc2 "github.com/pulumi/pulumi-awsx/sdk/go/awsx/ec2"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		vpc, err := awsxEc2.NewVpc(ctx, "vpc", &awsxEc2.VpcArgs{
			CidrBlock:                 pulumi.StringRef("10.0.0.0/16"),
			NumberOfAvailabilityZones: pulumi.IntRef(2),
			SubnetSpecs: []awsxEc2.SubnetSpecArgs{
				{
					Type: awsxEc2.SubnetTypePublic,
					Name: pulumi.StringRef("public-lb-subnet"),
				},
			},
			NatGateways: &awsxEc2.NatGatewayConfigurationArgs{
				Strategy: awsxEc2.NatGatewayStrategyNone,
			},
		})
		if err != nil {
			return err
		}
		securityGroup, err := ec2.NewSecurityGroup(ctx, "securityGroup", &ec2.SecurityGroupArgs{
			VpcId: vpc.VpcId,
			Ingress: ec2.SecurityGroupIngressArray{
				&ec2.SecurityGroupIngressArgs{
					Protocol: pulumi.String("tcp"),
					FromPort: pulumi.Int(80),
					ToPort:   pulumi.Int(80),
					CidrBlocks: pulumi.StringArray{
						pulumi.String("0.0.0.0/0"),
					},
				},
			},
		})
		if err != nil {
			return err
		}
		loadBalancer, err := lb.NewLoadBalancer(ctx, "loadBalancer", &lb.LoadBalancerArgs{
			SecurityGroups: pulumi.StringArray{
				securityGroup.ID(),
			},
			Subnets: vpc.PublicSubnetIds,
		})
		if err != nil {
			return err
		}
		targetGroup, err := lb.NewTargetGroup(ctx, "targetGroup", &lb.TargetGroupArgs{
			TargetType: pulumi.String("lambda"),
			VpcId:      vpc.VpcId,
		})
		if err != nil {
			return err
		}
		_, err = lb.NewListener(ctx, "listener", &lb.ListenerArgs{
			LoadBalancerArn: loadBalancer.Arn,
			Port:            pulumi.Int(80),
			DefaultActions: lb.ListenerDefaultActionArray{
				&lb.ListenerDefaultActionArgs{
					Type:           pulumi.String("forward"),
					TargetGroupArn: targetGroup.Arn,
				},
			},
		})
		if err != nil {
			return err
		}
		tmpJSON0, err := json.Marshal(map[string]interface{}{
			"Version": "2012-10-17",
			"Statement": []map[string]interface{}{
				{
					"Action": "sts:AssumeRole",
					"Effect": "Allow",
					"Principal": map[string]interface{}{
						"Service": "lambda.amazonaws.com",
					},
				},
			},
		})
		if err != nil {
			return err
		}
		json0 := string(tmpJSON0)
		lambdaRole, err := iam.NewRole(ctx, "lambdaRole", &iam.RoleArgs{
			AssumeRolePolicy: pulumi.String(json0),
			ManagedPolicyArns: pulumi.StringArray{
				pulumi.String("arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"),
			},
		})
		if err != nil {
			return err
		}
		fn, err := lambda.NewFunction(ctx, "fn", &lambda.FunctionArgs{
			Runtime: pulumi.String("nodejs18.x"),
			Handler: pulumi.String("index.handler"),
			Role:    lambdaRole.Arn,
			Code:    pulumi.NewFileArchive("./lambda"),
		})
		if err != nil {
			return err
		}
		lambdaPermission, err := lambda.NewPermission(ctx, "lambdaPermission", &lambda.PermissionArgs{
			Action:    pulumi.String("lambda:InvokeFunction"),
			Principal: pulumi.String("elasticloadbalancing.amazonaws.com"),
			Function:  fn.Arn,
			SourceArn: targetGroup.Arn,
		})
		if err != nil {
			return err
		}
		_, err = lb.NewTargetGroupAttachment(ctx, "targetGroupAttachment", &lb.TargetGroupAttachmentArgs{
			TargetGroupArn: targetGroup.Arn,
			TargetId:       fn.Arn,
		}, pulumi.DependsOn([]pulumi.Resource{lambdaPermission}))
		if err != nil {
			return err
		}
		ctx.Export("url", loadBalancer.DnsName)
		return nil
	})
}
