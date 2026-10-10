"""Unit tests for OpenAPI parser module."""

import pytest
from src.openapi_parser import (
    parse_openapi_spec,
    extract_operation_tool,
    convert_to_json_schema,
    OpenAPIParseError
)
from src.shared.models import ToolDefinition


class TestParseOpenAPISpec:
    """Tests for parse_openapi_spec function."""
    
    def test_parse_minimal_valid_spec(self):
        """Test parsing a minimal valid OpenAPI 3.0 specification."""
        spec = {
            'openapi': '3.0.0',
            'info': {'title': 'Test API', 'version': '1.0.0'},
            'paths': {
                '/test': {
                    'get': {
                        'operationId': 'getTest',
                        'summary': 'Get test data',
                        'responses': {
                            '200': {
                                'description': 'Success',
                                'content': {
                                    'application/json': {
                                        'schema': {'type': 'object'}
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
        
        tools = parse_openapi_spec(spec)
        
        assert len(tools) == 1
        assert tools[0].name == 'getTest'
        assert tools[0].description == 'Get test data'
        assert tools[0].input_schema['type'] == 'object'
        assert tools[0].output_schema['type'] == 'object'
    
    def test_parse_openapi_3_1_spec(self):
        """Test parsing OpenAPI 3.1.x specification."""
        spec = {
            'openapi': '3.1.0',
            'info': {'title': 'Test API', 'version': '1.0.0'},
            'paths': {
                '/test': {
                    'get': {
                        'operationId': 'getTest',
                        'summary': 'Get test',
                        'responses': {'200': {'description': 'Success'}}
                    }
                }
            }
        }
        
        tools = parse_openapi_spec(spec)
        assert len(tools) == 1
    
    def test_missing_openapi_field(self):
        """Test error when 'openapi' field is missing."""
        spec = {
            'info': {'title': 'Test API', 'version': '1.0.0'},
            'paths': {}
        }
        
        with pytest.raises(OpenAPIParseError, match="Missing 'openapi' field"):
            parse_openapi_spec(spec)
    
    def test_unsupported_openapi_version(self):
        """Test error for unsupported OpenAPI version."""
        spec = {
            'openapi': '2.0',
            'info': {'title': 'Test API', 'version': '1.0.0'},
            'paths': {}
        }
        
        with pytest.raises(OpenAPIParseError, match="Unsupported OpenAPI version"):
            parse_openapi_spec(spec)
    
    def test_missing_paths_field(self):
        """Test error when 'paths' field is missing."""
        spec = {
            'openapi': '3.0.0',
            'info': {'title': 'Test API', 'version': '1.0.0'}
        }
        
        with pytest.raises(OpenAPIParseError, match="No valid operations found"):
            parse_openapi_spec(spec)
    
    def test_empty_paths(self):
        """Test error when paths is empty."""
        spec = {
            'openapi': '3.0.0',
            'info': {'title': 'Test API', 'version': '1.0.0'},
            'paths': {}
        }
        
        with pytest.raises(OpenAPIParseError, match="No valid operations found"):
            parse_openapi_spec(spec)
    
    def test_multiple_operations(self):
        """Test parsing spec with multiple operations."""
        spec = {
            'openapi': '3.0.0',
            'info': {'title': 'Test API', 'version': '1.0.0'},
            'paths': {
                '/users': {
                    'get': {
                        'operationId': 'listUsers',
                        'summary': 'List users',
                        'responses': {'200': {'description': 'Success'}}
                    },
                    'post': {
                        'operationId': 'createUser',
                        'summary': 'Create user',
                        'responses': {'201': {'description': 'Created'}}
                    }
                },
                '/users/{id}': {
                    'get': {
                        'operationId': 'getUser',
                        'summary': 'Get user',
                        'responses': {'200': {'description': 'Success'}}
                    }
                }
            }
        }
        
        tools = parse_openapi_spec(spec)
        
        assert len(tools) == 3
        tool_names = [t.name for t in tools]
        assert 'listUsers' in tool_names
        assert 'createUser' in tool_names
        assert 'getUser' in tool_names


class TestExtractOperationTool:
    """Tests for extract_operation_tool function."""
    
    def test_extract_with_operation_id(self):
        """Test extraction when operationId is present."""
        operation = {
            'operationId': 'getCurrentWeather',
            'summary': 'Get current weather',
            'responses': {'200': {'description': 'Success'}}
        }
        
        tool = extract_operation_tool('/weather', 'get', operation)
        
        assert tool.name == 'getCurrentWeather'
        assert tool.description == 'Get current weather'
    
    def test_extract_without_operation_id(self):
        """Test extraction generates name from method and path."""
        operation = {
            'summary': 'Get weather',
            'responses': {'200': {'description': 'Success'}}
        }
        
        tool = extract_operation_tool('/weather', 'get', operation)
        
        assert tool.name == 'get_weather'
    
    def test_extract_with_path_parameters(self):
        """Test extraction with path parameters in URL."""
        operation = {
            'summary': 'Get user',
            'responses': {'200': {'description': 'Success'}}
        }
        
        tool = extract_operation_tool('/users/{id}', 'get', operation)
        
        assert tool.name == 'get_users_id'
    
    def test_extract_with_parameters(self):
        """Test extraction with query parameters."""
        operation = {
            'operationId': 'searchUsers',
            'summary': 'Search users',
            'parameters': [
                {
                    'name': 'query',
                    'in': 'query',
                    'required': True,
                    'schema': {'type': 'string'}
                },
                {
                    'name': 'limit',
                    'in': 'query',
                    'required': False,
                    'schema': {'type': 'integer'}
                }
            ],
            'responses': {'200': {'description': 'Success'}}
        }
        
        tool = extract_operation_tool('/users/search', 'get', operation)
        
        assert 'query' in tool.input_schema['properties']
        assert 'limit' in tool.input_schema['properties']
        assert 'query' in tool.input_schema['required']
        assert 'limit' not in tool.input_schema['required']
    
    def test_extract_with_request_body(self):
        """Test extraction with requestBody."""
        operation = {
            'operationId': 'createUser',
            'summary': 'Create user',
            'requestBody': {
                'required': True,
                'content': {
                    'application/json': {
                        'schema': {
                            'type': 'object',
                            'properties': {
                                'name': {'type': 'string'},
                                'email': {'type': 'string'}
                            },
                            'required': ['name', 'email']
                        }
                    }
                }
            },
            'responses': {'201': {'description': 'Created'}}
        }
        
        tool = extract_operation_tool('/users', 'post', operation)
        
        assert 'name' in tool.input_schema['properties']
        assert 'email' in tool.input_schema['properties']
        assert 'name' in tool.input_schema['required']
        assert 'email' in tool.input_schema['required']
    
    def test_extract_with_security(self):
        """Test extraction preserves security requirements."""
        operation = {
            'operationId': 'getProtected',
            'summary': 'Get protected resource',
            'security': [{'bearerAuth': []}],
            'responses': {'200': {'description': 'Success'}}
        }
        
        tool = extract_operation_tool('/protected', 'get', operation)
        
        assert tool.security == [{'bearerAuth': []}]
    
    def test_extract_uses_description_fallback(self):
        """Test extraction uses description when summary is missing."""
        operation = {
            'operationId': 'getTest',
            'description': 'This is a test endpoint',
            'responses': {'200': {'description': 'Success'}}
        }
        
        tool = extract_operation_tool('/test', 'get', operation)
        
        assert tool.description == 'This is a test endpoint'
    
    def test_extract_generates_description_fallback(self):
        """Test extraction generates description when both summary and description are missing."""
        operation = {
            'operationId': 'getTest',
            'responses': {'200': {'description': 'Success'}}
        }
        
        tool = extract_operation_tool('/test', 'get', operation)
        
        assert tool.description == 'GET /test'


class TestConvertToJsonSchema:
    """Tests for convert_to_json_schema function."""
    
    def test_convert_simple_type(self):
        """Test conversion of simple type."""
        openapi_schema = {'type': 'string'}
        
        json_schema = convert_to_json_schema(openapi_schema)
        
        assert json_schema == {'type': 'string'}
    
    def test_convert_with_format(self):
        """Test conversion preserves format."""
        openapi_schema = {'type': 'string', 'format': 'date-time'}
        
        json_schema = convert_to_json_schema(openapi_schema)
        
        assert json_schema['type'] == 'string'
        assert json_schema['format'] == 'date-time'
    
    def test_convert_object_with_properties(self):
        """Test conversion of object with properties."""
        openapi_schema = {
            'type': 'object',
            'properties': {
                'name': {'type': 'string'},
                'age': {'type': 'integer'}
            },
            'required': ['name']
        }
        
        json_schema = convert_to_json_schema(openapi_schema)
        
        assert json_schema['type'] == 'object'
        assert 'name' in json_schema['properties']
        assert 'age' in json_schema['properties']
        assert json_schema['required'] == ['name']
    
    def test_convert_array_with_items(self):
        """Test conversion of array with items."""
        openapi_schema = {
            'type': 'array',
            'items': {'type': 'string'}
        }
        
        json_schema = convert_to_json_schema(openapi_schema)
        
        assert json_schema['type'] == 'array'
        assert json_schema['items']['type'] == 'string'
    
    def test_convert_nullable(self):
        """Test conversion of nullable type (OpenAPI 3.0.x)."""
        openapi_schema = {
            'type': 'string',
            'nullable': True
        }
        
        json_schema = convert_to_json_schema(openapi_schema)
        
        assert 'oneOf' in json_schema
        assert {'type': 'string'} in json_schema['oneOf']
        assert {'type': 'null'} in json_schema['oneOf']
    
    def test_convert_enum(self):
        """Test conversion preserves enum."""
        openapi_schema = {
            'type': 'string',
            'enum': ['red', 'green', 'blue']
        }
        
        json_schema = convert_to_json_schema(openapi_schema)
        
        assert json_schema['enum'] == ['red', 'green', 'blue']
    
    def test_convert_with_ref(self):
        """Test conversion resolves $ref."""
        components = {
            'schemas': {
                'User': {
                    'type': 'object',
                    'properties': {
                        'name': {'type': 'string'}
                    }
                }
            }
        }
        openapi_schema = {'$ref': '#/components/schemas/User'}
        
        json_schema = convert_to_json_schema(openapi_schema, components)
        
        assert json_schema['type'] == 'object'
        assert 'name' in json_schema['properties']
    
    def test_convert_nested_properties(self):
        """Test conversion handles nested object properties."""
        openapi_schema = {
            'type': 'object',
            'properties': {
                'user': {
                    'type': 'object',
                    'properties': {
                        'name': {'type': 'string'}
                    }
                }
            }
        }
        
        json_schema = convert_to_json_schema(openapi_schema)
        
        assert json_schema['properties']['user']['type'] == 'object'
        assert json_schema['properties']['user']['properties']['name']['type'] == 'string'
    
    def test_convert_invalid_ref(self):
        """Test conversion raises error for invalid $ref."""
        openapi_schema = {'$ref': '#/components/schemas/NonExistent'}
        
        with pytest.raises(OpenAPIParseError, match="Cannot resolve reference"):
            convert_to_json_schema(openapi_schema, {})
    
    def test_convert_external_ref(self):
        """Test conversion raises error for external $ref."""
        openapi_schema = {'$ref': 'http://example.com/schema.json'}
        
        with pytest.raises(OpenAPIParseError, match="External references not supported"):
            convert_to_json_schema(openapi_schema, {})


class TestEdgeCases:
    """Tests for edge cases and error handling."""
    
    def test_operation_with_no_parameters(self):
        """Test operation with no parameters."""
        operation = {
            'operationId': 'getAll',
            'summary': 'Get all items',
            'responses': {'200': {'description': 'Success'}}
        }
        
        tool = extract_operation_tool('/items', 'get', operation)
        
        assert tool.input_schema['type'] == 'object'
        assert tool.input_schema['properties'] == {}
    
    def test_operation_with_no_responses(self):
        """Test operation with no responses."""
        operation = {
            'operationId': 'deleteItem',
            'summary': 'Delete item'
        }
        
        tool = extract_operation_tool('/items/{id}', 'delete', operation)
        
        assert tool.output_schema == {'type': 'object'}
    
    def test_root_path_operation(self):
        """Test operation on root path."""
        operation = {
            'summary': 'Get root',
            'responses': {'200': {'description': 'Success'}}
        }
        
        tool = extract_operation_tool('/', 'get', operation)
        
        assert tool.name == 'get'
    
    def test_parameter_without_name(self):
        """Test parameter without name is skipped."""
        operation = {
            'operationId': 'test',
            'summary': 'Test',
            'parameters': [
                {'in': 'query', 'schema': {'type': 'string'}}
            ],
            'responses': {'200': {'description': 'Success'}}
        }
        
        tool = extract_operation_tool('/test', 'get', operation)
        
        assert tool.input_schema['properties'] == {}
