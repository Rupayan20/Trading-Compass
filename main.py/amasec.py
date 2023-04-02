import openai
from apikey import APIKEY
openai.api_key = "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"

def generate_response(prompt):
    model_engine = "davinci"
    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    return response.choices[0].text.strip()

user_query = input("Ask me anything about the stock market: ")
response = generate_response(user_query)
print(response)
