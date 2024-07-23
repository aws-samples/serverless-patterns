import { Context, AppSyncIdentityIAM } from '@aws-appsync/utils';

interface Response {
    accountId: string;
    sourceIp: string[];
    userArn: string;
    username: string;
}

export function request(ctx: Context<void>) {
    // This demo code uses IAM authorization model only, thus it is safe to hardcode the type here
    const identity = ctx.identity as AppSyncIdentityIAM;
    
    const payload: Response = {
        accountId: identity.accountId,
        sourceIp: identity.sourceIp,
        userArn: identity.userArn,
        username: identity.username,
    };

    return {
        payload,
    }
}

export function response(ctx: Context): Response {
    return ctx.result;
}