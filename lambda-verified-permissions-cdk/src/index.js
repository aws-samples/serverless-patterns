const { VerifiedPermissionsClient, IsAuthorizedCommand } = require('@aws-sdk/client-verifiedpermissions');
const client = new VerifiedPermissionsClient();

exports.handler = async (event) => {
  const body = JSON.parse(event.body || '{}');
  const { userId, role, action, resourceId, classification } = body;

  if (!userId || !role || !action || !resourceId) {
    return { statusCode: 400, body: JSON.stringify({ error: 'Missing required fields: userId, role, action, resourceId' }) };
  }

  const params = {
    policyStoreId: process.env.POLICY_STORE_ID,
    principal: { entityType: 'MyApp::User', entityId: userId },
    action: { actionType: 'MyApp::Action', actionId: action },
    resource: { entityType: 'MyApp::Document', entityId: resourceId },
    entities: {
      entityList: [
        { identifier: { entityType: 'MyApp::User', entityId: userId }, attributes: { role: { string: role } } },
        { identifier: { entityType: 'MyApp::Document', entityId: resourceId }, attributes: { owner: { string: userId }, classification: { string: classification || 'public' } } }
      ]
    }
  };

  const result = await client.send(new IsAuthorizedCommand(params));
  return {
    statusCode: 200,
    body: JSON.stringify({ decision: result.decision, userId, action, resourceId, role })
  };
};
