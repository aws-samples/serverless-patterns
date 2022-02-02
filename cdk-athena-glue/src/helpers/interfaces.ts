import { StackProps  } from '@aws-cdk/core';
import { IBucket  } from '@aws-cdk/aws-s3';
import { IDatabase } from '@aws-cdk/aws-glue';
import { CfnNamedQuery } from '@aws-cdk/aws-athena';

export interface s3BucketProps extends StackProps {
    s3EmpMaster: IBucket,
}

export interface glueProps extends StackProps {
    gDB: IDatabase,
    s3aQuery: IBucket,
}
