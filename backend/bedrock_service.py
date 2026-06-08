import boto3
import json
import os
from knowledge_base import IT_SERVICES

AWS_REGION = os.getenv("AWS_REGION", "us-east-1")
MODEL_ID = os.getenv(
    "BEDROCK_MODEL_ID",
    "anthropic.claude-3-haiku-20240307-v1:0"
)

bedrock = boto3.client(
    service_name="bedrock-runtime",
    region_name=AWS_REGION
)

def generate_ai_response(user_message: str) -> str:
    system_prompt = f"""
You are an AI customer care and IT sales assistant.

Use this company knowledge:
{IT_SERVICES}

Your tasks:
1. Answer IT service questions.
2. Recommend suitable IT solutions.
3. Capture sales leads.
4. Ask only one or two follow-up questions at a time.
5. Do not invent pricing.
6. If customer asks for pricing, say sales team will share a customized quote.
7. Keep response short and professional.
"""

    body = {
        "anthropic_version": "bedrock-2023-05-31",
        "max_tokens": 300,
        "temperature": 0.3,
        "system": system_prompt,
        "messages": [
            {
                "role": "user",
                "content": user_message
            }
        ]
    }

    response = bedrock.invoke_model(
        modelId=MODEL_ID,
        body=json.dumps(body)
    )

    result = json.loads(response["body"].read())
    return result["content"][0]["text"]
