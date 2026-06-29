// Copyright 2026 Amazon.com, Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: MIT-0

import * as cdk from 'aws-cdk-lib';
import { Construct } from 'constructs';
import * as lambda from 'aws-cdk-lib/aws-lambda';
import * as sfn from 'aws-cdk-lib/aws-stepfunctions';
import * as tasks from 'aws-cdk-lib/aws-stepfunctions-tasks';
import * as dynamodb from 'aws-cdk-lib/aws-dynamodb';
import * as iam from 'aws-cdk-lib/aws-iam';
import * as path from 'path';

export class SfnInvoicingBedrockChargebackStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    const modelId = this.node.tryGetContext('modelId') ||
      'us.anthropic.claude-sonnet-4-20250514-v1:0';

    // DynamoDB table for chargeback ledger
    const chargebackTable = new dynamodb.Table(this, 'ChargebackLedger', {
      partitionKey: { name: 'invoiceUnitId', type: dynamodb.AttributeType.STRING },
      sortKey: { name: 'period', type: dynamodb.AttributeType.STRING },
      billingMode: dynamodb.BillingMode.PAY_PER_REQUEST,
      removalPolicy: cdk.RemovalPolicy.DESTROY,
    });

    // Lambda: List Invoice Units
    const listUnitsFn = new lambda.Function(this, 'ListInvoiceUnits', {
      runtime: lambda.Runtime.PYTHON_3_12,
      handler: 'list_units.handler',
      code: lambda.Code.fromAsset(path.join(__dirname, '..', '..', 'src')),
      timeout: cdk.Duration.seconds(30),
      memorySize: 256,
    });

    listUnitsFn.addToRolePolicy(new iam.PolicyStatement({
      actions: ['invoicing:ListInvoiceUnits'],
      resources: ['*'], // Invoicing API does not support resource-level permissions
    }));

    // Lambda: Fetch Invoices per Unit
    const fetchInvoicesFn = new lambda.Function(this, 'FetchInvoices', {
      runtime: lambda.Runtime.PYTHON_3_12,
      handler: 'fetch_invoices.handler',
      code: lambda.Code.fromAsset(path.join(__dirname, '..', '..', 'src')),
      timeout: cdk.Duration.seconds(60),
      memorySize: 256,
    });

    fetchInvoicesFn.addToRolePolicy(new iam.PolicyStatement({
      actions: ['invoicing:ListInvoiceSummaries', 'sts:GetCallerIdentity'],
      resources: ['*'], // Invoicing API does not support resource-level permissions
    }));

    // Lambda: Bedrock Analysis + DynamoDB write
    const analysisFn = new lambda.Function(this, 'BedrockAnalysis', {
      runtime: lambda.Runtime.PYTHON_3_12,
      handler: 'analysis.handler',
      code: lambda.Code.fromAsset(path.join(__dirname, '..', '..', 'src')),
      timeout: cdk.Duration.seconds(120),
      memorySize: 512,
      environment: {
        MODEL_ID: modelId,
        TABLE_NAME: chargebackTable.tableName,
      },
    });

    analysisFn.addToRolePolicy(new iam.PolicyStatement({
      actions: ['bedrock:InvokeModel'],
      resources: [
        `arn:aws:bedrock:${this.region}:${this.account}:inference-profile/${modelId}`,
        'arn:aws:bedrock:*::foundation-model/*',
      ],
    }));

    chargebackTable.grantWriteData(analysisFn);

    // Step Functions definition
    const listUnitsTask = new tasks.LambdaInvoke(this, 'ListUnitsTask', {
      lambdaFunction: listUnitsFn,
      outputPath: '$.Payload',
    });

    const fetchInvoicesTask = new tasks.LambdaInvoke(this, 'FetchInvoicesTask', {
      lambdaFunction: fetchInvoicesFn,
      outputPath: '$.Payload',
    });

    const analysisTask = new tasks.LambdaInvoke(this, 'AnalysisTask', {
      lambdaFunction: analysisFn,
      outputPath: '$.Payload',
    });

    // Map state: iterate over each invoice unit in parallel
    const mapState = new sfn.Map(this, 'ProcessEachUnit', {
      itemsPath: '$.units',
      maxConcurrency: 5,
    });

    mapState.itemProcessor(
      fetchInvoicesTask.next(analysisTask)
    );

    const definition = listUnitsTask.next(mapState);

    const stateMachine = new sfn.StateMachine(this, 'InvoiceReconciliation', {
      definitionBody: sfn.DefinitionBody.fromChainable(definition),
      timeout: cdk.Duration.minutes(15),
    });

    // Outputs
    new cdk.CfnOutput(this, 'StateMachineArn', {
      value: stateMachine.stateMachineArn,
    });

    new cdk.CfnOutput(this, 'ChargebackTableName', {
      value: chargebackTable.tableName,
    });
  }
}
