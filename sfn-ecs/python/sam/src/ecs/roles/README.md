# Usage

## Create the roles
```
aws iam create-role --role-name ECSTaskExecutionRole --assume-role-policy-document file://EcsTaskAssumeRolePolicyDocument.json
aws iam create-role --role-name ECSTaskRole --assume-role-policy-document file://EcsTaskAssumeRolePolicyDocument.json
```

## Create the policies
```
aws iam create-policy --policy-name ECSTaskRolePolicy --policy-document file://EcsTaskRole.json
aws iam create-policy --policy-name ECSTaskExecutionRolePolicy --policy-document file://EcsTaskExecutionRole.json
```

## Attach the policies to the roles
```
aws iam list-policies --query 'Policies[?PolicyName==`ECSTaskRolePolicy`].Arn' --output text | aws iam attach-role-policy --role-name ECSTaskRole --policy-arn 
aws iam list-policies --query 'Policies[?PolicyName==`ECSTaskExecutionRolePolicy`].Arn' --output text | aws iam attach-role-policy --role-name ECSTaskExecutionRole --policy-arn 
```
