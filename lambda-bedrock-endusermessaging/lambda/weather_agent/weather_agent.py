import json
import requests
import os
import boto3
from datetime import datetime
from typing import Dict, Any, Optional


class WeatherDataAgent:

    def __init__(self):
        self.weather_api_key = get_secret_value(os.environ['WEATHER_API_KEY_SECRET_ARN'])
        self.bedrock_client = boto3.client('bedrock-runtime')
        self.bedrock_model_id = os.environ.get('AWS_BEDROCK_MODEL_ID', 'anthropic.claude-3-haiku-20240307-v1:0')
    
    
    def fetch_weather_data(self, location: str) -> Optional[Dict[str, Any]]:
        """Agent function: Fetch real weather data from WeatherAPI"""
        try:
            url = "https://api.weatherapi.com/v1/current.json"
            params = {
                'key': self.weather_api_key,
                'q': location,
                'aqi': 'no' 
            }
            
            response = requests.get(url, params=params, timeout=10)
            
            if response.status_code != 200:
                response.raise_for_status()
            
            weather_data = response.json()        
            return weather_data
            
        except requests.RequestException as e:
            print(f"Network error fetching weather data: {str(e)}")
            return None
        except KeyError as e:
            print(f"Unexpected weather data format: {str(e)}")
            return None
        except Exception as e:
            print(f"Unexpected error fetching weather data: {str(e)}")
            return None
    
    def create_structured_data(self, location: str) -> Dict[str, Any]:
        """Agent function: Compile weather data into structured format"""   
        weather_data = self.fetch_weather_data(location)
        
        if weather_data:
            try:
                structured_data = {
                    'location': location,
                    'weather': {
                        'temperature': round(weather_data['current']['temp_f']),
                        'feels_like': round(weather_data['current']['feelslike_f']),
                        'humidity': weather_data['current']['humidity'],
                        'description': weather_data['current']['condition']['text'],
                        'wind_speed': weather_data['current']['wind_mph'],
                        'visibility': weather_data['current']['vis_miles']
                    }
                }
            except KeyError as e:
                structured_data = {
                    'location': location,
                    'weather': None,
                    'error': f'Weather data format error: {str(e)}'
                }
        else:
            structured_data = {
                'location': location,
                'weather': None,
                'error': 'Weather data unavailable'
            }
        
        return structured_data
    
    def summarize_with_bedrock(self, structured_data: Dict[str, Any]) -> str:            
        if structured_data['weather']:
            weather = structured_data['weather']
            weather_context = f"""
Weather Data for {structured_data['location']}:
- Temperature: {weather['temperature']}°F (feels like {weather['feels_like']}°F)
- Conditions: {weather['description']}
- Humidity: {weather['humidity']}%
- Wind Speed: {weather['wind_speed']} mph
- Visibility: {weather['visibility']} miles
"""
        else:
            weather_context = f"""
Weather data is currently unavailable for {structured_data['location']}.
Error: {structured_data.get('error', 'Unknown error')}
"""
        
        prompt = f"""
Based on the following weather information, create a personalized briefing:

{weather_context}

Requirements:
1. Keep it under 160 characters for SMS
2. Start with "Hello!"
3. ALWAYS mention the temperature in Fahrenheit prominently if available
4. Make it friendly and informative
5. Include practical advice based on weather conditions
6. Do NOT mention seasons, weekends, or time of day
7. If weather data is unavailable, provide a positive message anyway
8. Use appropriate emojis sparingly (2-3 max)

Format: "Hello! It's [temperature]°F in [location]. [Weather description]. [Practical advice]"
"""
                
        try:
            response = self.bedrock_client.invoke_model(
                modelId=self.bedrock_model_id,
                body=json.dumps({
                    "anthropic_version": "bedrock-2023-05-31",
                    "max_tokens": 200,
                    "temperature": 0.4,
                    "messages": [
                        {
                            "role": "user",
                            "content": prompt
                        }
                    ]
                })
            )
            
            response_body = json.loads(response['body'].read())
            summary = response_body['content'][0]['text'].strip()
            
            # Ensure SMS length limit
            if len(summary) > 160:
                summary = summary[:157] + "..."
            
            return summary
            
        except Exception as e:
            # Fallback scenario
            if structured_data['weather']:
                temp = structured_data['weather']['temperature']
                condition = structured_data['weather']['description']
                fallback = f"Hello! It's {temp}°F in {structured_data['location']} with {condition}. Have a great day!"
            else:
                fallback = f"Hello! Weather info unavailable for {structured_data['location']}, but have a wonderful day!"
            
            return fallback

def get_secret_value(secret_arn):
    client = boto3.client('secretsmanager')
    response = client.get_secret_value(SecretId=secret_arn)
    return response['SecretString']

def lambda_handler(event, context):
    """Main handler for weather agent"""
    
    agent = WeatherDataAgent()
    
    # Get location from event or environment
    location = event.get('location', os.environ.get('LOCATION', 'Seattle'))
    
    try:
        # Agent fetches and structures data
        structured_data = agent.create_structured_data(location)
        
        # Bedrock FM creates intelligent summary
        personalized_briefing = agent.summarize_with_bedrock(structured_data)
        
        result = {
            'statusCode': 200,
            'body': json.dumps({
                'briefing': personalized_briefing,
                'location': location,
                'timestamp': datetime.now().isoformat(),
                'weather_available': structured_data['weather'] is not None,
                'debug_info': {
                    'weather_data_present': structured_data['weather'] is not None,
                    'error': structured_data.get('error', None)
                }
            })
        }
        
        return result
        
    except Exception as e:
        import traceback        
        return {
            'statusCode': 500,
            'body': json.dumps({
                'error': str(e),
                'fallback_message': f"Hello! Have a great day in {location}!",
                'debug_info': {
                    'error_type': type(e).__name__,
                    'error_message': str(e)
                }
            })
        }
