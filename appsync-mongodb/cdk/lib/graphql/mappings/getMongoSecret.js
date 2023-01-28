import { util } from '@aws-appsync/utils'

export function request(ctx) {
	return {
		method: 'POST',
		version: '2018-05-29',
		resourcePath: '/',
		params: {
			headers: {
				'content-type': 'application/x-amz-json-1.1',
				'x-amz-target': 'secretsmanager.GetSecretValue',
			},
			body: {
				SecretId: 'APPSYNC_MONGO_API_KEY',
			},
		},
	}
}

export function response(ctx) {
	//"{Name: 'APPSYNC_MONGO_API_KEY', SecretString: 'abc123'}"
	const result = JSON.parse(ctx.result.body).SecretString
	console.log(result)
	return result
}
