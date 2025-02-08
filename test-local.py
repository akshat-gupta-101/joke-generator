from mira_sdk import MiraClient, Flow
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("API_KEY")

client = MiraClient(config={"API_KEY": api_key})

flow = Flow(source="flow.yaml")

input_dict = {
    "topic": "Technology",
    "style": "Observational"
}

response = client.flow.test(flow, input_dict)

print(response)
