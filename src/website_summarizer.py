from language_models.ollama import *
from language_models.open_ai import *
from IPython.display import Markdown, display
from models.website import Website
from utils.prompt_utils import messages_for

# This can use eihter model, but has to be used in an IDE that displays markdown
def display_summary_markdown(url):
    display(Markdown(summarize_website_ollama(url)))

def summarize_website_ollama(url):
    website = Website(url)
    return queryOllama("llama3.2", messages_for(website))

def summarize_website_open_ai(url):
    website = Website(url)
    return queryOpenAI("gpt-4o-mini", messages_for(website))
	       
#print(summarize_website_open_ai("https://edwarddonner.com"))
print(summarize_website_ollama("https://edwarddonner.com"))