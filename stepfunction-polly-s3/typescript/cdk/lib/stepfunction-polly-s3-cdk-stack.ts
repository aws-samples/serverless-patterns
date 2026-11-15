import {
  aws_stepfunctions as sfn,
  aws_stepfunctions_tasks as tasks,
  aws_s3 as s3,
  CfnOutput,
  Stack,
  StackProps
} from 'aws-cdk-lib';
import { Construct } from 'constructs';

export class StepfunctionPollyS3CdkStack extends Stack {
  constructor(scope: Construct, id: string, props?: StackProps) {
    super(scope, id, props);

    // For more about voice ids in Amazon Polly
    // Visit: https://docs.aws.amazon.com/polly/latest/dg/voicelist.html#availablevoice-list
    const VOICE_ID = 'Joey';

    const wordsBucket = new s3.Bucket(this, 'WordsBucket');

    const wordsIterator = new sfn.Map(this, 'WordsIterator', {
      maxConcurrency: 5,
    });

    const synthersize = new tasks.CallAwsService(this, 'StartSpeechSynthesisTask', {
      service: 'polly',
      action: 'startSpeechSynthesisTask',
      resultPath: '$.result',
      parameters: {
        "OutputFormat": "mp3",
        "OutputS3BucketName": wordsBucket.bucketName,
        "Text.$": "$.word",
        "VoiceId": VOICE_ID
      },
      iamResources: ['*'],
    });

    const stateMachineDefinition = wordsIterator.iterator(synthersize);

    const wordSynthesiserStateMachine = new sfn.StateMachine(this, 'WordSynthesiser', {
      definition: stateMachineDefinition
    });

    wordsBucket.grantPut(wordSynthesiserStateMachine);

    // Outputs
    new CfnOutput(this, 'StateMachine', {
      value: wordSynthesiserStateMachine.stateMachineName,
      description: 'State machine',
      exportName: 'StateMachine',
    });

    new CfnOutput(this, 'BucketName', {
      value: wordsBucket.bucketName,
      description: 'Bucket name',
      exportName: 'BucketName',
    });
  }
}
