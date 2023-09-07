import { Duration, Stack, StackProps } from 'aws-cdk-lib';
import * as iam from 'aws-cdk-lib/aws-iam';
import * as lambda from 'aws-cdk-lib/aws-lambda';
import * as ec2 from 'aws-cdk-lib/aws-ec2';
import * as redis from 'aws-cdk-lib/aws-elasticache';
import { Construct } from 'constructs';

export class LambdaElasticacheIntegrationpatternCdkStack extends Stack {
  constructor(scope: Construct, id: string, props?: StackProps) {
    super(scope, id, props);
        // defines an AWS Lambda resource roles
        const lambdarole = new iam.Role(this,'lambda-vpc-execution-role',{
          assumedBy: new iam.ServicePrincipal('lambda.amazonaws.com'),
          description: 'Lambda execution role for accessing VPC',
          managedPolicies: [
              iam.ManagedPolicy.fromAwsManagedPolicyName(
                'service-role/AWSLambdaVPCAccessExecutionRole',
              ),
          ],
        });

      //get default or any private vpc 
      const defaultvpc = ec2.Vpc.fromLookup(this, 'ElastiCacheVPC', {
        vpcName: "Default", // can be configured where ElastiCache is deployed
        isDefault: true
      });

      //security group for lambda vpc access
      const lambdasecuritygroup = new ec2.SecurityGroup(this, 'LambdaVPC-SG',{
        vpc:defaultvpc, 
        allowAllOutbound: true,
        description: 'Security group for lambda to access Redis'
      });
      
      //get predefined securitygroup
      const redissecuritygroup = new ec2.SecurityGroup(this, 'Redis-SG',{
        vpc:defaultvpc, 
        allowAllOutbound: true,
        description: 'Security group for Redis'
      });
      redissecuritygroup.addIngressRule(
        ec2.Peer.securityGroupId(lambdasecuritygroup.securityGroupId),
        ec2.Port.tcp(6379),
      );


      // Get all public subnet ids, you can deploy it to privatesubnets as well
      const Subnets = defaultvpc.publicSubnets.map((subnet) => {
        return subnet.subnetId
      });

        // Create redis subnet group from subnet ids
      const redisSubnetGroup = new redis.CfnSubnetGroup(this, 'RedisSubnetGroup', {
        subnetIds: Subnets,
        description: "Subnet group for redis"
      });

      // Create Redis Cluster
    const redisCluster = new redis.CfnCacheCluster(this, 'RedisCluster', {
      autoMinorVersionUpgrade: true,
      cacheNodeType: 'cache.t2.small',
      engine: 'redis',
      numCacheNodes: 1,
      cacheSubnetGroupName: redisSubnetGroup.ref,
      clusterName: 'sample-redis' ,
      vpcSecurityGroupIds: [redissecuritygroup.securityGroupId]
    });
    
    // Define this redis cluster is depends on redis subnet group created first
    redisCluster.node.addDependency(redisSubnetGroup);

    // Lambda creation
    const redisaccess = new lambda.Function(this, 'Elasticache-RedisAccess', {
      runtime: lambda.Runtime.NODEJS_18_X,    // execution environment
      code: lambda.Code.fromAsset('lambda'),  // code loaded from "lambda" directory
      handler: 'index.handler',               // file is "index", function is "handler"
      role: lambdarole,
      vpc:defaultvpc,
      allowPublicSubnet: true,
      securityGroups: [lambdasecuritygroup],
      timeout: Duration.minutes(5),
      environment: {
        REDIS_PORT: redisCluster.attrRedisEndpointPort,
        REDIS_HOST: redisCluster.attrRedisEndpointAddress,
      }
    });
  }
}
