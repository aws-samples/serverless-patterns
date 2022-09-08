/*! Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
 *  SPDX-License-Identifier: MIT-0
 */

import { Construct } from 'constructs'
import { NestedStack, NestedStackProps, RemovalPolicy } from 'aws-cdk-lib'
import { Table,BillingMode,AttributeType } from 'aws-cdk-lib/aws-dynamodb'
import * as Config from '../config.json'

export class DynamoDB extends NestedStack {
    public readonly iotDDB: Table

    constructor(scope: Construct, id: string, props?: NestedStackProps) {
        super(scope, id, props)

        this.iotDDB = new Table(this, 'garage-historical-data', {
            partitionKey: { name: 'macId', type: AttributeType.STRING },
            sortKey: { name: 'timestamp', type: AttributeType.NUMBER },
            billingMode: BillingMode.PROVISIONED,
            removalPolicy: RemovalPolicy.DESTROY,
            tableName: Config.dynamodb.tableName,
            timeToLiveAttribute: "ttl"
        })

    }
}
