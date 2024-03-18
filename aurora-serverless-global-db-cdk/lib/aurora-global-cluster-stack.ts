import { Construct } from 'constructs';
import { StackProps, Stack } from 'aws-cdk-lib'
import { CfnGlobalCluster } from 'aws-cdk-lib/aws-rds';

export class AuroraGlobalClusterStack extends Stack {
    public readonly cfnGlobalCluster: CfnGlobalCluster;
    constructor(scope: Construct, id: string, props?: StackProps) {
        super(scope, id, props);

        // Aurora Global Cluster
        const cfnGlobalCluster = new CfnGlobalCluster(this, 'AuroraGlobalCluster', {
            engine: 'aurora-postgresql',
            engineVersion: '14.6',
            globalClusterIdentifier: 'aurora-serverless-global-cluster',
        });

        this.cfnGlobalCluster = cfnGlobalCluster;
    }
}

export interface GlobalClusterProps extends StackProps {
    cfnGlobalCluster: CfnGlobalCluster,
    isPrimary?: boolean
}