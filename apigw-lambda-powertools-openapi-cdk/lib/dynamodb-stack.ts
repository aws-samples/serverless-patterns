// lib/dynamodb-stack.ts
import * as cdk from "aws-cdk-lib";
import * as dynamodb from "aws-cdk-lib/aws-dynamodb";
import { Construct } from "constructs";

export interface DynamoDBStackProps extends cdk.NestedStackProps {
  stageName: string;
}

export class DynamoDBStack extends cdk.NestedStack {
  public readonly table: dynamodb.TableV2;

  constructor(scope: Construct, id: string, props: DynamoDBStackProps) {
    super(scope, id, props);

    this.table = new dynamodb.TableV2(this, "Table", {
      tableName: "orders",
      partitionKey: {
        name: "p",
        type: dynamodb.AttributeType.STRING,
      },
      sortKey: {
        name: "s",
        type: dynamodb.AttributeType.STRING,
      },
      billing: dynamodb.Billing.onDemand(),
      removalPolicy:
        props.stageName === "dev"
          ? cdk.RemovalPolicy.DESTROY
          : cdk.RemovalPolicy.RETAIN,
    });
  }
}
