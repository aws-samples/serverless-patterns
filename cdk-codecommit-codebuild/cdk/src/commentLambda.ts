import * as AWS from 'aws-sdk';

const client = new AWS.CodeCommit({region: 'us-east-1'});

interface Variables {
    name: string,
    value: string
}

interface Environment {
    'environment-variables': Variables[]
}

interface AdditionalInformation {
    environment: Environment
}

interface CodebuildEvent {
    'additional-information': AdditionalInformation,
    'build-status': string,
    'build-id': string
}

const getVariableFromEvent = (event: CodebuildEvent, variableName: string) => {
    const variable =  event['additional-information']
        .environment['environment-variables']
        .find((variable: any) => variable.name === variableName)
        ?.value
    if (variable === undefined) {
        throw new Error('Variable missing in the environment. Make sure to inject everything in the Codebuild Environment')
    }

    return variable
}

const getBuildStatus = (event: CodebuildEvent) => {
    return event['build-status']
}

const getBuildId = (event: CodebuildEvent) => {
    return event['build-id'].split('/')[1]
}

const extractVariablesFromEvent = (event: CodebuildEvent) => {
    return {
        afterCommitId: getVariableFromEvent(event, 'destinationCommit'),
        beforeCommitId: getVariableFromEvent(event, 'sourceCommit'),
        pullRequestId: getVariableFromEvent(event, 'pullRequestID'),
        repositoryName: getVariableFromEvent(event, 'repositoryName'),
        buildId: getBuildId(event),
        status: getBuildStatus(event),
    }
}

interface publishComment {
    afterCommitId: string,
    beforeCommitId: string,
    pullRequestId: string,
    repositoryName: string,
    comment: string
}

const publishComment = async ({ afterCommitId, beforeCommitId, pullRequestId, repositoryName, comment }: publishComment) => {
    await client.postCommentForPullRequest({
        afterCommitId,
        beforeCommitId,
        pullRequestId,
        repositoryName,
        content: comment
    }).promise()
}

const buildComment = (status: string, buildId: string) => {
    const buildUrl = `https://console.aws.amazon.com/codesuite/codebuild/522548170624/projects/ExampleCodeBuild108CF21E-07B3VTpE1jtn/build/${buildId}`

    return `Build ${status}! [(see logs)](${buildUrl})`
}

export const handler = async (event: CodebuildEvent) => {
    const {
        afterCommitId,
        beforeCommitId,
        pullRequestId,
        repositoryName,
        status,
        buildId
    } = extractVariablesFromEvent(event)

    const comment = buildComment(status, buildId)

    await publishComment({
        afterCommitId,
        beforeCommitId,
        pullRequestId,
        repositoryName,
        comment
    })
}
