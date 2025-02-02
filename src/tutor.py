# Project that takes a technical question and respods with an explanation
from language_models.open_ai import query_open_ai_stream

def ask_question(question):
    system_prompt = "You are a helpful tutor that explains technical concepts in a way that is easy to understand.\
    	You answer any topics that may be asked, breaking down complex topics into simpler terms and smaller concepts. \
        If you are answering in code, make sure you format it correctly and put it in a code block. \
        If you do not know the answer, say so instead of guessing. You may speculate if you are not sure, but always say so and make sure you explain your reasoning."

    stream = query_open_ai_stream(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": get_user_prompt_for_question(question)}
        ]
    )
    for chunk in stream:
        print(chunk.choices[0].delta.content or '', end='')


def get_user_prompt_for_question(question):
    user_prompt = f"Please explain this technical concept: {question}\n\n\
        Provide a clear explanation with examples that would help someone understand it completely."
    return user_prompt


question = """Please explain what this code does and why:
yield from {book.get("author") for book in books if book.get("author")}
What would happen if I removed the yield from? Explain even if I had a return statement on the non yield."""

ask_question(question)
     
