const { VerifiedPermissionsClient, IsAuthorizedCommand } = require('@aws-sdk/client-verifiedpermissions');
const client = new VerifiedPermissionsClient();

const ACTIONS = ['Read', 'Write', 'Delete'];

// Demo documents. Owner and classification are server-side data, never request input.
const OWNER = process.env.DEMO_OWNER_PRINCIPAL || 'no-owner-configured';
const DOCUMENTS = {
  'doc-1': { owner: OWNER, classification: 'confidential' },
  'doc-2': { owner: OWNER, classification: 'public' }
};
const ADMINS = (process.env.ADMIN_PRINCIPALS || '').split(',').map((s) => s.trim()).filter(Boolean);

const respond = (statusCode, body) => ({ statusCode, body: JSON.stringify(body) });

exports.handler = async (event) => {
  // Caller identity comes from the SigV4 signature checked by the AWS_IAM Function URL.
  const callerArn = event.requestContext?.authorizer?.iam?.userArn;
  if (!callerArn) return respond(403, { error: 'No caller identity' });
  // Drop the session name so an assumed role is one stable principal.
  const principal = callerArn.replace(/^(arn:[^:]+:sts::\d+:assumed-role\/[^/]+)\/.+$/, '$1');
  const role = ADMINS.includes(principal) ? 'admin' : 'reader';

  const usage = { error: `Provide action (${ACTIONS.join(', ')}) and resourceId (${Object.keys(DOCUMENTS).join(', ')})` };
  let request;
  try {
    request = JSON.parse(event.body || '{}');
  } catch (e) {
    return respond(400, usage);
  }
  if (request === null || typeof request !== 'object' || Array.isArray(request)) return respond(400, usage);
  const { action, resourceId } = request;
  // Own-property check: inherited names such as constructor or __proto__ are not documents.
  if (!ACTIONS.includes(action) || typeof resourceId !== 'string' || !Object.hasOwn(DOCUMENTS, resourceId)) {
    return respond(400, usage);
  }
  const doc = DOCUMENTS[resourceId];

  const result = await client.send(new IsAuthorizedCommand({
    policyStoreId: process.env.POLICY_STORE_ID,
    principal: { entityType: 'MyApp::User', entityId: principal },
    action: { actionType: 'MyApp::Action', actionId: action },
    resource: { entityType: 'MyApp::Document', entityId: resourceId },
    entities: {
      entityList: [
        { identifier: { entityType: 'MyApp::User', entityId: principal }, attributes: { role: { string: role } } },
        {
          identifier: { entityType: 'MyApp::Document', entityId: resourceId },
          attributes: {
            owner: { entityIdentifier: { entityType: 'MyApp::User', entityId: doc.owner } },
            classification: { string: doc.classification }
          }
        }
      ]
    }
  }));
  return respond(200, { decision: result.decision, principal, role, action, resourceId });
};
