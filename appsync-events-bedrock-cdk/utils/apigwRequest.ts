import https from 'https'

export interface RequestParams {
    url: string;
    method: string;
    apiKey: string;
  }
  
 export interface ApiResponse {
    statusCode: number;
    body: any;
  }
  
 export interface ChatRequest {
    prompt?: string;
    userId?: string;
  }

export const makeRequest = async (params: RequestParams, body: ChatRequest): Promise<ApiResponse> => {
    const endpoint = new URL(params.url);
    const options = {
        method: params.method,
        headers: {
            'Content-Type': 'application/json',
            'x-api-key': params.apiKey,
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'POST',
            'Access-Control-Allow-Headers': 'Content-Type, x-api-key'
        },
        body: body ? JSON.stringify(body) : undefined,
    };

    try {
        const response = await fetch(`${endpoint.toString()}/chat`, options);
        const data = await response.json();
        return {
            statusCode: response.status,
            body: data
        };
    } catch (error) {
        throw error;
    }
}
