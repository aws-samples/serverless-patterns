#!/usr/bin/env node
import * as cdk from 'aws-cdk-lib';
import { SecretsManagerPostQuantumTlsStack } from '../lib/secretsmanager-post-quantum-tls-stack';

const app = new cdk.App();
new SecretsManagerPostQuantumTlsStack(app, 'SecretsManagerPostQuantumTlsStack');
