import { readFileSync, writeFileSync } from 'fs';
import { join } from 'path';
import { fileURLToPath } from 'url';
import { dirname } from 'path';

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);

const cdkOutputs = JSON.parse(readFileSync(join(__dirname, '..', 'cdk-outputs.json'), 'utf8'));

const stackName = "AppsyncEventsBedrockCdkStack"

writeFileSync(
    join(__dirname, '..', 'demo-app', '.env.local'), `
VITE_API_KEY=${cdkOutputs[stackName].ApiKey}
VITE_CHANNEL_NAME=${cdkOutputs[stackName].ChannelName}
VITE_REGION=${cdkOutputs[stackName].Region}
VITE_EVENTS_API_HTTP=${cdkOutputs[stackName].EventsApiHttp}
VITE_EVENTS_API_REAL_TIME=${cdkOutputs[stackName].EventsApiRealtime}
VITE_CHAT_API_URL=${cdkOutputs[stackName].ChatApiUrl}`,
    'utf8',
);