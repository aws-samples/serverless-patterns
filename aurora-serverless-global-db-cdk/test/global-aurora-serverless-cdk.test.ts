import { App } from 'aws-cdk-lib';
import { Template } from 'aws-cdk-lib/assertions';
import { AuroraGlobalClusterStack } from '../lib/aurora-global-cluster-stack';
import { AuroraRegionalClusterStack } from '../lib/aurora-regional-cluster-stack'

test('Validate Stack Resources', () => {
    const app = new App();
   
    const account = app.node.tryGetContext('account') || process.env.CDK_INTEG_ACCOUNT || process.env.CDK_DEFAULT_ACCOUNT;
    const primaryRegion = {account: account, region: 'eu-west-1'};
    const secondaryRegion = {account: account, region: 'eu-west-2'};

    const globalclusterstack = new AuroraGlobalClusterStack(app, "AuroraGlobalCluster", {
        env: primaryRegion
    });
    
    const primaryregionstack = new AuroraRegionalClusterStack(app, `AuroraPrimaryCluster-${primaryRegion.region}`, {
        env: primaryRegion, cfnGlobalCluster: globalclusterstack.cfnGlobalCluster, isPrimary: true
    });
      
    const secondaryregionstack = new AuroraRegionalClusterStack(app, `AuroraSecondaryCluster-${secondaryRegion.region}`, {
        env: secondaryRegion, cfnGlobalCluster: globalclusterstack.cfnGlobalCluster, isPrimary: false
    });
   
    const globalclustertemplate = Template.fromStack(globalclusterstack);
    const primarytemplate = Template.fromStack(primaryregionstack);
    const secondarytemplate = Template.fromStack(secondaryregionstack);

    globalclustertemplate.resourceCountIs('AWS::RDS::GlobalCluster', 1);
    
    primarytemplate.resourceCountIs('AWS::EC2::VPC', 1);
    primarytemplate.resourceCountIs('AWS::RDS::DBSubnetGroup', 1);
    primarytemplate.resourceCountIs('AWS::SecretsManager::Secret', 1);
    primarytemplate.resourceCountIs('AWS::RDS::DBCluster', 1);
    primarytemplate.resourceCountIs('AWS::RDS::DBInstance', 1);
    
    secondarytemplate.resourceCountIs('AWS::EC2::VPC', 1);
    secondarytemplate.resourceCountIs('AWS::RDS::DBSubnetGroup', 1);
    secondarytemplate.resourceCountIs('AWS::SecretsManager::Secret', 1);
    secondarytemplate.resourceCountIs('AWS::RDS::DBCluster', 1);
    secondarytemplate.resourceCountIs('AWS::RDS::DBInstance', 1);
});
