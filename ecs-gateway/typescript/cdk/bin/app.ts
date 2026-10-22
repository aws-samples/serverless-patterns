#!/usr/bin/env node
import * as cdk from 'aws-cdk-lib';
import { EcsGatewayStack } from '../lib/ecs-gateway-stack';

const app = new cdk.App();
new EcsGatewayStack(app, 'EcsGatewayStack');
