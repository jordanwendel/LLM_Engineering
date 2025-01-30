import ollama

def query_ollama(model, messages, response_format=None, stream=False):
    params = {
        "model": model,
        "messages": messages,
    }
    
    if response_format is not None:
        params["format"] = response_format
    
    if stream:
        params["stream"] = stream
        
    response = ollama.chat(**params)
    return response['message']['content']