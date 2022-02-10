import { Stack, Construct, StackProps } from '@aws-cdk/core';
import { CfnServer, CfnUser } from '@aws-cdk/aws-transfer';
import { Role, PolicyStatement, ServicePrincipal } from '@aws-cdk/aws-iam';
import { Bucket } from '@aws-cdk/aws-s3';

import { conf } from './options';

export class sftpStack extends Stack {
  constructor(scope: Construct, id: string, props?: StackProps) {
    super(scope, id, props);
    const  { s3Attr, users } = conf;

    const loggingRole = new Role(this, 'loggingRole', {
      assumedBy: new ServicePrincipal('transfer.amazonaws.com'),
      description: 'logging role for SFTP server'
    });

    loggingRole.addToPrincipalPolicy(new PolicyStatement({
      sid: 'Logs',
      actions: [
        'logs:CreateLogStream',
        'logs:DescribeLogStreams',
        'logs:CreateLogGroup',
        'logs:PutLogEvents',
      ],
      resources: ['*'],
    }));

   const sftpServer = new CfnServer(this, 'sftpServer', {
     domain: 'S3',
     endpointType: 'PUBLIC',
     identityProviderType: 'SERVICE_MANAGED',
     loggingRole: loggingRole.roleArn,
     protocols: ['SFTP'],
   });

   const serverId = sftpServer.attrServerId;
   const homeDirectory = Bucket.fromBucketArn(this, 'homeDirectory', s3Attr.bucketARN);

   const userRole = new Role(this, 'userRole', {
    assumedBy: new ServicePrincipal('transfer.amazonaws.com'),
    description: 'SFTP standard user role',
  });
  userRole.addToPrincipalPolicy(new PolicyStatement({
    sid: 'List',
    actions: ['s3:ListBucket'],
    resources: [
      `${homeDirectory.bucketArn}/*`,
      `${homeDirectory.bucketArn}`
    ],
  }));
  userRole.addToPrincipalPolicy(new PolicyStatement({
    sid: 'UserObjects',
    actions: [
        's3:PutObject',
        's3:GetObject',
        's3:GetObjectVersion',
    ],
    resources: [`${homeDirectory.bucketArn}/*`],
  }));

  users.forEach((user, i) => {
    const { userName, publicKey } = user;
    new CfnUser(this, `user${i + 1}`, {
        role: userRole.roleArn,
        serverId,
        userName,
        homeDirectory: `/${homeDirectory.bucketName}`,
        sshPublicKeys: [publicKey],
        policy: '{ \n\
            "Version": "2012-10-17", \n\
                    "Statement": [ \n\
                        { \n\
                            "Sid": "AllowListingOfUserFolder", \n\
                            "Effect": "Allow", \n\
                            "Action": "s3:ListBucket", \n\
                            "Resource": "arn:aws:s3:::${transfer:HomeBucket}", \n\
                            "Condition": { \n\
                                "StringLike": { \n\
                                    "s3:prefix": [ \n\
                                        "home/${transfer:UserName}/*", \n\
                                        "home/${transfer:UserName}" \n\
                                    ] \n\
                                } \n\
                            } \n\
                        }, \n\
                        { \n\
                            "Sid": "HomeDirObjectAccess", \n\
                            "Effect": "Allow", \n\
                            "Action": [ \n\
                                "s3:PutObject", \n\
                                "s3:GetObject", \n\
                                "s3:GetObjectVersion" \n\
                            ], \
                            "Resource": "arn:aws:s3:::${transfer:HomeDirectory}*" \n\
                        } \n\
                    ] \n\
            } \n\
        ',
    });
});
}
}
