import openai
from config import GPT_KEY

openai.api_key = GPT_KEY


def execute_promt(promt):
    response = openai.ChatCompletion.create(
        model="gpt-4-0613",
        messages=[{"role": "system",
                   "content": 'You are helpful chatbot'},
                  {"role": "user", "content": promt}
                  ])
    return response.choices[0].message['content']
