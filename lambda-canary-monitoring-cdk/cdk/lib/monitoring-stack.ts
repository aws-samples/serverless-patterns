import * as cloudwatch from 'aws-cdk-lib/aws-cloudwatch';
import * as cdk from 'aws-cdk-lib';
import { Construct } from 'constructs';

export interface IMonitoring {
  dashboard: cloudwatch.Dashboard;
}

export class MonitoringStack extends cdk.Stack implements IMonitoring {
  public readonly dashboard: cloudwatch.Dashboard;

  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);
    this.dashboard = new cloudwatch.Dashboard(this, 'Dashboard');
  }
}
