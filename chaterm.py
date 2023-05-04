import openai
from dotenv import load_dotenv
import os

load_dotenv()
openai.api_key  = os.getenv('OPENAI_API_KEY')

def get_completion_from_messages(messages, model="gpt-3.5-turbo-0301", temperature=0.8):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature, # this is the degree of randomness of the model's output
    )
#     print(str(response.choices[0].message))
    return response.choices[0].message["content"]

if __name__ == '__main__':
    print("\033[34mpls input you question(quit for exit):\033[0m")
    while True:
        question = input(">")
        if question.lower() == "quit":
            print("bye")
            break
        messages = [{"role":"system","content":"you are a helpful assistant,answer the given question"},
                    {"role": "user", "content": question}]
        print("\033[34m>AI is thinking...>")
        print(get_completion_from_messages(messages)+"\033[0m")