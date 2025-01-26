from dotenv import load_dotenv
from openai import OpenAI
import os

load_dotenv(override=True)
api_key = os.getenv('OPENAI_API_KEY')
openai = OpenAI()

def queryOpenAI(model, messages):
    response = openai.chat.completions.create(model=model, messages=messages)
    return response.choices[0].message.content