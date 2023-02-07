#!/usr/bin/env node
import 'source-map-support/register';
import * as cdk from 'aws-cdk-lib';
import { MessageTranslatorStack } from '../lib/message-translator-stack';

const app = new cdk.App();
new MessageTranslatorStack(app, 'MessageTranslatorStack');
