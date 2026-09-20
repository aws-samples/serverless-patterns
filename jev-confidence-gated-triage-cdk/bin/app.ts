#!/usr/bin/env node
// Copyright 2026 Amazon.com, Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: MIT-0

import "source-map-support/register";
import * as cdk from "aws-cdk-lib";
import { JevConfidenceGatedTriageStack } from "../lib/jev-confidence-gated-triage-stack";

const description = "Sample app (uksb-1tthgi812) (tag:jev-confidence-gated-triage-cdk)";
const app = new cdk.App();
new JevConfidenceGatedTriageStack(app, "JevConfidenceGatedTriageStack", { description });
