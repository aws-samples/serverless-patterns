/*! Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
 *  SPDX-License-Identifier: MIT-0
 */

import { Construct } from 'constructs'
import { CfnOutput, NestedStack, NestedStackProps, RemovalPolicy } from 'aws-cdk-lib'
import { Bucket } from 'aws-cdk-lib/aws-s3'

export class S3Buckets extends NestedStack {
    public readonly kfh_bucket: Bucket

    constructor(scope: Construct, id: string, props?: NestedStackProps) {
        super(scope, id, props)

        // Amazon Kinesis Firehose Destination S3 bucket
        this.kfh_bucket = new Bucket(this, 'kfh-bucket', {
            removalPolicy: RemovalPolicy.DESTROY,
            autoDeleteObjects: true
        }) 

        new CfnOutput(this, 'KfhDataBucketName', { value: this.kfh_bucket.bucketName })
        new CfnOutput(this, 'KfhDataBucketArn', { value: this.kfh_bucket.bucketArn })

    }
}

