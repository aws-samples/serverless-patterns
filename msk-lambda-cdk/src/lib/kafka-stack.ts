/*
 * Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
 * SPDX-License-Identifier: MIT-0
 *
 * Permission is hereby granted, free of charge, to any person obtaining a copy of this
 * software and associated documentation files (the "Software"), to deal in the Software
 * without restriction, including without limitation the rights to use, copy, modify,
 * merge, publish, distribute, sublicense, and/or sell copies of the Software, and to
 * permit persons to whom the Software is furnished to do so.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
 * INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A
 * PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
 * HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
 * OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
 * SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
 */
import * as cdk from '@aws-cdk/core';
import * as msk from '@aws-cdk/aws-msk';
import * as ec2 from '@aws-cdk/aws-ec2'

import {VpcStack} from "./vpc-stack";
import { ManagedKafkaEventSource } from '@aws-cdk/aws-lambda-event-sources';
import { Cluster } from '@aws-cdk/aws-msk';

export class KafkaStack extends cdk.Stack {
    public kafkaCluster: msk.CfnCluster;

    // public readonly myClusterArn: string;

    constructor(vpcStack: VpcStack, scope: cdk.Construct, id: string, props?: cdk.StackProps) {
        super(scope, id, props);
        
        // const auth = new msk.ClientAuthentication.sasl({iam:});

        this.kafkaCluster = new msk.CfnCluster(this, "kafkaCluster", {
            brokerNodeGroupInfo: {
                securityGroups: [vpcStack.kafkaSecurityGroup.securityGroupId],
                clientSubnets: [...vpcStack.vpc.selectSubnets({
                    subnetType: ec2.SubnetType.PRIVATE_WITH_NAT
                }).subnetIds],
                instanceType: "kafka.t3.small",
                storageInfo: {
                    ebsStorageInfo: {
                        volumeSize: 5
                    }
                }
            },
            clusterName: "TransactionsKafkaCluster",
            kafkaVersion: "2.7.0",
            numberOfBrokerNodes: 2,
            clientAuthentication: {
                sasl: {
                  iam: {
                    enabled: false,
                  },
                  scram: {
                    enabled: false,
                  },
                },
                tls: {
                  enabled: false,
                },
                unauthenticated: {
                  enabled: true,
                },
            },    
        });

        // this.myClusterArn = cdk.Fn.getAtt(this.kafkaCluster.logicalId, "Arn").toString();

    }
}