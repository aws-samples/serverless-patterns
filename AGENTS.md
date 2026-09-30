# Agent instructions

This repo holds serverless patterns published on [Serverless Land](https://serverlessland.com/patterns). New patterns use `{family}/{language}/{framework}` folders, e.g. `sqs-lambda/python/sam`, where the family groups variants of the same services. Older patterns use single top-level folders such as `sqs-lambda-python-sam`. Folders starting with `_` and `.github/` are repo tooling.

To create or change a pattern, follow the [pattern checklist](PUBLISHING.md#pattern-checklist) in PUBLISHING.md. These rules apply on top of it:

- Before writing a new pattern, search the repo for one with the same services, in both folder styles. If one exists, add a variant to its family instead of a duplicate.
- Work in one pattern variant folder only. Start from `_pattern-model/` or a similar existing pattern. If you copy a pattern, update every reference to the original: `example-pattern.json`, README, and resource and stack names.
- Don't edit `_scripts/pattern-schema.mjs`. It's generated from serverless-land. Don't edit other files in `_scripts/`, `_pattern-model/` or `.github/` unless asked.
- Before you finish, run the pattern file check and the framework's build or synth:

    ```bash
    cd _scripts && npm i && cd ..
    node _scripts/validate.js {pattern-folder}/example-pattern.json
    ```

- Use least-privilege IAM, e.g. SAM policy templates, instead of `*` actions or resources.
- Don't hardcode account IDs, Regions, ARNs or secrets. Use parameters, pseudo parameters or environment variables.
- Keep custom code short. A pattern shows how services connect.
- Stage files by name, e.g. `git add {pattern-folder}`. Don't use `git add .` or `git add -A`.
