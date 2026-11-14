import { Template } from 'aws-cdk-lib/assertions';
import * as cdk from 'aws-cdk-lib';
import * as StaticSite from '../lib/static-site-stack';

test('Empty Stack', () => {
    const app = new cdk.App();
    // WHEN
    const stack = new StaticSite.StaticSiteStack(app, 'MyTestStack');
    // THEN
    Template.fromStack(stack).hasResource("AWS::Lambda::Function", {});
});
