import ollama

def query_ollama(model, messages):
    response = ollama.chat(model=model, messages=messages)
    return response['message']['content']