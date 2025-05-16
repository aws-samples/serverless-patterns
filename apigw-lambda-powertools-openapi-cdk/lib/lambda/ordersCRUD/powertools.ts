import { Logger } from "@aws-lambda-powertools/logger";
import { Metrics } from "@aws-lambda-powertools/metrics";
import { Tracer } from "@aws-lambda-powertools/tracer";
import { SecretsProvider } from "@aws-lambda-powertools/parameters/secrets";

// objects created here for import and reuse in other files
export const logger = new Logger();
export const metrics = new Metrics();
export const secretsProvider = new SecretsProvider({});
export const tracer = new Tracer();

logger.appendKeys({
  stage: process.env.STAGE,
});
