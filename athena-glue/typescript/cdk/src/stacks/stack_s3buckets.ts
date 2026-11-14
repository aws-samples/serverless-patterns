import { RemovalPolicy, Stack, StackProps } from 'aws-cdk-lib';
import { Construct } from 'constructs';
import { BlockPublicAccess, Bucket, IBucket } from 'aws-cdk-lib/aws-s3';
import { config } from '../config';


export class S3GlueStack extends Stack {

    public readonly s3EmpMaster: IBucket;
    public readonly s3aQuery: IBucket;

    constructor(scope: Construct, id: string, props: StackProps) {
        super(scope, id, props);

        const s3EmpMaster = new Bucket(this, 'S3EmpMaster', {
            versioned: true,
            bucketName: config.s3EmpMaster,
            publicReadAccess: false,
            removalPolicy: RemovalPolicy.DESTROY,
            blockPublicAccess: BlockPublicAccess.BLOCK_ALL,
        });
        this.s3EmpMaster = s3EmpMaster;

        const queryResults = new Bucket(this, 'AthenaViewResults', {
            versioned: true,
            bucketName: config.queryBucketName,
            blockPublicAccess: BlockPublicAccess.BLOCK_ALL,
            publicReadAccess: false,
            removalPolicy: RemovalPolicy.DESTROY
        });
        this.s3aQuery = queryResults;

    }
}
