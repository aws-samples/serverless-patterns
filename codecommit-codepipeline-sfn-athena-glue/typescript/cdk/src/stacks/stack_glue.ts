import { Stack, StackProps } from 'aws-cdk-lib';
import { Construct } from 'constructs';
import { Schema, Database, Table, IDatabase, ITable, DataFormat } from '@aws-cdk/aws-glue-alpha';

import { config } from '../config';
import { s3BucketProps } from '../helpers/interfaces';

export class TestGlueStack extends Stack {

    public readonly gDB: IDatabase;
    public readonly empTable: ITable;
    public readonly empDetailTable: ITable;

    constructor(scope: Construct, id: string, props: s3BucketProps) {
        super(scope, id, props);

        const testDatabase = new Database(this, 'testDB', {
            databaseName: config.databaseName
        });

        const empTable = new Table(this, 'empMaster', {
            database: testDatabase,
            tableName: config.empMaster,
            columns: [
                {
                    name: 'emp_id',
                    type: Schema.INTEGER
                },
                {
                    name: 'emp_name',
                    type: Schema.STRING
                },
                {
                    name: 'emp_email',
                    type: Schema.STRING
                },
                {
                    name: 'emp_phone',
                    type: Schema.char(10)
                }
            ],
            bucket: props.s3EmpMaster,
            s3Prefix: 'emp',
            dataFormat: DataFormat.JSON
        });

        const empDetailTable = new Table(this, 'empDetails', {
            database: testDatabase,
            tableName: config.empDetails,
            columns: [
                {
                    name: 'emp_id',
                    type: Schema.INTEGER
                },
                {
                    name: 'emp_department',
                    type: Schema.STRING
                },
                {
                    name: 'emp_manager',
                    type: Schema.STRING
                },
            ],
            bucket: props.s3EmpMaster,
            s3Prefix: 'empDetails',
            dataFormat: DataFormat.JSON
        });

        this.empTable = empTable;
        this.empDetailTable = empDetailTable;
        this.gDB = testDatabase;
    }
}