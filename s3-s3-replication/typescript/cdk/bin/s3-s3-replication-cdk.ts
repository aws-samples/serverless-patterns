#!/usr/bin/env node
import 'source-map-support/register';
import * as cdk from 'aws-cdk-lib';
import { S3S3ReplicationCdkStack } from '../lib/s3-s3-replication-cdk-stack';

const app = new cdk.App();
new S3S3ReplicationCdkStack(app, 'S3S3ReplicationCdkStack');