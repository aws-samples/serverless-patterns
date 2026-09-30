// GENERATED — do not edit this copy. The source of truth is maintained by
// the Serverless Land team; open an issue to request a change.

// Serverless Land pattern file schema
//
// Describes the pattern JSON file (e.g. example-pattern.json) that every
// serverless pattern needs so it can be published on
// https://serverlessland.com/patterns. Requires zod ^4.
//
//   import { createPatternSchema } from "./pattern-schema.mjs";
//   const result = createPatternSchema().safeParse(pattern);
//   if (!result.success) console.log(result.error.issues);

import { z } from "zod";

// ---------------------------------------------------------------------------
// Allowed values
// ---------------------------------------------------------------------------

export const VALID_LANGUAGES = [
  ".NET",
  "AWS CLI",
  "Bash",
  "Go",
  "Integration",
  "Java",
  "JSON",
  "Node.js",
  "OpenAPI",
  "PHP",
  "PowerShell",
  "Python",
  "Ruby",
  "Rust",
  "Spark",
  "TypeScript",
  "VTL",
  "YAML",
];

export const VALID_FRAMEWORKS = [
  "AWS CDK",
  "AWS CDK for Terraform",
  "AWS CLI",
  "AWS CloudFormation",
  "AWS SAM",
  "Pulumi",
  "Serverless Framework",
  "Terraform",
  "Terraform (with modules)",
];

export const VALID_LEVELS = ["100", "200", "300", "400"];

// ---------------------------------------------------------------------------
// Official service names in titles
//
// The first mention of a service in a title must use its official name
// ("AWS Lambda", not "Lambda"). Later mentions may use the short form, e.g.
// "AWS Lambda to Lambda".
// ---------------------------------------------------------------------------

export const INFORMAL_SERVICE_NAMES = {
  // Compound names first (checked before their shorter parts)
  "Kinesis Data Firehose": "Amazon Data Firehose",
  "Kinesis Firehose": "Amazon Data Firehose",
  "Kinesis Data Streams": "Amazon Kinesis",
  "Step Functions": "AWS Step Functions",
  "API Gateway": "Amazon API Gateway",
  "S3 Object Lambda": "Amazon S3 Object Lambda",
  SAM: "AWS SAM",
  // Single-word names
  Lambda: "AWS Lambda",
  DynamoDB: "Amazon DynamoDB",
  EventBridge: "Amazon EventBridge",
  CloudFront: "Amazon CloudFront",
  CloudWatch: "Amazon CloudWatch",
  CloudFormation: "AWS CloudFormation",
  CloudTrail: "AWS CloudTrail",
  Cognito: "Amazon Cognito",
  AppSync: "AWS AppSync",
  Kinesis: "Amazon Kinesis",
  Firehose: "Amazon Data Firehose",
  Bedrock: "Amazon Bedrock",
  SageMaker: "Amazon SageMaker",
  Fargate: "AWS Fargate",
  Rekognition: "Amazon Rekognition",
  Textract: "Amazon Textract",
  Comprehend: "Amazon Comprehend",
  Transcribe: "Amazon Transcribe",
  Translate: "Amazon Translate",
  Polly: "Amazon Polly",
  Glue: "AWS Glue",
  S3: "Amazon S3",
  SNS: "Amazon SNS",
  SQS: "Amazon SQS",
  Amplify: "AWS Amplify",
  Athena: "Amazon Athena",
  Redshift: "Amazon Redshift",
  OpenSearch: "Amazon OpenSearch",
  ElastiCache: "Amazon ElastiCache",
  DocumentDB: "Amazon DocumentDB",
  Aurora: "Amazon Aurora",
};

function escapeRegex(str) {
  return str.replace(/[.*+?^${}()|[\]\\]/g, "\\$" + "&");
}

/**
 * Returns [{ found, expected }] for each service whose first mention in the
 * title isn't its official name. Empty array = title is fine.
 */
export function findInformalServiceNames(title) {
  const issues = [];

  // First pass: services whose first occurrence uses the AWS/Amazon prefix.
  const introduced = new Set();
  for (const [shortName] of Object.entries(INFORMAL_SERVICE_NAMES)) {
    const escaped = escapeRegex(shortName);
    const re = new RegExp("\\b(?:AWS|Amazon|Amazon Data)\\s" + escaped + "\\b");
    if (re.test(title)) {
      introduced.add(shortName);
    }
  }

  // Second pass: flag a service only if its first occurrence is bare and no
  // parent service was introduced ("S3" introduced makes bare
  // "S3 Object Lambda" OK).
  let masked = title;
  for (const [shortName, officialName] of Object.entries(
    INFORMAL_SERVICE_NAMES,
  )) {
    const escaped = escapeRegex(shortName);
    const anyOccurrence = new RegExp(
      "\\b(?:AWS\\s|Amazon\\s|Amazon Data\\s)?" + escaped + "\\b",
    );
    const match = masked.match(anyOccurrence);
    if (!match) continue;

    const firstMatch = match[0];
    const hasPrefix = /^(?:AWS|Amazon|Amazon Data)\s/.test(firstMatch);

    // Mask the match so shorter names don't re-flag parts of it
    masked =
      masked.slice(0, match.index) +
      "\0".repeat(firstMatch.length) +
      masked.slice(match.index + firstMatch.length);

    if (hasPrefix) continue;
    if (introduced.has(shortName)) continue;

    const parentIntroduced = [...introduced].some((svc) =>
      shortName.startsWith(svc + " "),
    );
    if (parentIntroduced) continue;

    issues.push({ found: shortName, expected: officialName });
  }
  return issues;
}

// ---------------------------------------------------------------------------
// Sections
// ---------------------------------------------------------------------------

export const introBoxSchema = z.object({
  headline: z.string(),
  text: z.array(z.string()),
});

export const resourcesSchema = z
  .object({
    headline: z.string().optional(),
    bullets: z
      .array(
        z.object({ text: z.string().optional(), link: z.string().optional() }),
      )
      .optional(),
  })
  .optional();

export const deploySchema = z.object({ text: z.array(z.string()) });

export const testingSchema = z.object({
  headline: z.string().optional(),
  text: z.array(z.string()),
});

export const cleanupSchema = z.object({
  headline: z.string().optional(),
  text: z.array(z.string()),
});

// ---------------------------------------------------------------------------
// People
//
// First-time authors: add yourself to "authors".
// Returning authors: if you have a profile page at
// https://serverlessland.com/about/your-name, you can instead list
//   "contributors": ["content/contributors/your-name.json"]
// using the same "your-name" as the page URL. You can use both.
// ---------------------------------------------------------------------------

const socialHandle = (pattern, message) =>
  z.string().regex(pattern, message).or(z.literal("")).optional();

export const authorsSchema = z
  .array(
    z
      .object({
        name: z.string().trim().min(1, "author name must not be empty"),
        bio: z.string().trim().min(1, "author bio must not be empty"),
        image: z.string().optional(),
        linkedin: socialHandle(
          /^[^\s/:]+$/,
          'linkedin must be your profile ID only, not a URL (e.g. "jane-doe")',
        ),
        twitter: socialHandle(
          /^@?[A-Za-z0-9_]+$/,
          'twitter must be your handle only — letters, numbers and _ (e.g. "jane_doe"), not a URL',
        ),
      })
      .strict(),
  )
  .min(1, "authors array must have at least 1 entry");

export const contributorsSchema = z
  .array(
    z
      .string()
      .regex(
        /^content\/contributors\/[^/]+\.json$/,
        'Each contributor must look like "content/contributors/your-name.json", where your-name matches your profile page at https://serverlessland.com/about/your-name',
      ),
  )
  .min(1, "contributors array must have at least 1 entry");

// ---------------------------------------------------------------------------
// Pattern
// ---------------------------------------------------------------------------

/** A folder path relative to the repo root: "a/b/c", no URL, no leading "serverless-patterns/", no leading/trailing "/". */
export const patternPathSchema = z
  .string()
  .regex(
    /^(?!serverless-patterns(\/|$))(?!https?:)[^/\s]+(\/[^/\s]+)*$/,
    'patternPath is the folder from the repo root, e.g. "sqs-lambda/python/sam" (no URL, no leading "serverless-patterns/", no leading or trailing "/")',
  );

/**
 * Pattern fields, without the people fields. Pass a servicesMap
 * ({ "lambda": "AWS Lambda", ... }) to also check patternArch service keys.
 *
 * Checks sit on the fields themselves so every error is reported in one go
 * (Zod 4 skips object-level refinements while any field is invalid).
 */
export function createPatternShape(servicesMap) {
  return {
    title: z
      .string({ required_error: "Missing 'title'" })
      .max(100, "title must be 100 characters or fewer")
      .superRefine(checkTitleServiceNames),
    description: z
      .string({ required_error: "Missing 'description'" })
      .max(175, "description must be 175 characters or fewer"),
    language: z.enum(VALID_LANGUAGES, {
      message: `language must be one of: ${VALID_LANGUAGES.join(", ")}`,
    }),
    framework: z.enum(VALID_FRAMEWORKS, {
      message: `framework must be one of: ${VALID_FRAMEWORKS.join(", ")}`,
    }),
    level: z.enum(VALID_LEVELS, {
      message: `level must be one of: ${VALID_LEVELS.join(", ")}`,
    }),
    // The pattern page draws the architecture from patternArch, so an
    // embedded image in the intro text would show it twice.
    introBox: introBoxSchema.extend({
      text: z.array(
        z
          .string()
          .refine(
            (t) => !/<img\b/i.test(t),
            "introBox.text must not contain <img> tags — describe the architecture with patternArch instead",
          ),
      ),
    }),
    // The file shown on the pattern page. Serverless Land records the folder
    // your example-pattern.json is in when it imports the pattern, so you
    // don't need to give the folder.
    gitHub: z.object(
      {
        template: z.object(
          {
            // Relative to your pattern folder, not the repo root, e.g.
            // "template.yaml" or "cdk/lib/my-stack.ts".
            templateFile: z
              .string({ error: 'Missing gitHub.template.templateFile (e.g. "template.yaml")' })
              .min(1, 'gitHub.template.templateFile must not be empty (e.g. "template.yaml")'),
            // Pattern folder from the repo root, e.g. "sqs-lambda/python/sam".
            // Optional: set by Serverless Land.
            patternPath: patternPathSchema.optional(),
            // Older fields, still accepted. Serverless Land derives these now.
            repoURL: z.string().optional(),
            templateURL: z.string().optional(),
            projectFolder: z.string().optional(),
          },
          { error: 'Missing gitHub.template: add { "templateFile": "template.yaml" }' },
        ),
      },
      { error: 'Missing gitHub: add { "template": { "templateFile": "template.yaml" } }' },
    ),
    deploy: deploySchema,
    testing: testingSchema,
    cleanup: cleanupSchema,
    resources: resourcesSchema,
    patternArch: servicesMap
      ? z
          .any()
          .optional()
          .superRefine((arch, ctx) =>
            checkPatternArchServices(arch, ctx, servicesMap),
          )
      : z.any().optional(),
  };
}

/**
 * The pattern file schema: every field rule, with people given as "authors"
 * and/or "contributors" (at least one required). Extra fields are allowed.
 */
export function createPatternSchema({ servicesMap } = {}) {
  return z
    .object({
      ...createPatternShape(servicesMap),
      authors: authorsSchema.optional(),
      contributors: contributorsSchema.optional(),
    })
    .passthrough()
    .refine((data) => data?.authors?.length || data?.contributors?.length, {
      path: ["authors"],
      message: "Add yourself to 'authors' (or 'contributors').",
      when: () => true, // report alongside any other errors
    })
    .refine(templateFileNotPrefixed, {
      path: ["gitHub", "template", "templateFile"],
      message:
        "templateFile is relative to the pattern folder — remove the folder prefix",
      when: () => true,
    });
}

/** templateFile must not repeat the pattern folder (it's already relative to it). */
export function templateFileNotPrefixed(data) {
  const { patternPath, projectFolder, templateFile } = data?.gitHub?.template ?? {};
  const folderValue = patternPath || projectFolder;
  if (typeof folderValue !== "string" || typeof templateFile !== "string") {
    return true;
  }
  const folder = folderValue.replace(/\/+$/, "");
  return !(folder && templateFile.startsWith(folder + "/"));
}

function checkTitleServiceNames(title, ctx) {
  for (const { found, expected } of findInformalServiceNames(title)) {
    ctx.addIssue({
      code: "custom",
      message: `Use official service name "${expected}" instead of "${found}" in title.`,
    });
  }
}

function checkPatternArchServices(arch, ctx, servicesMap) {
  if (!arch || typeof arch !== "object") return;
  for (const [key, value] of Object.entries(arch)) {
    if (value && typeof value === "object" && "service" in value) {
      if (value.service && !Object.hasOwn(servicesMap, value.service)) {
        ctx.addIssue({
          code: "custom",
          path: [key, "service"],
          message: `Invalid service "${value.service}" — not a known service key.`,
        });
      }
    }
  }
}
