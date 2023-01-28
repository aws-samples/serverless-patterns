import { CfnOutput, Stack, StackProps } from 'aws-cdk-lib'
import {
	AccountRecovery,
	UserPool,
	UserPoolClient,
	VerificationEmailStyle,
} from 'aws-cdk-lib/aws-cognito'

import { Construct } from 'constructs'

interface AuthStackProps extends StackProps {}

export class AuthStack extends Stack {
	public readonly userpool: UserPool
	public readonly userPoolClient: UserPoolClient

	constructor(scope: Construct, id: string, props: AuthStackProps) {
		super(scope, id, props)

		const userPool = new UserPool(this, `ProductUserpool`, {
			selfSignUpEnabled: true,
			accountRecovery: AccountRecovery.PHONE_AND_EMAIL,
			userVerification: {
				emailStyle: VerificationEmailStyle.CODE,
			},
			autoVerify: {
				email: true,
			},
			standardAttributes: {
				email: {
					required: true,
					mutable: true,
				},
			},
		})

		const userPoolClient = new UserPoolClient(this, `ProductUserpoolClient`, {
			userPool,
		})

		this.userpool = userPool
		this.userPoolClient = userPoolClient

		new CfnOutput(this, 'UserPoolId', {
			value: userPool.userPoolId,
		})

		new CfnOutput(this, 'UserPoolClientId', {
			value: userPoolClient.userPoolClientId,
		})
	}
}
