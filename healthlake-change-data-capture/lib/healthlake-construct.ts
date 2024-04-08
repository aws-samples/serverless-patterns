import * as hl from "aws-cdk-lib/aws-healthlake";
import { Construct } from "constructs";
import { Key } from "aws-cdk-lib/aws-kms";

export class HealthlakeConstruct extends Construct {
    private readonly _cfnFHIRDatastore: hl.CfnFHIRDatastore;

    constructor(scope: Construct, id: string, key: Key) {
        super(scope, id);

        this._cfnFHIRDatastore = new hl.CfnFHIRDatastore(
            this,
            "HealthlakeDataStore",
            {
                datastoreTypeVersion: "R4",
                datastoreName: `sample-store`,
                sseConfiguration: {
                    kmsEncryptionConfig: {
                        cmkType: "CUSTOMER_MANAGED_KMS_KEY",
                        kmsKeyId: key.keyId,
                    },
                },
            }
        );
    }

    get cfnFHIRDatastore(): hl.CfnFHIRDatastore {
        return this._cfnFHIRDatastore;
    }
}
