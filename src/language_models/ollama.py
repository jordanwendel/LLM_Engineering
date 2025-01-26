import ollama

def queryOllama(model, messages):
    response = ollama.chat(model=model, messages=messages)
    return response['message']['content']