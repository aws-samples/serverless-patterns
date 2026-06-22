#!/usr/bin/env python3
"""
CloudFormation Template Validator
Validates the structure and completeness of CloudFormation templates.
"""

import yaml
import sys
import re

# Custom YAML loader that handles CloudFormation intrinsic functions
class CFNLoader(yaml.SafeLoader):
    pass

def cfn_constructor(loader, tag_suffix, node):
    """Handle CloudFormation intrinsic functions."""
    if isinstance(node, yaml.ScalarNode):
        return {tag_suffix: loader.construct_scalar(node)}
    elif isinstance(node, yaml.SequenceNode):
        return {tag_suffix: loader.construct_sequence(node)}
    elif isinstance(node, yaml.MappingNode):
        return {tag_suffix: loader.construct_mapping(node)}
    return {tag_suffix: None}

# Register CloudFormation intrinsic functions
CFNLoader.add_multi_constructor('!', cfn_constructor)

def validate_template(template_path):
    """Validate CloudFormation template structure and completeness."""
    
    print(f"Validating CloudFormation template: {template_path}\n")
    
    try:
        with open(template_path, 'r') as f:
            template = yaml.load(f, Loader=CFNLoader)
        
        errors = []
        warnings = []
        
        # 1. Validate basic structure
        print("=" * 60)
        print("1. BASIC STRUCTURE VALIDATION")
        print("=" * 60)
        
        required_sections = ['AWSTemplateFormatVersion', 'Description', 'Parameters', 'Resources', 'Outputs']
        for section in required_sections:
            if section in template:
                print(f"✓ {section} section present")
            else:
                errors.append(f"Missing required section: {section}")
                print(f"✗ {section} section MISSING")
        
        # 2. Validate parameters
        print("\n" + "=" * 60)
        print("2. PARAMETERS VALIDATION")
        print("=" * 60)
        
        params = template.get('Parameters', {})
        print(f"Total parameters: {len(params)}")
        
        required_params = ['EnvironmentName', 'Region']
        for param in required_params:
            if param in params:
                param_config = params[param]
                print(f"✓ {param}")
                print(f"  Type: {param_config.get('Type')}")
                print(f"  Default: {param_config.get('Default', 'N/A')}")
            else:
                errors.append(f"Missing required parameter: {param}")
                print(f"✗ {param} MISSING")
        
        # 3. Validate resources
        print("\n" + "=" * 60)
        print("3. RESOURCES VALIDATION")
        print("=" * 60)
        
        resources = template.get('Resources', {})
        print(f"Total resources: {len(resources)}\n")
        
        # Group resources by type
        resource_types = {}
        for res_name, res_config in resources.items():
            res_type = res_config.get('Type', 'Unknown')
            if res_type not in resource_types:
                resource_types[res_type] = []
            resource_types[res_type].append(res_name)
        
        print("Resources by type:")
        for res_type, res_names in sorted(resource_types.items()):
            print(f"\n{res_type}: {len(res_names)}")
            for name in res_names:
                print(f"  - {name}")
        
        # Check for required resources
        print("\n" + "-" * 60)
        print("Required Resources Check:")
        print("-" * 60)
        
        required_resources = {
            'AgentCoreGateway': 'AWS::BedrockAgentCore::Gateway',
            'AgentCoreMemory': 'AWS::BedrockAgentCore::Memory',
            'AgentLambda': 'AWS::Lambda::Function',
            'InterceptorLambda': 'AWS::Lambda::Function',
            'ToolLambda': 'AWS::Lambda::Function',
            'S3ListBucketsTarget': 'AWS::BedrockAgentCore::GatewayTarget',
            'GatewayExecutionRole': 'AWS::IAM::Role',
            'AgentLambdaRole': 'AWS::IAM::Role',
            'InterceptorLambdaRole': 'AWS::IAM::Role',
            'ToolLambdaRole': 'AWS::IAM::Role',
            'CognitoUserPool': 'AWS::Cognito::UserPool',
            'CognitoUserPoolClient': 'AWS::Cognito::UserPoolClient'
        }
        
        for res_name, expected_type in required_resources.items():
            if res_name in resources:
                actual_type = resources[res_name].get('Type')
                if actual_type == expected_type:
                    print(f"✓ {res_name} ({expected_type})")
                else:
                    errors.append(f"{res_name}: Expected {expected_type}, got {actual_type}")
                    print(f"✗ {res_name} - Expected {expected_type}, got {actual_type}")
            else:
                errors.append(f"Missing required resource: {res_name}")
                print(f"✗ {res_name} - MISSING")
        
        # 4. Validate Lambda configurations
        print("\n" + "=" * 60)
        print("4. LAMBDA CONFIGURATION VALIDATION")
        print("=" * 60)
        
        lambda_configs = {
            'AgentLambda': {
                'Runtime': 'python3.12',
                'Timeout': 30,
                'MemorySize': 512,
                'RequiredEnvVars': ['COGNITO_JWKS_URL', 'GATEWAY_ID', 'MEMORY_ID', 'BEDROCK_MODEL_ID', 'AWS_REGION']
            },
            'InterceptorLambda': {
                'Runtime': 'python3.12',
                'Timeout': 5,
                'MemorySize': 256,
                'RequiredEnvVars': ['LOG_LEVEL', 'AWS_REGION']
            },
            'ToolLambda': {
                'Runtime': 'python3.12',
                'Timeout': 10,
                'MemorySize': 256,
                'RequiredEnvVars': ['LOG_LEVEL', 'AWS_REGION']
            }
        }
        
        for lambda_name, expected_config in lambda_configs.items():
            if lambda_name in resources:
                lambda_res = resources[lambda_name]
                props = lambda_res.get('Properties', {})
                
                print(f"\n{lambda_name}:")
                
                # Check runtime
                runtime = props.get('Runtime')
                if runtime == expected_config['Runtime']:
                    print(f"  ✓ Runtime: {runtime}")
                else:
                    warnings.append(f"{lambda_name}: Runtime is {runtime}, expected {expected_config['Runtime']}")
                    print(f"  ⚠ Runtime: {runtime} (expected {expected_config['Runtime']})")
                
                # Check timeout
                timeout = props.get('Timeout')
                if timeout == expected_config['Timeout']:
                    print(f"  ✓ Timeout: {timeout}s")
                else:
                    warnings.append(f"{lambda_name}: Timeout is {timeout}s, expected {expected_config['Timeout']}s")
                    print(f"  ⚠ Timeout: {timeout}s (expected {expected_config['Timeout']}s)")
                
                # Check memory
                memory = props.get('MemorySize')
                if memory == expected_config['MemorySize']:
                    print(f"  ✓ Memory: {memory}MB")
                else:
                    warnings.append(f"{lambda_name}: Memory is {memory}MB, expected {expected_config['MemorySize']}MB")
                    print(f"  ⚠ Memory: {memory}MB (expected {expected_config['MemorySize']}MB)")
                
                # Check VPC config (should NOT be present)
                if 'VpcConfig' in props:
                    errors.append(f"{lambda_name}: Should NOT have VPC configuration")
                    print(f"  ✗ VPC Config: Present (should be absent)")
                else:
                    print(f"  ✓ VPC Config: Absent (correct)")
                
                # Check environment variables
                env_vars = props.get('Environment', {}).get('Variables', {})
                print(f"  Environment Variables:")
                for var in expected_config['RequiredEnvVars']:
                    if var in env_vars:
                        print(f"    ✓ {var}")
                    else:
                        errors.append(f"{lambda_name}: Missing environment variable {var}")
                        print(f"    ✗ {var} MISSING")
        
        # 5. Validate outputs
        print("\n" + "=" * 60)
        print("5. OUTPUTS VALIDATION")
        print("=" * 60)
        
        outputs = template.get('Outputs', {})
        print(f"Total outputs: {len(outputs)}\n")
        
        required_outputs = [
            'GatewayId',
            'MemoryId',
            'CognitoUserPoolId',
            'AgentLambdaArn',
            'InterceptorLambdaArn',
            'ToolLambdaArn'
        ]
        
        for output in required_outputs:
            if output in outputs:
                print(f"✓ {output}")
            else:
                errors.append(f"Missing required output: {output}")
                print(f"✗ {output} MISSING")
        
        # 6. Validate CloudWatch logging
        print("\n" + "=" * 60)
        print("6. CLOUDWATCH LOGGING VALIDATION")
        print("=" * 60)
        
        log_groups = [
            'AgentLambdaLogGroup',
            'InterceptorLambdaLogGroup',
            'ToolLambdaLogGroup'
        ]
        
        for log_group in log_groups:
            if log_group in resources:
                log_res = resources[log_group]
                props = log_res.get('Properties', {})
                retention = props.get('RetentionInDays')
                
                if retention == 30:
                    print(f"✓ {log_group} (retention: {retention} days)")
                else:
                    warnings.append(f"{log_group}: Retention is {retention} days, expected 30 days")
                    print(f"⚠ {log_group} (retention: {retention} days, expected 30)")
            else:
                errors.append(f"Missing log group: {log_group}")
                print(f"✗ {log_group} MISSING")
        
        # 7. Validate CloudWatch alarms
        print("\n" + "=" * 60)
        print("7. CLOUDWATCH ALARMS VALIDATION")
        print("=" * 60)
        
        alarm_count = sum(1 for r in resources.values() if r.get('Type') == 'AWS::CloudWatch::Alarm')
        print(f"Total alarms: {alarm_count}")
        
        expected_alarms = [
            'AgentLambdaErrorAlarm',
            'AgentLambdaDurationAlarm',
            'AgentLambdaThrottleAlarm',
            'InterceptorLambdaErrorAlarm',
            'InterceptorLambdaDurationAlarm',
            'ToolLambdaErrorAlarm',
            'ToolLambdaDurationAlarm'
        ]
        
        for alarm in expected_alarms:
            if alarm in resources:
                print(f"✓ {alarm}")
            else:
                warnings.append(f"Missing recommended alarm: {alarm}")
                print(f"⚠ {alarm} MISSING (recommended)")
        
        # 8. Validate Gateway configuration
        print("\n" + "=" * 60)
        print("8. GATEWAY CONFIGURATION VALIDATION")
        print("=" * 60)
        
        if 'AgentCoreGateway' in resources:
            gateway = resources['AgentCoreGateway']
            props = gateway.get('Properties', {})
            
            # Check authorizer type
            auth_type = props.get('AuthorizerType')
            if auth_type == 'CUSTOM_JWT':
                print("✓ Authorizer Type: CUSTOM_JWT")
                
                # Check authorizer configuration
                auth_config = props.get('AuthorizerConfiguration', {})
                custom_jwt = auth_config.get('CustomJWTAuthorizer', {})
                if 'DiscoveryUrl' in custom_jwt:
                    print("✓ CustomJWTAuthorizer DiscoveryUrl configured")
                else:
                    errors.append("Gateway CustomJWTAuthorizer missing DiscoveryUrl")
                    print("✗ CustomJWTAuthorizer DiscoveryUrl MISSING")
            else:
                warnings.append(f"Gateway AuthorizerType is {auth_type}, expected CUSTOM_JWT")
                print(f"⚠ Authorizer Type: {auth_type} (expected CUSTOM_JWT)")
            
            # Check interceptor configuration
            interceptor_configs = props.get('InterceptorConfigurations', [])
            if interceptor_configs:
                print(f"✓ InterceptorConfigurations: {len(interceptor_configs)} configured")
                for idx, config in enumerate(interceptor_configs):
                    interceptor_type = config.get('InterceptorType')
                    if interceptor_type == 'REQUEST':
                        print(f"  ✓ Interceptor {idx+1}: REQUEST type")
                    else:
                        warnings.append(f"Interceptor {idx+1}: Type is {interceptor_type}, expected REQUEST")
                        print(f"  ⚠ Interceptor {idx+1}: {interceptor_type} (expected REQUEST)")
            else:
                warnings.append("Gateway has no InterceptorConfigurations")
                print("⚠ InterceptorConfigurations: None configured")
        
        # 9. Validate Gateway Target inline schema
        print("\n" + "=" * 60)
        print("9. GATEWAY TARGET INLINE SCHEMA VALIDATION")
        print("=" * 60)
        
        if 'S3ListBucketsTarget' in resources:
            target = resources['S3ListBucketsTarget']
            props = target.get('Properties', {})
            
            if 'InlineSchema' in props:
                print("✓ Inline schema present")
                schema = props['InlineSchema']
                
                # Check schema structure
                if 'properties' in schema:
                    schema_props = schema['properties']
                    required_props = ['toolName', 'description', 'parameters', 'returns']
                    
                    for prop in required_props:
                        if prop in schema_props:
                            print(f"  ✓ {prop}")
                        else:
                            errors.append(f"Gateway Target schema missing property: {prop}")
                            print(f"  ✗ {prop} MISSING")
                    
                    # Check user_context in parameters
                    if 'parameters' in schema_props:
                        params_props = schema_props['parameters'].get('properties', {})
                        if 'user_context' in params_props:
                            print("  ✓ user_context in parameters")
                        else:
                            errors.append("Gateway Target schema parameters should include user_context")
                            print("  ✗ user_context MISSING in parameters")
                else:
                    errors.append("Gateway Target inline schema missing properties")
                    print("✗ Schema properties MISSING")
            else:
                errors.append("Gateway Target should use inline schema")
                print("✗ Inline schema MISSING")
        
        # 10. Validate IAM permissions
        print("\n" + "=" * 60)
        print("10. IAM PERMISSIONS VALIDATION")
        print("=" * 60)
        
        # Check Agent Lambda permissions
        if 'AgentLambdaRole' in resources:
            role = resources['AgentLambdaRole']
            policies = role.get('Properties', {}).get('Policies', [])
            
            print("AgentLambdaRole permissions:")
            required_actions = ['bedrock:InvokeModel', 'bedrock-agent-runtime:InvokeTool', 'bedrock-agent-runtime:PutMemory']
            
            all_actions = []
            for policy in policies:
                statements = policy.get('PolicyDocument', {}).get('Statement', [])
                for stmt in statements:
                    all_actions.extend(stmt.get('Action', []))
            
            for action in required_actions:
                if action in all_actions:
                    print(f"  ✓ {action}")
                else:
                    warnings.append(f"AgentLambdaRole missing recommended permission: {action}")
                    print(f"  ⚠ {action} MISSING (recommended)")
        
        # Check Tool Lambda permissions
        if 'ToolLambdaRole' in resources:
            role = resources['ToolLambdaRole']
            policies = role.get('Properties', {}).get('Policies', [])
            
            print("\nToolLambdaRole permissions:")
            required_actions = ['s3:ListAllMyBuckets', 's3:GetBucketLocation']
            
            all_actions = []
            for policy in policies:
                statements = policy.get('PolicyDocument', {}).get('Statement', [])
                for stmt in statements:
                    all_actions.extend(stmt.get('Action', []))
            
            for action in required_actions:
                if action in all_actions:
                    print(f"  ✓ {action}")
                else:
                    errors.append(f"ToolLambdaRole missing required permission: {action}")
                    print(f"  ✗ {action} MISSING")
        
        # Summary
        print("\n" + "=" * 60)
        print("VALIDATION SUMMARY")
        print("=" * 60)
        
        if errors:
            print(f"\n❌ ERRORS: {len(errors)}")
            for error in errors:
                print(f"  - {error}")
        
        if warnings:
            print(f"\n⚠️  WARNINGS: {len(warnings)}")
            for warning in warnings:
                print(f"  - {warning}")
        
        if not errors and not warnings:
            print("\n✅ Template validation PASSED - No errors or warnings")
            return 0
        elif not errors:
            print("\n✅ Template validation PASSED - No errors (warnings present)")
            return 0
        else:
            print("\n❌ Template validation FAILED - Errors found")
            return 1
        
    except yaml.YAMLError as e:
        print(f"\n❌ YAML SYNTAX ERROR: {e}")
        return 1
    except FileNotFoundError:
        print(f"\n❌ FILE NOT FOUND: {template_path}")
        return 1
    except Exception as e:
        print(f"\n❌ VALIDATION ERROR: {e}")
        import traceback
        traceback.print_exc()
        return 1

if __name__ == '__main__':
    template_path = 'infrastructure/cloudformation-template.yaml'
    sys.exit(validate_template(template_path))
