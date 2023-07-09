#!/usr/bin/env node
import { App } from 'aws-cdk-lib';
import { EventBridgeCDKStateMachineStack } from '../lib/eventbridge-stepfunction-sqs-stack';

const app = new App();

new EventBridgeCDKStateMachineStack(app, 'EventBridgeCDKStateMachineStack', {});

