# from .app import chat_messages
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.environ.get('DEEPSEEK_API_KEY'),
    base_url="https://api.deepseek.com",
)

def stream_output(messages): 
    return client.chat.completions.create(  
        model="deepseek-flash",
        messages=messages, 
        stream=True,
        reasoning_effort="low",
        extra_body={"thinking": {"type": "disabled"}},
    )