#!/usr/bin/env node
import 'source-map-support/register';
import * as cdk from 'aws-cdk-lib';
import { AsyncFunctionsStack } from '../lib/async-functions';

const app = new cdk.App();
new AsyncFunctionsStack(app, 'AsyncFunctionStack', {});
