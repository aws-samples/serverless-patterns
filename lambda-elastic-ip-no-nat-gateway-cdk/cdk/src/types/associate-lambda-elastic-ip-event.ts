export type AssociateLambdaElasticIpEvent = {
    vpcId: string;
    subnetId: string;
    securityGroupId: string;
    allocationId: string;
    staticIp: string;
    availabilityZone: string;
    functionName: string;
  };
