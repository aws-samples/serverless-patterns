import { StackProps  } from 'aws-cdk-lib';
import { IBucket  } from 'aws-cdk-lib/aws-s3';
import { IDatabase } from '@aws-cdk/aws-glue-alpha';
import { CfnNamedQuery } from 'aws-cdk-lib/aws-athena';

export interface s3BucketProps extends StackProps {
    s3EmpMaster: IBucket,
}

export interface glueProps extends StackProps {
    gDB: IDatabase,
    s3aQuery: IBucket,
}

export interface viewProps extends StackProps {
    vw_emp_roster: CfnNamedQuery,
    WG: string
}