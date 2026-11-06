#!/usr/bin/env node
// Copyright 2026 Amazon.com, Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: MIT-0

import "source-map-support/register";
import * as cdk from "aws-cdk-lib";
import { StrandsDeciderConfidenceGatedTriageStack } from "../lib/strands-decider-confidence-gated-triage-stack";

const description = "Sample app (uksb-1tthgi812) (tag:sfn-sagemaker-sqs-sns-typescript-cdk)";
const app = new cdk.App();
new StrandsDeciderConfidenceGatedTriageStack(app, "StrandsDeciderConfidenceGatedTriageStack", { description });
