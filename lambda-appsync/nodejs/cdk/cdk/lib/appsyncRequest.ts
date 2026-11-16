import { Sha256 } from '@aws-crypto/sha256-js'
import { defaultProvider } from '@aws-sdk/credential-provider-node'
import { HttpRequest } from '@smithy/protocol-http'
import { SignatureV4 } from '@smithy/signature-v4'
import { URL } from 'url'

const region = process.env.AWS_REGION!

export type QueryDetails = {
	query: string
	variables?: { [key: string]: any }
}

export interface GraphQLResult<T = object> {
	data?: T
	errors?: any[]
	extensions?: { [key: string]: any }
}

const signer = new SignatureV4({
	credentials: defaultProvider(),
	region,
	service: 'appsync',
	sha256: Sha256,
})

/**
 *
 * @param {Object} queryDetails the query, operationName, and variables
 * @param {String} appsyncUrl url of your AppSync API
 * @param {String} apiKey the api key to include in headers. if null, will sign with SigV4
 */
const request = async <T = object>(
	queryDetails: QueryDetails,
	appsyncUrl: string,
	apiKey?: string
): Promise<GraphQLResult<T>> => {
	const endpoint = new URL(appsyncUrl).hostname
	const req = new HttpRequest({
		method: 'POST',
		protocol: 'https:',
		hostname: endpoint,
		path: '/graphql',
		headers: {
			host: endpoint,
			'Content-Type': 'application/json',
			...(apiKey ? { 'x-api-key': apiKey } : {}),
		},
		body: JSON.stringify(queryDetails),
	})

	const { headers, body, method } = apiKey ? req : await signer.sign(req)

	const result = await fetch(appsyncUrl, { method, headers, body })
	return result.json() as Promise<GraphQLResult<T>>
}

export default request
