import { IFunction } from "aws-cdk-lib/aws-lambda";
import { Construct } from "constructs";
import { Key } from "aws-cdk-lib/aws-kms";
import { Effect, PolicyStatement } from "aws-cdk-lib/aws-iam";
import { CfnFHIRDatastore } from "aws-cdk-lib/aws-healthlake";

export const addHealthlakeToFunc = (
    scope: Construct,
    id: string,
    func: IFunction,
    hl: CfnFHIRDatastore,
    key: Key
) => {
    func.addToRolePolicy(
        new PolicyStatement({
            actions: [
                "healthlake:ListFHIRDatastores",
                "healthlake:DescribeFHIRDatastore",
                "healthlake:DescribeFHIRImportJob",
                "healthlake:DescribeFHIRExportJob",
                "healthlake:GetCapabilities",
                "healthlake:ReadResource",
                "healthlake:SearchWithGet",
                "healthlake:SearchWithPost",
            ],
            effect: Effect.ALLOW,
            resources: [hl.attrDatastoreArn],
        })
    );

    key.grantEncryptDecrypt(func);
};
