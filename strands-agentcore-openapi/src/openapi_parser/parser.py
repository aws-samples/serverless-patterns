"""OpenAPI 3.x specification parser for tool definition generation."""

from typing import List, Dict, Any, Optional
from src.shared.models import ToolDefinition


class OpenAPIParseError(Exception):
    """Exception raised when OpenAPI specification parsing fails."""
    pass


def parse_openapi_spec(spec_dict: dict) -> List[ToolDefinition]:
    """Parse OpenAPI 3.x specification and extract tool definitions.
    
    Args:
        spec_dict: OpenAPI specification as dictionary
        
    Returns:
        List of ToolDefinition objects, one per operation
        
    Raises:
        OpenAPIParseError: If specification is invalid or unsupported
    """
    # Validate OpenAPI version
    openapi_version = spec_dict.get('openapi', '')
    if not openapi_version:
        raise OpenAPIParseError("Missing 'openapi' field in specification")
    
    # Check version is 3.0.x or 3.1.x
    if not (openapi_version.startswith('3.0.') or openapi_version.startswith('3.1.')):
        raise OpenAPIParseError(
            f"Unsupported OpenAPI version: {openapi_version}. "
            "Only OpenAPI 3.0.x and 3.1.x are supported."
        )
    
    # Extract paths
    paths = spec_dict.get('paths', {})
    if not isinstance(paths, dict):
        raise OpenAPIParseError("Missing or empty 'paths' field in specification")
    
    # Extract components for schema references
    components = spec_dict.get('components', {})
    
    # Extract global security requirements
    global_security = spec_dict.get('security', [])
    
    # Parse all operations
    tools = []
    for path, path_item in paths.items():
        if not isinstance(path_item, dict):
            continue
            
        # Iterate through HTTP methods
        for method in ['get', 'post', 'put', 'patch', 'delete', 'head', 'options']:
            operation = path_item.get(method)
            if operation and isinstance(operation, dict):
                try:
                    tool = extract_operation_tool(
                        path=path,
                        method=method,
                        operation=operation,
                        components=components,
                        global_security=global_security
                    )
                    tools.append(tool)
                except Exception as e:
                    raise OpenAPIParseError(
                        f"Error parsing operation {method.upper()} {path}: {str(e)}"
                    )
    
    if not tools:
        raise OpenAPIParseError("No valid operations found in specification")
    
    return tools


def extract_operation_tool(
    path: str,
    method: str,
    operation: dict,
    components: dict = None,
    global_security: List[dict] = None
) -> ToolDefinition:
    """Convert OpenAPI operation to ToolDefinition.
    
    Args:
        path: API path (e.g., "/weather")
        method: HTTP method (e.g., "get")
        operation: OpenAPI operation object
        components: OpenAPI components for schema references
        global_security: Global security requirements
        
    Returns:
        ToolDefinition for the operation
    """
    components = components or {}
    global_security = global_security or []
    
    # Extract or generate tool name
    operation_id = operation.get('operationId')
    if operation_id:
        tool_name = operation_id
    else:
        # Generate from method + path
        # Convert /weather/{location} to get_weather_location
        path_parts = path.strip('/').replace('{', '').replace('}', '').replace('/', '_')
        tool_name = f"{method}_{path_parts}" if path_parts else method
    
    # Extract description from summary or description
    description = operation.get('summary', operation.get('description', f'{method.upper()} {path}'))
    
    # Convert parameters to input schema
    parameters = operation.get('parameters', [])
    request_body = operation.get('requestBody')
    input_schema = _build_input_schema(parameters, request_body, components)
    
    # Convert responses to output schema
    responses = operation.get('responses', {})
    output_schema = _build_output_schema(responses, components)
    
    # Extract security requirements (operation-level overrides global)
    security = operation.get('security', global_security)
    
    return ToolDefinition(
        name=tool_name,
        description=description,
        input_schema=input_schema,
        output_schema=output_schema,
        security=security
    )


def _build_input_schema(
    parameters: List[dict],
    request_body: Optional[dict],
    components: dict
) -> dict:
    """Build JSON Schema for tool input from parameters and requestBody.
    
    Args:
        parameters: List of OpenAPI parameter objects
        request_body: OpenAPI requestBody object
        components: OpenAPI components for schema references
        
    Returns:
        JSON Schema for input
    """
    properties = {}
    required = []
    
    # Process parameters
    for param in parameters:
        param_name = param.get('name')
        if not param_name:
            continue
            
        param_schema = param.get('schema', {})
        param_description = param.get('description', '')
        
        # Convert OpenAPI schema to JSON Schema
        properties[param_name] = convert_to_json_schema(param_schema, components)
        if param_description:
            properties[param_name]['description'] = param_description
        
        # Track required parameters
        if param.get('required', False):
            required.append(param_name)
    
    # Process requestBody
    if request_body:
        content = request_body.get('content', {})
        # Try to get JSON content type
        for content_type in ['application/json', '*/*']:
            if content_type in content:
                media_type = content[content_type]
                body_schema = media_type.get('schema', {})
                
                # Convert schema
                converted_schema = convert_to_json_schema(body_schema, components)
                
                # If schema has properties, merge them
                if 'properties' in converted_schema:
                    properties.update(converted_schema['properties'])
                    if 'required' in converted_schema:
                        required.extend(converted_schema['required'])
                else:
                    # Otherwise, add as 'body' property
                    properties['body'] = converted_schema
                    if request_body.get('required', False):
                        required.append('body')
                break
    
    # Build final schema
    input_schema = {
        'type': 'object',
        'properties': properties
    }
    
    if required:
        input_schema['required'] = required
    
    return input_schema


def _build_output_schema(responses: dict, components: dict) -> dict:
    """Build JSON Schema for tool output from responses.
    
    Args:
        responses: OpenAPI responses object
        components: OpenAPI components for schema references
        
    Returns:
        JSON Schema for output
    """
    # Try to get successful response (200, 201, or default)
    for status_code in ['200', '201', 'default']:
        if status_code in responses:
            response = responses[status_code]
            content = response.get('content', {})
            
            # Try to get JSON content type
            for content_type in ['application/json', '*/*']:
                if content_type in content:
                    media_type = content[content_type]
                    schema = media_type.get('schema', {})
                    return convert_to_json_schema(schema, components)
    
    # No schema found, return generic object
    return {'type': 'object'}


def convert_to_json_schema(openapi_schema: dict, components: dict = None) -> dict:
    """Convert OpenAPI schema to JSON Schema format.
    
    Handles OpenAPI-specific keywords like nullable, discriminator, and $ref.
    
    Args:
        openapi_schema: OpenAPI schema object
        components: OpenAPI components for resolving $ref
        
    Returns:
        JSON Schema compatible with Claude
    """
    components = components or {}
    
    # Handle $ref
    if '$ref' in openapi_schema:
        ref_path = openapi_schema['$ref']
        resolved_schema = _resolve_ref(ref_path, components)
        return convert_to_json_schema(resolved_schema, components)
    
    # Start with a copy of the schema
    json_schema = {}
    
    # Copy basic fields
    for field in ['type', 'format', 'description', 'default', 'example', 
                  'minimum', 'maximum', 'minLength', 'maxLength', 
                  'pattern', 'enum', 'items', 'additionalProperties']:
        if field in openapi_schema:
            json_schema[field] = openapi_schema[field]
    
    # Handle properties (for object types)
    if 'properties' in openapi_schema:
        json_schema['properties'] = {}
        for prop_name, prop_schema in openapi_schema['properties'].items():
            json_schema['properties'][prop_name] = convert_to_json_schema(prop_schema, components)
    
    # Handle required
    if 'required' in openapi_schema:
        json_schema['required'] = openapi_schema['required']
    
    # Handle allOf, oneOf, anyOf
    for keyword in ['allOf', 'oneOf', 'anyOf']:
        if keyword in openapi_schema:
            json_schema[keyword] = [
                convert_to_json_schema(schema, components)
                for schema in openapi_schema[keyword]
            ]
    
    # Handle nullable (OpenAPI 3.0.x specific)
    if openapi_schema.get('nullable', False):
        # Convert to oneOf with null type
        if 'type' in json_schema:
            original_type = json_schema.pop('type')
            json_schema['oneOf'] = [
                {'type': original_type},
                {'type': 'null'}
            ]
    
    # Handle items for arrays
    if 'items' in json_schema and isinstance(json_schema['items'], dict):
        json_schema['items'] = convert_to_json_schema(json_schema['items'], components)
    
    return json_schema


def _resolve_ref(ref_path: str, components: dict) -> dict:
    """Resolve $ref to actual schema from components.
    
    Args:
        ref_path: Reference path (e.g., "#/components/schemas/Weather")
        components: OpenAPI components object
        
    Returns:
        Resolved schema
        
    Raises:
        OpenAPIParseError: If reference cannot be resolved
    """
    if not ref_path.startswith('#/'):
        raise OpenAPIParseError(f"External references not supported: {ref_path}")
    
    # Parse path like "#/components/schemas/Weather"
    parts = ref_path[2:].split('/')  # Remove "#/" and split
    
    # Start from the root spec, not just components
    # The components dict passed in is actually the full components section
    current = {'components': components} if components else {}
    
    for part in parts:
        if not isinstance(current, dict) or part not in current:
            raise OpenAPIParseError(f"Cannot resolve reference: {ref_path}")
        current = current[part]
    
    return current
