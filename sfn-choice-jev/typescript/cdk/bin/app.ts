#!/usr/bin/env node
// Copyright 2026 Amazon.com, Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: MIT-0

import "source-map-support/register";
import * as cdk from "aws-cdk-lib";
import { SfnChoiceJevStack } from "../lib/sfn-choice-jev-stack";

const description = "Sample app (uksb-1tthgi812) (tag:sfn-choice-jev-typescript-cdk)";
const app = new cdk.App();
new SfnChoiceJevStack(app, "SfnChoiceJevStack", { description });
