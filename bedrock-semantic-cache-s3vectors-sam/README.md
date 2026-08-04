# Serverless semantic cache for Amazon Bedrock (with Amazon S3 Vectors)

Return cached answers for **semantically similar** prompts — different wording still hits — so you skip the LLM call on repeats and near-repeats. Cuts Amazon Bedrock cost and latency, scales to zero, and drops in front of any model.

Learn more at Serverless Land Patterns: https://serverlessland.com/patterns/bedrock-semantic-cache-s3vectors-sam

> Important: this application uses AWS services (AWS Lambda, Amazon Bedrock, Amazon S3 Vectors, AWS Systems Manager) and there are costs associated with these services after the Free Tier usage. You are responsible for any AWS costs incurred. No warranty is implied in this example.

---

## TL;DR — read this first

- **What it is:** a Lambda in front of Amazon Bedrock that caches answers by *meaning* (not exact text). Same question asked three different ways → one Bedrock call, two instant cache hits.
- **Best for:** FAQ / support bots, docs Q&A, high-traffic assistants — anywhere many users ask the same things in different words.
- **Not for:** answers that must be exact, fresh, or per-user (unless you add namespacing / invalidation / a verify step).
- **Cost:** a cache hit skips the expensive LLM call and pays only a tiny embedding + vector query. Break-even is a few percent hit rate, so any repetitive workload is a net win.
- **Distinct from Bedrock native features:** native Prompt Caching is *exact-prefix* only (one character breaks it); Intelligent Prompt Routing picks a cheaper model. This caches by *semantic similarity* and skips the model entirely. They complement each other.

## Where it shines ✅

- **Repetitive, paraphrase-heavy traffic.** Research shows ~31% of LLM queries are semantically similar to a prior one — those become instant, free hits.
- **Latency-sensitive UX.** Measured ~7x faster on a hit (≈230 ms vs ≈1,700 ms).
- **Cost-sensitive, high-volume assistants.** Every hit is one fewer Bedrock invocation and does **not** count against your Bedrock TPM/RPM limits (throttle relief under load).
- **Any model / provider.** The cache is model-agnostic; the on-miss call is a drop-in for Bedrock or an external model.

## Where it will NOT shine ❌ (be honest)

- **Unique, one-off prompts.** No repetition → ~0 hits → you pay a tiny per-request overhead for nothing. Skip it here.
- **Answers that must be exact or fresh.** A similar-but-not-identical prompt can return a subtly different prior answer. Mitigate with a higher threshold + TTL, or bypass the cache for such routes.
- **Per-user / personalized answers.** Namespace the cache per user, or don't cache these.
- **Semantic antonyms.** The built-in negation guard catches "not / n't", but not opposites like "cheapest" vs "most expensive". For high-stakes (financial, legal, medical), add an optional LLM equivalence-verify on borderline hits.

## How it saves money regardless (the math)

Every request pays a tiny "cache tax": one embedding call (~$0.00002) + one vector query (fractions of a cent). You **save** on every HIT because you skip the LLM call (cents to dollars, especially with large prompts / RAG context / bigger models).

```
net savings = (hits x LLM cost skipped) - (all requests x tiny cache tax)
```

Because the tax is orders of magnitude smaller than an LLM call, **break-even is roughly a 1-5% hit rate.** Real repetitive workloads sit far above that, and savings **compound** as the cache warms. The only losing case is genuinely zero repetition. Plus: everything is pay-per-use and **scales to zero** (Lambda + S3 Vectors), so there is no idle cost.

---

## How it works

```
prompt --> [Lambda] --embed--> Amazon Bedrock (Titan v2 -> 1024-dim vector)
              |
              |--search--> Amazon S3 Vectors (cosine top-K; answer is stored in vector metadata)
              |                |-- HIT (sim >= threshold, fresh, current epoch, negation-parity) --> return cached answer  (~230 ms, $0 LLM)
              |                |-- MISS -->
              |--generate--> Amazon Bedrock LLM (writes the answer)
              |--store-----> Amazon S3 Vectors (embedding + answer + model + created_at + epoch)
              |--return
   (force-invalidate epoch is stored in AWS Systems Manager Parameter Store)
```

- **Amazon Bedrock** is used two ways: **embeddings** (turn text into a meaning vector so matching is semantic) and the **LLM** (answer on a miss).
- **Amazon S3 Vectors** is the cache store *and* the similarity search — pay-per-use, no always-on cost. This is the primitive that makes a serverless semantic cache economical.
- **AWS Lambda** is stateless glue. The cache lives entirely in S3 Vectors, so it survives cold starts, redeploys, and env recycling.
- **SSM Parameter Store** holds the epoch counter for force-invalidation.

### Correctness features
- **Tunable similarity threshold** (default cosine 0.85) — per-deploy and per-request.
- **Freshness TTL** — entries older than `TTL_SECONDS` are treated as a miss.
- **Force-invalidate** — bump one epoch number → every prior entry instantly misses (no deletes/scans). For big changes that can't wait for TTL.
- **Negation-parity guard** — "is X" vs "is NOT X" embed ~identically but mean the opposite; the guard blocks that false hit.
- **top-K + iterate** — a stale duplicate near-neighbour never blocks a valid hit.

## Requirements

- An AWS account with permissions for AWS Lambda, Amazon Bedrock, Amazon S3 Vectors, and AWS Systems Manager.
- [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) v2 (recent — must include the `s3vectors` and `lambda-microvms`-era models; `bedrock-runtime`).
- [AWS SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html).
- Amazon Bedrock **model access enabled** for the embeddings model (`amazon.titan-embed-text-v2:0`) and the text model (`amazon.nova-lite-v1:0`) in your Region.
- A Region where Amazon S3 Vectors and Amazon Bedrock are available (e.g. `us-east-1`).

## Deployment

S3 Vectors is not yet a CloudFormation resource, so create the vector store first (two commands), then deploy the rest with SAM.

```bash
# 1. Create the S3 Vectors bucket and a cosine index (1024 dims = Titan v2)
export VECTOR_BUCKET="semantic-cache-$(aws sts get-caller-identity --query Account --output text)"
aws s3vectors create-vector-bucket --vector-bucket-name "$VECTOR_BUCKET"
aws s3vectors create-index \
  --vector-bucket-name "$VECTOR_BUCKET" \
  --index-name prompt-cache --data-type float32 --dimension 1024 --distance-metric cosine \
  --metadata-configuration 'nonFilterableMetadataKeys=prompt,response,model,created_at,epoch'

# 2. Build and deploy the Lambda + IAM + SSM epoch parameter
sam build
sam deploy --guided
#   - VectorBucket: value of $VECTOR_BUCKET above
#   - VectorIndex : prompt-cache
#   - ApiKey      : (optional) a secret for the x-api-key header, or leave blank for IAM-only
```

Note the `FunctionUrl` and `FunctionName` outputs.

## Testing

The function URL uses AWS_IAM auth (SigV4). The simplest test is a direct invoke:

```bash
KEY="<the ApiKey you set, or omit the header if blank>"
payload() { python3 -c "import json,sys;print(json.dumps({'headers':{'x-api-key':'$KEY'},'body':json.dumps({'prompt':sys.argv[1]})}))" "$1" > ev.json; }

# MISS (calls Bedrock)
payload "What is the capital of France?"; aws lambda invoke --function-name semantic-cache --cli-binary-format raw-in-base64-out --payload file://ev.json out.json; cat out.json
sleep 6
# HIT — exact repeat  (cached=true, similarity ~1.0, ~230ms)
payload "What is the capital of France?"; aws lambda invoke --function-name semantic-cache --cli-binary-format raw-in-base64-out --payload file://ev.json out.json; cat out.json
# HIT — semantic (different words)
payload "Which city is the capital of France?"; aws lambda invoke --function-name semantic-cache --cli-binary-format raw-in-base64-out --payload file://ev.json out.json; cat out.json
```

Force-invalidate (e.g., after a data/policy change):

```bash
python3 -c "import json;print(json.dumps({'headers':{'x-api-key':'$KEY'},'body':json.dumps({'action':'invalidate'})}))" > ev.json
aws lambda invoke --function-name semantic-cache --cli-binary-format raw-in-base64-out --payload file://ev.json out.json; cat out.json
# -> {"invalidated": true, "epoch": N}. Every prior answer now misses (propagates within ~30s).
```

Expected: exact/semantic repeats HIT (`cached=true` with a similarity score); unrelated prompts MISS; after `invalidate`, the same prompt MISSes once, then HITs again once re-cached.

## Tuning

| Setting | Env var / request field | Effect |
|---|---|---|
| Similarity threshold | `SIM_THRESHOLD` (deploy) or `threshold` (per request) | Higher = stricter matching, fewer but safer hits |
| Freshness | `TTL_SECONDS` | Max age of a served answer |
| Force-invalidate | `POST {"action":"invalidate"}` | Invalidate the whole cache instantly |
| Models | `EMBED_MODEL`, `LLM_MODEL` | Swap embeddings / answer model |

## Cleanup

```bash
sam delete
aws s3vectors delete-index --vector-bucket-name "$VECTOR_BUCKET" --index-name prompt-cache
aws s3vectors delete-vector-bucket --vector-bucket-name "$VECTOR_BUCKET"
aws ssm delete-parameter --name /semantic-cache/epoch
```

---

Author: Manish S

Copyright 2026 Amazon.com, Inc. or its affiliates. All Rights Reserved. SPDX-License-Identifier: MIT-0
