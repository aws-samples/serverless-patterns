import { App } from 'aws-cdk-lib';
import { AuroraGlobalClusterStack } from '../lib/aurora-global-cluster-stack';
import { AuroraRegionalClusterStack } from '../lib/aurora-regional-cluster-stack';
import { FargateTestAppStack } from '../lib/fargate-test-app-stack';

const app = new App();

const account = app.node.tryGetContext('account') || process.env.CDK_INTEG_ACCOUNT || process.env.CDK_DEFAULT_ACCOUNT;
const primaryRegion = { account: account, region: 'eu-west-1' };
const secondaryRegion = { account: account, region: 'eu-west-2' };

const globalCluster = new AuroraGlobalClusterStack(app, "aurora-global-cluster", {
    env: primaryRegion
});

const primaryclusterstack = new AuroraRegionalClusterStack(app, `primary-cluster`, {
    env: primaryRegion, cfnGlobalCluster: globalCluster.cfnGlobalCluster, isPrimary: true
});

const secondaryclusterstack = new AuroraRegionalClusterStack(app, `secondary-cluster`, {
    env: secondaryRegion, cfnGlobalCluster: globalCluster.cfnGlobalCluster, isPrimary: false
});

primaryclusterstack.addDependency(globalCluster);
secondaryclusterstack.addDependency(primaryclusterstack)

const primarytestappstack = new FargateTestAppStack(app, `primary-test-app`, {
    env: primaryRegion,
    endpoint: primaryclusterstack.endpoint,
    port: primaryclusterstack.port,
    vpc: primaryclusterstack.vpc,
    isPrimary: true,
    region: primaryclusterstack.region,
    dbSecurityGroupId: primaryclusterstack.dbSecurityGroupId
});

const secondarytestappstack = new FargateTestAppStack(app, `secondary-test-app`, {
    env: secondaryRegion,
    endpoint: secondaryclusterstack.endpoint,
    port: secondaryclusterstack.port,
    vpc: secondaryclusterstack.vpc,
    isPrimary: false,
    region: primaryclusterstack.region,
    dbSecurityGroupId: secondaryclusterstack.dbSecurityGroupId
});

primarytestappstack.addDependency(primaryclusterstack);
secondarytestappstack.addDependency(secondaryclusterstack);

app.synth();