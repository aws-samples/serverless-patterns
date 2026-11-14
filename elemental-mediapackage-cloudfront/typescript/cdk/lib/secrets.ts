/**
 *  Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
 *
 *  Licensed under the Apache License, Version 2.0 (the "License"). You may not use this file except in compliance
 *  with the License. A copy of the License is located at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 *  or in the 'license' file accompanying this file. This file is distributed on an 'AS IS' BASIS, WITHOUT WARRANTIES
 *  OR CONDITIONS OF ANY KIND, express or implied. See the License for the specific language governing permissions
 *  and limitations under the License.
 */

import {
  Aws,
  CfnOutput,
  aws_secretsmanager as secretsmanager,
} from "aws-cdk-lib";
import { Construct } from "constructs";

export class Secrets extends Construct {
  public readonly cdnSecret: secretsmanager.ISecret;
 
  constructor(scope: Construct, id: string) {
    super(scope, id);

    const cdnSecret = new secretsmanager.Secret(this, "CdnSecret", {
      secretName: "MediaPackage/"+Aws.STACK_NAME,
      description: "Secret for Secure Resilient Live Streaming Delivery",
      generateSecretString: {
        secretStringTemplate: JSON.stringify({ MediaPackageCDNIdentifier: "" }),
        generateStringKey: "MediaPackageCDNIdentifier", //MUST keep this StringKey to use with EMP
      },
    });

    this.cdnSecret = cdnSecret;

    new CfnOutput(this, "cdnSecret", {
      value: cdnSecret.secretName,
      exportName: Aws.STACK_NAME + "cdnSecret",
      description: "The name of the cdnSecret",
    });


  }
}
