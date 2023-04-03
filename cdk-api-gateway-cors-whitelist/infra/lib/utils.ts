import { GoFunction } from "@aws-cdk/aws-lambda-go-alpha";
import { Duration } from "aws-cdk-lib";
import { Alarm, Metric } from "aws-cdk-lib/aws-cloudwatch";
import { Construct } from "constructs";

export const createFailureAlarm = (
    c: Construct,
    id: string,
    func: GoFunction
): Alarm => {
    return new Alarm(c, id, {
        alarmDescription: "The latest deployment errors > 0",
        metric: new Metric({
            metricName: "Errors",
            namespace: "AWS/Lambda",
            statistic: "sum",
            dimensionsMap: {
                Resource: `${func.functionName}:${func.currentVersion}`,
                FunctionName: func.functionName,
            },
            period: Duration.minutes(1),
        }),

        threshold: 1,
        evaluationPeriods: 1,
    });
};
