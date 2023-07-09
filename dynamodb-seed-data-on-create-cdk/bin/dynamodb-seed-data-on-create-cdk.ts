#!/usr/bin/env node
import 'source-map-support/register';
import * as cdk from 'aws-cdk-lib';
import { DynamodbSeedDataOnCreateCdkStack } from '../lib/dynamodb-seed-data-on-create-cdk-stack';

const app = new cdk.App();
new DynamodbSeedDataOnCreateCdkStack(app, 'DynamodbSeedDataOnCreateCdkStack');