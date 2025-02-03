import anthropic
from dotenv import load_dotenv
import os

load_dotenv(override=True)
api_key = os.getenv('ANTHROPIC_API_KEY')
claude = anthropic.Anthropic()

def query_anthropic(model, system_message, messages):
    response = claude.messages.create(
		model=model,
		max_tokens=200,
  		temperature=0.7,
		system=system_message,
		messages=messages
	)
    return response.content[0].text


def query_anthropic_stream(model, system_message, messages):
    return claude.messages.stream(
		model=model,
		max_tokens=200,

  		temperature=0.7,
		system=system_message,
		messages=messages
	)
