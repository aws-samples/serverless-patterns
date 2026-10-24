// Flags admin-equivalent IAM grants in a pattern's infrastructure code.
//
// A pattern shows how services connect, so it should never need account admin.
// This check scans the pattern folder for:
//   - the AdministratorAccess, IAMFullAccess and PowerUserAccess managed policies
//   - iam:* actions
//   - an Action of * paired with a Resource of * in an identity policy
//     (statements with a Principal are resource policies and are skipped)
//
// It's a text scan rather than a template parse, so it covers SAM, CloudFormation,
// CDK and Terraform the same way. Commented-out lines are ignored.
const fs = require('fs');
const path = require('path');

const SKIP_DIRS = new Set([
  'node_modules', '.aws-sam', 'cdk.out', '.git', '.terraform', 'target', 'build', 'dist',
  '__pycache__', '.venv', 'venv', 'site-packages', 'botocore', 'boto3',
]);
const EXTENSIONS = new Set(['.yaml', '.yml', '.json', '.ts', '.js', '.mjs', '.py', '.tf', '.java', '.go', '.cs']);
const SKIP_FILES = new Set(['example-pattern.json', 'package-lock.json', 'package.json', 'tsconfig.json', 'cdk.json']);
const MAX_BYTES = 1024 * 1024;

const RULES = [
  { id: 'managed-admin', re: /\b(AdministratorAccess|IAMFullAccess|PowerUserAccess)\b/, message: 'grants an admin-equivalent AWS managed policy' },
  { id: 'iam-wildcard', re: /(^|[\s"'[,])iam:\*($|[\s"'\],])/, message: 'grants iam:* (every IAM action)' },
];

// "Action": "*", Action: '*', actions: ['*'], actions = ["*"] ...
const ACTION_STAR = /\b[Aa]ctions?["']?\s*[:=]\s*\[?\s*["']\*["']/;
const RESOURCE_STAR = /\b[Rr]esources?["']?\s*[:=]\s*\[?\s*["']\*["']/;
const PRINCIPAL = /\b[Pp]rincipals?["']?\s*[:=]/;
const STATEMENT_WINDOW = 6;

const isComment = (line) => /^\s*(#|\/\/|\*|<!--)/.test(line);

const listFiles = (dir) => {
  const out = [];
  for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
    if (entry.isDirectory()) {
      if (!SKIP_DIRS.has(entry.name)) out.push(...listFiles(path.join(dir, entry.name)));
    } else if (EXTENSIONS.has(path.extname(entry.name)) && !SKIP_FILES.has(entry.name) && !entry.name.endsWith('.min.js')) {
      const file = path.join(dir, entry.name);
      if (fs.statSync(file).size <= MAX_BYTES) out.push(file);
    }
  }
  return out;
};

const scanFile = (file) => {
  const lines = fs.readFileSync(file, 'utf-8').split(/\r?\n/);
  const findings = [];
  lines.forEach((line, i) => {
    if (isComment(line)) return;
    for (const rule of RULES) {
      if (rule.re.test(line)) findings.push({ line: i + 1, message: rule.message, text: line.trim() });
    }
    if (ACTION_STAR.test(line)) {
      const window = lines.slice(Math.max(0, i - STATEMENT_WINDOW), i + STATEMENT_WINDOW + 1).filter((l) => !isComment(l));
      if (window.some((l) => RESOURCE_STAR.test(l)) && !window.some((l) => PRINCIPAL.test(l))) {
        findings.push({ line: i + 1, message: 'grants every action on every resource', text: line.trim() });
      }
    }
  });
  return findings;
};

// Returns an array of "path:line: message" strings for one pattern folder.
const checkPatternIam = (patternDir, repoRoot) =>
  listFiles(patternDir).flatMap((file) =>
    scanFile(file).map(({ line, message, text }) => `\`${path.relative(repoRoot, file)}:${line}\` ${message}: \`${text.slice(0, 120)}\``)
  );

module.exports = { checkPatternIam };
