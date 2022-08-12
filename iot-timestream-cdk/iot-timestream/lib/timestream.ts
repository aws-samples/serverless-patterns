/*! Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
 *  SPDX-License-Identifier: MIT-0
 */

import { Construct } from 'constructs'
import { NestedStack, NestedStackProps, RemovalPolicy } from 'aws-cdk-lib'
import { CfnDatabase, CfnTable } from 'aws-cdk-lib/aws-timestream'
import * as Config from '../config.json'

export class Timestream extends NestedStack {
    public readonly tstrm_database: CfnDatabase
    public readonly tstrm_table: CfnTable

    constructor(scope: Construct, id: string, props?: NestedStackProps) {
        super(scope, id, props)

        this.tstrm_database = new CfnDatabase(this, 'iotTimestreamDB', {
            databaseName: Config.timestream.databaseName
        })

        this.tstrm_table = new CfnTable(this, 'iotTimestreamTbl', {
            tableName: Config.timestream.tableName,
            databaseName: Config.timestream.databaseName,
            retentionProperties: {
                memoryStoreRetentionPeriodInHours: (24*7).toString(10),
                magneticStoreRetentionPeriodInDays: (365*2).toString(10)
            }
        })

        this.tstrm_table.applyRemovalPolicy(RemovalPolicy.DESTROY)
        this.tstrm_database.applyRemovalPolicy(RemovalPolicy.DESTROY)



    }
}

