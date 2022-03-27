import { Stack, RemovalPolicy, Duration} from 'aws-cdk-lib';
import { Construct } from 'constructs';
import { CfnWorkGroup, CfnNamedQuery } from 'aws-cdk-lib/aws-athena';
import { AthenaStartQueryExecution, EncryptionOption } from 'aws-cdk-lib/aws-stepfunctions-tasks';
import { IntegrationPattern, StateMachine, IStateMachine, LogLevel} from 'aws-cdk-lib/aws-stepfunctions';

import * as fs from 'fs';
import * as path from 'path';
import { config } from '../config';
import { glueProps } from '../helpers/interfaces';

export class AthenaStack extends Stack {

    public readonly WG: string;
    public readonly vw_emp_roster: CfnNamedQuery;
    public readonly sViewsMachine: IStateMachine;

    constructor(scope: Construct, id: string, props: glueProps) {
        super(scope, id, props);

        const workgroup = new CfnWorkGroup(this, 'WorkGroup', {
            name: config.workgroupName,
            description: 'workfroup for creating Views',
            state: 'ENABLED',
            workGroupConfiguration: {
                publishCloudWatchMetricsEnabled: true,
                enforceWorkGroupConfiguration: true,
                requesterPaysEnabled: true,
                bytesScannedCutoffPerQuery: 11000000,
                resultConfiguration: {
                    outputLocation: `s3://${props.s3aQuery.bucketName}`,
                },
            },
        });
        workgroup.applyRemovalPolicy(RemovalPolicy.DESTROY);
        this.WG = workgroup.name;

        const empRoster = new CfnNamedQuery(this, 'empRoster', {
            database: props.gDB.databaseName,
            queryString: fs.readFileSync(path.join(__dirname, '../glue/view.sql')).toString().trim(),
            description: 'Emp Details view',
            name: 'empDetails',
            workGroup: workgroup.name,
        });
        empRoster.addDependsOn(workgroup);

        this.vw_emp_roster = empRoster;
        this.WG = workgroup.name;

        const queryEmpViewTask = new AthenaStartQueryExecution(this, 'queryEmpView', {
            queryString: empRoster.queryString,
            queryExecutionContext: {
              databaseName: props.gDB.databaseName
            },
            resultConfiguration: {
              outputLocation: {
                bucketName: props.s3aQuery.bucketName,
                objectKey: 'v_'
              },
            },
            workGroup: workgroup.name,
            integrationPattern: IntegrationPattern.RUN_JOB,
        });

        const definition = queryEmpViewTask;
        const sViewsFlow = new StateMachine(this, 'AthenaViewsFlow', {
            definition,
            stateMachineName: 'test-QueryFlows',
            timeout: Duration.minutes(5)
        });

        props.s3aQuery.grantReadWrite(sViewsFlow);
        this.sViewsMachine = sViewsFlow;
    }
}