def messages_for(website):
    system_prompt = "You are an assistant that analyzes the contents of a website and provides a short summary, \
    ignoring text that might be navigation related. Respond in markdown."
    return [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": __user_prompt_for(website)}
    ]
    
def __user_prompt_for(website):
    user_prompt = f"You are looking at a website titles {website.title}"
    user_prompt += "\nThe contents of this website is as follows; please provide a short summary of this website in markdown. \
        If it includes news or announcements, then summarize these too \n\n"
    user_prompt += website.text
    return user_prompt