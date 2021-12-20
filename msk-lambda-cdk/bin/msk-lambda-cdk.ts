#!/usr/bin/env node
import * as cdk from '@aws-cdk/core';

import { MskLambdaCdkStack } from '../lib/msk-lambda-cdk-stack';

const app = new cdk.App();
new MskLambdaCdkStack(app, 'MskLambdaCdkStack');
