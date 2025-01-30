from language_models.ollama import query_ollama
from language_models.open_ai import query_open_ai
from IPython.display import Markdown, display
from models.website import Website

# This can use eihter model, but has to be used in an IDE that displays markdown
def display_summary_markdown(url):
    display(Markdown(summarize_website_ollama(url)))

def summarize_website_ollama(url):
    website = Website(url)
    return query_ollama("llama3.2", messages_for(website))

def summarize_website_open_ai(url):
    website = Website(url)
    return query_open_ai("gpt-4o-mini", messages_for(website))

def messages_for(website):
    system_prompt = "You are an assistant that analyzes the contents of a website and provides a short summary, \
    ignoring text that might be navigation related. Respond in markdown."
    return [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt_for(website)}
    ]
    
def user_prompt_for(website):
    user_prompt = f"You are looking at a website titles {website.title}"
    user_prompt += "\nThe contents of this website is as follows; please provide a short summary of this website in markdown. \
        If it includes news or announcements, then summarize these too \n\n"
    user_prompt += website.text
    return user_prompt
	       
#print(summarize_website_open_ai("https://edwarddonner.com"))
print(summarize_website_ollama("https://edwarddonner.com"))