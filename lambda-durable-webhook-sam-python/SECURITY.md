# Security Guide - Lambda Durable Webhook Pattern

## 🔒 Security Overview

This pattern implements multiple security layers to protect your webhook endpoint from unauthorized access and abuse.

---

## Current Security Features

### 1. Transport Security ✅
- **HTTPS/TLS 1.2+**: All API Gateway endpoints use TLS encryption
- **Certificate Management**: Handled automatically by AWS

### 2. Authentication ✅
- **HMAC-SHA256 Signature Validation**: Validates webhook authenticity
- **Configurable Secret**: Set via CloudFormation parameter
- **Constant-Time Comparison**: Prevents timing attacks

### 3. Authorization ✅
- **IAM Least Privilege**: Each Lambda has minimal required permissions
- **Resource-Based Policies**: API Gateway can only invoke specific functions

### 4. Data Protection ✅
- **Encryption at Rest**: DynamoDB uses AWS-managed encryption
- **Encryption in Transit**: TLS for all communications
- **TTL for Data Cleanup**: Automatic deletion after 7 days

### 5. Audit & Monitoring ✅
- **CloudWatch Logs**: All requests logged
- **Structured Logging**: JSON format for easy parsing
- **Execution Tracking**: Unique tokens for each webhook

---

## Security Architecture

```
┌─────────────┐
│   Internet  │
└──────┬──────┘
       │ HTTPS/TLS
       ▼
┌─────────────────────┐
│   API Gateway       │
│  - CORS configured  │
│  - Rate limiting*   │
└──────┬──────────────┘
       │
       ▼
┌─────────────────────┐
│ Validator Lambda    │
│  - HMAC validation  │
│  - JSON validation  │
│  - Sync response    │
└──────┬──────────────┘
       │ Async invoke
       ▼
┌─────────────────────┐
│ Processor Lambda    │
│  - Durable exec     │
│  - Checkpointing    │
└──────┬──────────────┘
       │
       ▼
┌─────────────────────┐
│    DynamoDB         │
│  - Encrypted        │
│  - TTL enabled      │
└─────────────────────┘

* Recommended for production
```

---

## HMAC Signature Validation

### How It Works

1. **Webhook Provider** calculates HMAC-SHA256 of request body using shared secret
2. **Sends signature** in `X-Hub-Signature-256` header (format: `sha256=<hash>`)
3. **Validator Lambda** recalculates signature and compares
4. **Rejects** requests with invalid/missing signatures (if secret configured)

### Implementation

```python
def validate_signature(payload: str, signature: str, secret: str) -> bool:
    """Validate HMAC-SHA256 signature"""
    if not secret or not signature:
        return True  # Skip if not configured
    
    if signature.startswith('sha256='):
        signature = signature[7:]
    
    expected = hmac.new(
        secret.encode('utf-8'),
        payload.encode('utf-8'),
        hashlib.sha256
    ).hexdigest()
    
    return hmac.compare_digest(expected, signature)  # Constant-time comparison
```

### Configuration

```bash
# Deploy with HMAC validation enabled
sam deploy --parameter-overrides WebhookSecret=your-secret-key-here

# Test with signature
PAYLOAD='{"type":"test"}'
SIGNATURE=$(echo -n "$PAYLOAD" | openssl dgst -sha256 -hmac "your-secret-key-here" | cut -d' ' -f2)

curl -X POST $ENDPOINT/webhook \
  -H "Content-Type: application/json" \
  -H "X-Hub-Signature-256: sha256=$SIGNATURE" \
  -d "$PAYLOAD"
```

---

## Additional Security Recommendations

### 1. API Gateway Rate Limiting

Protect against DDoS and abuse:

```bash
# Create usage plan
aws apigateway create-usage-plan \
  --name webhook-rate-limit \
  --throttle burstLimit=100,rateLimit=50 \
  --region us-east-2

# Associate with API stage
aws apigateway create-usage-plan-key \
  --usage-plan-id <plan-id> \
  --key-id <api-key-id> \
  --key-type API_KEY
```

**Recommended Limits:**
- **Rate**: 50 requests/second
- **Burst**: 100 requests
- **Quota**: 100,000 requests/day

### 2. API Keys (Optional)

Add an additional authentication layer:

```bash
# Create API key
aws apigateway create-api-key \
  --name webhook-api-key \
  --enabled

# Require API key in template.yaml
WebhookApi:
  Type: AWS::Serverless::Api
  Properties:
    Auth:
      ApiKeyRequired: true
```

### 3. IP Whitelisting

Restrict access to known webhook providers:

```yaml
# Add to template.yaml
WebhookApi:
  Type: AWS::Serverless::Api
  Properties:
    ResourcePolicy:
      IpRangeWhitelist:
        - "192.0.2.0/24"  # Example IP range
        - "198.51.100.0/24"
```

### 4. AWS WAF

Protect against common web exploits:

```bash
# Create WAF Web ACL
aws wafv2 create-web-acl \
  --name webhook-waf \
  --scope REGIONAL \
  --region us-east-2 \
  --default-action Allow={} \
  --rules file://waf-rules.json

# Associate with API Gateway
aws wafv2 associate-web-acl \
  --web-acl-arn <waf-arn> \
  --resource-arn <api-gateway-arn>
```

**Recommended WAF Rules:**
- Rate-based rule (1000 req/5min per IP)
- SQL injection protection
- XSS protection
- Known bad inputs

### 5. CloudWatch Alarms

Monitor for security events:

```bash
# Alarm for high error rate
aws cloudwatch put-metric-alarm \
  --alarm-name webhook-high-errors \
  --metric-name 4XXError \
  --namespace AWS/ApiGateway \
  --statistic Sum \
  --period 300 \
  --threshold 100 \
  --comparison-operator GreaterThanThreshold

# Alarm for unauthorized attempts
aws logs put-metric-filter \
  --log-group-name /aws/lambda/webhook-validator \
  --filter-name UnauthorizedAttempts \
  --filter-pattern "[..., status=401]" \
  --metric-transformations \
      metricName=UnauthorizedWebhooks,metricNamespace=CustomMetrics,metricValue=1
```

### 6. Secrets Management

Use AWS Secrets Manager for webhook secrets:

```yaml
# In template.yaml
Parameters:
  WebhookSecretArn:
    Type: String
    Description: ARN of secret in Secrets Manager

Resources:
  WebhookValidatorFunction:
    Environment:
      Variables:
        SECRET_ARN: !Ref WebhookSecretArn
    Policies:
      - Statement:
        - Effect: Allow
          Action: secretsmanager:GetSecretValue
          Resource: !Ref WebhookSecretArn
```

```python
# In code
import boto3
secrets = boto3.client('secretsmanager')
secret = secrets.get_secret_value(SecretId=os.environ['SECRET_ARN'])
webhook_secret = json.loads(secret['SecretString'])['webhook_secret']
```

---

## Security Testing

### Test HMAC Validation

```bash
# Valid signature
PAYLOAD='{"type":"test"}'
SECRET="test-secret-12345"
SIG=$(echo -n "$PAYLOAD" | openssl dgst -sha256 -hmac "$SECRET" | awk '{print $2}')

curl -X POST $ENDPOINT/webhook \
  -H "Content-Type: application/json" \
  -H "X-Hub-Signature-256: sha256=$SIG" \
  -d "$PAYLOAD"
# Expected: 202 Accepted

# Invalid signature
curl -X POST $ENDPOINT/webhook \
  -H "Content-Type: application/json" \
  -H "X-Hub-Signature-256: sha256=invalid" \
  -d "$PAYLOAD"
# Expected: 401 Unauthorized
```

### Test Rate Limiting

```bash
# Send 100 requests rapidly
for i in {1..100}; do
  curl -X POST $ENDPOINT/webhook \
    -H "Content-Type: application/json" \
    -d '{"type":"test"}' &
done
wait
# Expected: Some requests return 429 Too Many Requests
```

### Test Invalid Payloads

```bash
# Malformed JSON
curl -X POST $ENDPOINT/webhook \
  -H "Content-Type: application/json" \
  -d 'not json'
# Expected: 400 Bad Request

# SQL injection attempt
curl -X POST $ENDPOINT/webhook \
  -H "Content-Type: application/json" \
  -d '{"type":"test","data":"'; DROP TABLE users;--"}'
# Expected: 202 Accepted (but safely handled)
```

---

## Compliance Considerations

### GDPR
- **Data Minimization**: Only store necessary webhook data
- **Right to Erasure**: TTL ensures automatic deletion
- **Data Encryption**: At rest and in transit

### PCI DSS
- **No Card Data**: Never log or store full card numbers
- **Encryption**: TLS 1.2+ required
- **Access Control**: IAM policies enforce least privilege

### SOC 2
- **Audit Logging**: CloudWatch logs all access
- **Monitoring**: CloudWatch alarms for anomalies
- **Encryption**: AWS-managed keys

---

## Incident Response

### Suspected Compromise

1. **Rotate webhook secret immediately**:
   ```bash
   aws ssm put-parameter --name /webhook/secret \
     --value "new-secret-$(openssl rand -hex 32)" \
     --overwrite
   ```

2. **Review CloudWatch logs**:
   ```bash
   aws logs filter-log-events \
     --log-group-name /aws/lambda/webhook-validator \
     --start-time $(date -d '1 hour ago' +%s)000 \
     --filter-pattern "[..., status=401]"
   ```

3. **Block malicious IPs**:
   ```bash
   # Add to WAF IP set
   aws wafv2 update-ip-set \
     --id <ip-set-id> \
     --addresses "192.0.2.1/32"
   ```

4. **Enable detailed logging**:
   ```bash
   aws apigateway update-stage \
     --rest-api-id <api-id> \
     --stage-name prod \
     --patch-operations \
       op=replace,path=/accessLogSettings/destinationArn,value=<log-arn>
   ```

---

## Security Checklist

### Pre-Production
- [ ] Set strong webhook secret (32+ characters)
- [ ] Enable API Gateway logging
- [ ] Configure CloudWatch alarms
- [ ] Test HMAC validation
- [ ] Review IAM policies
- [ ] Enable AWS Config rules

### Production
- [ ] Implement rate limiting
- [ ] Add WAF protection
- [ ] Set up monitoring dashboard
- [ ] Document incident response
- [ ] Regular security reviews
- [ ] Penetration testing

### Ongoing
- [ ] Rotate secrets quarterly
- [ ] Review CloudWatch logs weekly
- [ ] Update dependencies monthly
- [ ] Security audit annually

---

## References

- [AWS API Gateway Security](https://docs.aws.amazon.com/apigateway/latest/developerguide/security.html)
- [Lambda Security Best Practices](https://docs.aws.amazon.com/lambda/latest/dg/lambda-security.html)
- [DynamoDB Encryption](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/encryption.howitworks.html)
- [OWASP API Security Top 10](https://owasp.org/www-project-api-security/)
