import google.generativeai
from dotenv import load_dotenv
import os

load_dotenv(override=True)
api_key = os.getenv('GOOGLE_API_KEY')
google.generativeai.configure(api_key=api_key)

def query_gemini(model, messages):
    return google.generativeai.GenerativeModel(
        model_name=model,
        system_instruction=messages
    ).generate_content(messages)
