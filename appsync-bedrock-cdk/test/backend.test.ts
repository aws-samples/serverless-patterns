import { Amplify, API, graphqlOperation } from 'aws-amplify';
import { GraphQLQuery } from '@aws-amplify/api';
import { InvokeMutation } from '../src/API';
import * as mutations from '../src/graphql/mutations';

Amplify.configure({
    aws_appsync_graphqlEndpoint:
    '<GraphQLApiURL>',
    aws_appsync_region: '<Region>',
    aws_appsync_authenticationType: 'API_KEY',
    aws_appsync_apiKey: '<GraphQLApiKey>'
})

// After the deployment of the stack, you should be able to retrieve the output from Bedrock invocations
test('Bedrock Model invoked', async () => {

    const mutation = await API.graphql<GraphQLQuery<InvokeMutation>>({
        query: mutations.invoke,
        variables: { prompt: 'What is the capital of France?' }
    }
    )

    expect(mutation.data?.invoke).toBeDefined()
})
