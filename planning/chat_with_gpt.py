import requests
from openai import OpenAI

def chat_with_gpt(query):
    if isinstance(query, str):
        content = []
        messages = []        
        content.append({
            "type": "text",
            "text": query,
        })
        messages.append({'role': 'user', "content": content})
        query = messages
        
    resp = client.chat.completions.create(
        model=model,
        messages=query
    )
    resp_content = resp.choices[0].message.content
    return resp_content