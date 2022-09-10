#!/usr/bin/env node
import 'source-map-support/register';
import * as cdk from 'aws-cdk-lib';
import { AlbLambdaCdkStack } from '../lib/alb-lambda-cdk-stack';

const app = new cdk.App();
new AlbLambdaCdkStack(app, 'AlbLambdaCdkStack');