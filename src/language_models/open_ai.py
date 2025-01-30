from dotenv import load_dotenv
from openai import OpenAI
import os

load_dotenv(override=True)
api_key = os.getenv('OPENAI_API_KEY')
openai = OpenAI()

def query_open_ai(model, messages, response_format=None, stream=False):
    params = {
        "model": model,
        "messages": messages,
    }
    
    if response_format is not None:
        params["response_format"] = response_format
        
    if stream:
        params["stream"] = stream
        
    response = openai.chat.completions.create(**params)
    return response.choices[0].message.content