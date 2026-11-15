import json
import argparse
from websocket import create_connection


# parse arguments
parser = argparse.ArgumentParser()
parser.add_argument('-w', '--websockets-url', help='WebSockets URL to connect', required=True)
parser.add_argument('-p', '--prompt', help='User prompt to LLM', required=True)
parser.add_argument('-m', '--model-id', default='anthropic.claude-v2:1', help='Amazon Bedrock Model ID')
parser.add_argument('-t', '--temperature', default='0', help='LLM temperature parameter')
args = parser.parse_args()

# constants
websockets_url = args.websockets_url
prompt = args.prompt.replace('\\n', '\n') # to adhere to Anthropic prompt format
model_id = args.model_id
temperature = 0

# websockets_url = "wss://u6731a4wn6.execute-api.us-east-1.amazonaws.com/prod"
# prompt = "Under 100 words, explain why the sky is blue."
# model_id = "meta.llama2-70b-chat-v1"
# temperature = 0

payload = {
    "action":"invokeModel",
    "parameters":{
        "modelId": model_id,
        "temperature": temperature
    },
    "prompt": prompt
}

ws = create_connection(websockets_url)
ws.send(json.dumps(payload))

print("--Start of LLM response--\n")
while True:
    result =  ws.recv()
    if result == "<End of LLM response>":
        break
    print(result, end="") # print on the same line
print("\n\n--End of LLM response--")

ws.close()
