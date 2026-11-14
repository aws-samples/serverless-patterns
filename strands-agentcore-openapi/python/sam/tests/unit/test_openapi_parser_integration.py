"""Integration tests for OpenAPI parser with realistic specifications."""

import pytest
from src.openapi_parser import parse_openapi_spec, OpenAPIParseError


class TestWeatherAPISpec:
    """Test parsing a realistic Weather API OpenAPI specification."""
    
    def test_parse_weather_api_spec(self):
        """Test parsing a complete Weather API specification."""
        spec = {
            'openapi': '3.0.3',
            'info': {
                'title': 'Weather API',
                'version': '1.0.0',
                'description': 'API for retrieving weather information'
            },
            'servers': [
                {'url': 'https://api.weather.example.com/v1'}
            ],
            'components': {
                'schemas': {
                    'WeatherData': {
                        'type': 'object',
                        'properties': {
                            'location': {'type': 'string'},
                            'temperature': {'type': 'number'},
                            'conditions': {'type': 'string'},
                            'humidity': {'type': 'integer'},
                            'wind_speed': {'type': 'number'}
                        },
                        'required': ['location', 'temperature', 'conditions']
                    },
                    'UserContext': {
                        'type': 'object',
                        'properties': {
                            'user_id': {'type': 'string'},
                            'username': {'type': 'string'},
                            'client_id': {'type': 'string'}
                        },
                        'required': ['user_id', 'username', 'client_id']
                    }
                },
                'securitySchemes': {
                    'bearerAuth': {
                        'type': 'http',
                        'scheme': 'bearer',
                        'bearerFormat': 'JWT'
                    }
                }
            },
            'security': [
                {'bearerAuth': []}
            ],
            'paths': {
                '/weather': {
                    'get': {
                        'operationId': 'getCurrentWeather',
                        'summary': 'Get current weather for a location',
                        'description': 'Returns current weather conditions including temperature, humidity, and wind speed',
                        'parameters': [
                            {
                                'name': 'location',
                                'in': 'query',
                                'required': True,
                                'description': 'Location name (e.g., "Seattle")',
                                'schema': {'type': 'string'}
                            },
                            {
                                'name': 'user_context',
                                'in': 'query',
                                'required': True,
                                'description': 'User context for audit trail',
                                'schema': {'$ref': '#/components/schemas/UserContext'}
                            }
                        ],
                        'responses': {
                            '200': {
                                'description': 'Successful response',
                                'content': {
                                    'application/json': {
                                        'schema': {'$ref': '#/components/schemas/WeatherData'}
                                    }
                                }
                            },
                            '400': {
                                'description': 'Invalid request'
                            },
                            '401': {
                                'description': 'Unauthorized'
                            }
                        },
                        'security': [
                            {'bearerAuth': []}
                        ]
                    }
                },
                '/forecast': {
                    'get': {
                        'operationId': 'getForecast',
                        'summary': 'Get weather forecast for a location',
                        'description': 'Returns multi-day weather forecast',
                        'parameters': [
                            {
                                'name': 'location',
                                'in': 'query',
                                'required': True,
                                'description': 'Location name',
                                'schema': {'type': 'string'}
                            },
                            {
                                'name': 'days',
                                'in': 'query',
                                'required': False,
                                'description': 'Number of days to forecast (1-7)',
                                'schema': {
                                    'type': 'integer',
                                    'minimum': 1,
                                    'maximum': 7,
                                    'default': 3
                                }
                            },
                            {
                                'name': 'user_context',
                                'in': 'query',
                                'required': True,
                                'description': 'User context for audit trail',
                                'schema': {'$ref': '#/components/schemas/UserContext'}
                            }
                        ],
                        'responses': {
                            '200': {
                                'description': 'Successful response',
                                'content': {
                                    'application/json': {
                                        'schema': {
                                            'type': 'object',
                                            'properties': {
                                                'location': {'type': 'string'},
                                                'days': {'type': 'integer'},
                                                'forecast': {
                                                    'type': 'array',
                                                    'items': {
                                                        'type': 'object',
                                                        'properties': {
                                                            'date': {'type': 'string', 'format': 'date'},
                                                            'high': {'type': 'number'},
                                                            'low': {'type': 'number'},
                                                            'conditions': {'type': 'string'}
                                                        }
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
        
        # Parse the specification
        tools = parse_openapi_spec(spec)
        
        # Verify we got both operations
        assert len(tools) == 2
        tool_names = [t.name for t in tools]
        assert 'getCurrentWeather' in tool_names
        assert 'getForecast' in tool_names
        
        # Verify getCurrentWeather tool
        current_weather = next(t for t in tools if t.name == 'getCurrentWeather')
        assert current_weather.description == 'Get current weather for a location'
        assert 'location' in current_weather.input_schema['properties']
        assert 'user_context' in current_weather.input_schema['properties']
        assert 'location' in current_weather.input_schema['required']
        assert 'user_context' in current_weather.input_schema['required']
        
        # Verify user_context was resolved from $ref
        user_context_schema = current_weather.input_schema['properties']['user_context']
        assert user_context_schema['type'] == 'object'
        assert 'user_id' in user_context_schema['properties']
        assert 'username' in user_context_schema['properties']
        assert 'client_id' in user_context_schema['properties']
        
        # Verify output schema was resolved from $ref
        assert current_weather.output_schema['type'] == 'object'
        assert 'location' in current_weather.output_schema['properties']
        assert 'temperature' in current_weather.output_schema['properties']
        assert 'conditions' in current_weather.output_schema['properties']
        
        # Verify security requirements
        assert current_weather.security == [{'bearerAuth': []}]
        
        # Verify getForecast tool
        forecast = next(t for t in tools if t.name == 'getForecast')
        assert forecast.description == 'Get weather forecast for a location'
        assert 'location' in forecast.input_schema['properties']
        assert 'days' in forecast.input_schema['properties']
        assert 'user_context' in forecast.input_schema['properties']
        
        # Verify days parameter has constraints
        days_schema = forecast.input_schema['properties']['days']
        assert days_schema['type'] == 'integer'
        assert days_schema['minimum'] == 1
        assert days_schema['maximum'] == 7
        assert days_schema['default'] == 3
        
        # Verify forecast output has array structure
        assert forecast.output_schema['type'] == 'object'
        assert 'forecast' in forecast.output_schema['properties']
        forecast_array = forecast.output_schema['properties']['forecast']
        assert forecast_array['type'] == 'array'
        assert 'items' in forecast_array
        assert forecast_array['items']['type'] == 'object'
        assert 'date' in forecast_array['items']['properties']
        assert 'high' in forecast_array['items']['properties']
        assert 'low' in forecast_array['items']['properties']
    
    def test_convert_to_claude_format(self):
        """Test converting tool definitions to Claude format."""
        spec = {
            'openapi': '3.0.0',
            'info': {'title': 'Test API', 'version': '1.0.0'},
            'paths': {
                '/test': {
                    'get': {
                        'operationId': 'testOperation',
                        'summary': 'Test operation',
                        'parameters': [
                            {
                                'name': 'param1',
                                'in': 'query',
                                'required': True,
                                'schema': {'type': 'string'}
                            }
                        ],
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
        tool = tools[0]
        
        # Convert to Claude format
        claude_tool = tool.to_claude_format()
        
        # Verify Claude format has required fields
        assert 'name' in claude_tool
        assert 'description' in claude_tool
        assert 'input_schema' in claude_tool
        
        # Verify output_schema is NOT in Claude format (Claude doesn't use it)
        assert 'output_schema' not in claude_tool
        
        # Verify values
        assert claude_tool['name'] == 'testOperation'
        assert claude_tool['description'] == 'Test operation'
        assert claude_tool['input_schema']['type'] == 'object'
        assert 'param1' in claude_tool['input_schema']['properties']
