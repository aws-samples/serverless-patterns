import 'source-map-support/register';
import * as cdk from 'aws-cdk-lib';
import {WebApplicationWithCloudfrontStack} from '../lib/amazon-cloudfront-for-web-applications-stack';

const app = new cdk.App();
const envUSEAST1 = { account: app.account, region: 'us-east-1' };

const stack = new WebApplicationWithCloudfrontStack(app, 'WebApplicationWithCloudfrontStack', {

  //// CloudFront and ACM requires to be deployed us-east-1 region
  //https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cnames-and-https-requirements.html
  env: envUSEAST1,
  crossRegionReferences: true,
});
