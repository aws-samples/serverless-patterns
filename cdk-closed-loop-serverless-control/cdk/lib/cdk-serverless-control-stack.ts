import { Stack, StackProps, Duration } from 'aws-cdk-lib';
import { Construct } from 'constructs';
import { PythonFunction } from "@aws-cdk/aws-lambda-python-alpha";
import { Runtime } from 'aws-cdk-lib/aws-lambda';
import { Effect, PolicyStatement } from 'aws-cdk-lib/aws-iam';
import { Rule } from 'aws-cdk-lib/aws-events';
import { Alarm, Metric, MathExpression, AlarmState, AlarmRule, CompositeAlarm, Statistic, ComparisonOperator, TreatMissingData } from 'aws-cdk-lib/aws-cloudwatch';
import { LambdaFunction } from 'aws-cdk-lib/aws-events-targets';

export class ServerlessControlStack extends Stack {
  constructor(scope: Construct, id: string, props?: StackProps) {
    super(scope, id, props);
    
    const callPlannerLambda = new PythonFunction(this, `CallPlannerLambda`, {
			entry: `lambda/CallPlannerLambda`, 
			index: 'handler.py',
			handler: 'handler', 
			functionName: 'CallPlanner',
			runtime: Runtime.PYTHON_3_9,
			memorySize: 128,
			timeout: Duration.seconds(5)
		});

		callPlannerLambda.addToRolePolicy(new PolicyStatement({
			effect: Effect.ALLOW,
			actions: ["events:PutEvents", "cloudwatch:DescribeAlarms"],
			resources: ["*"]
		}));

		const thirdPartyProcessorLambda = new PythonFunction(this, `ThirdPartyProcessorLambda`, {
			entry: `lambda/ThirdPartyProcessorLambda`, 
			index: 'handler.py', 
			handler: 'handler', 
			functionName: 'ThirdPartyProcessor',
			runtime: Runtime.PYTHON_3_9,
			memorySize: 128,
      timeout: Duration.seconds(30)
		});

		thirdPartyProcessorLambda.addToRolePolicy(new PolicyStatement({
      "effect": Effect.ALLOW,
			"actions": ["cloudwatch:PutMetricData"], 
			"resources": ["*"]
		}));
		
    new Rule(this, `ThirdPartyProcessorRule`, {
      targets: [new LambdaFunction(thirdPartyProcessorLambda)],
      eventPattern: {
        source: ["thirdPartyCalls"]
      }
    });

    const thirdPartyCallResponseTimeAlarm = new Alarm(this, `ThirdPartyCallResponseTimeAlarm`, {
      alarmName: `ThirdPartyCallResponseTimeAlarm`,
      metric: new Metric({
        "metricName": "APIResponseTime",
        "namespace": "ThirdPartyCalls",
        "period": Duration.minutes(1),
        "statistic": Statistic.AVERAGE,
        "dimensionsMap": {
          "Function": "ThirdPartyProcessor"
        }
      }),
      threshold: 2000,
      comparisonOperator: ComparisonOperator.GREATER_THAN_THRESHOLD,
      treatMissingData: TreatMissingData.MISSING,
      evaluationPeriods: 1,
      datapointsToAlarm: 1
    });

    const thirdPartyCallResponseStatusCodeAlarm = new Alarm(this, `ThirdPartyCallResponseStatusCodeAlarm`, {
      alarmName: `ThirdPartyCallResponseStatusCodeAlarm`,
      metric: new MathExpression({
        expression: "FILL(m2,0)/FILL(m1,1)",
        period: Duration.minutes(1),
        label: "APIErrorRatio",
        usingMetrics: {
          m1: new Metric({
            "metricName": "APIResponseCode",
            "namespace": "ThirdPartyCalls",
            "period": Duration.minutes(1),
            "statistic": Statistic.SUM,
            "dimensionsMap": {
              "Function": "ThirdPartyProcessor",
              "StatusCode": "200"
            }
          }),
          m2: new Metric({
            "metricName": "APIResponseCode",
            "namespace": "ThirdPartyCalls",
            "period": Duration.minutes(1),
            "statistic": Statistic.SUM,
            "dimensionsMap": {
              "Function": "ThirdPartyProcessor",
              "StatusCode": "500"
            }
          }),
        }
      }),
      threshold: 0.4,
      comparisonOperator: ComparisonOperator.GREATER_THAN_THRESHOLD,
      treatMissingData: TreatMissingData.MISSING,
      evaluationPeriods: 1,
      datapointsToAlarm: 1
    });
    
    new CompositeAlarm(this, 'ThirdPartyCallStatus', {
      compositeAlarmName: "ThirdPartyCallStatus",
      alarmRule: AlarmRule.anyOf(
            AlarmRule.fromAlarm(thirdPartyCallResponseTimeAlarm, AlarmState.ALARM),
            AlarmRule.fromAlarm(thirdPartyCallResponseStatusCodeAlarm, AlarmState.ALARM),
      ),

    });

  }
}
