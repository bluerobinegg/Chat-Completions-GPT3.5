import os 
from openai import OpenAI

# Set your API key
my_secret = os.environ['SECRET_KEY_DC2']
client = OpenAI(api_key="my_secret")

messages=[
      {"role": "system", "content": "You are a helpful Python programming tutor."},
      {"role": "user", "content": "Explain what the min() function does."}
    ]

user_qs = ["The min() function returns the smallest item from an iterable","Show the answer in bullet points and keep the example short."]

for q in user_qs:
  # print("User: ", q)
  user_dict = {"role":"user", "content": q}
  messages.append(user_dict)

  response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    # Add a user and assistant message for in-context learning
    messages=messages,
    max_tokens=100
  )

  assistant_dict = {"role":"assistant", "content": response.choices[0].message.content}
  messages.append(assistant_dict)
  
print(response.choices[0].message.content)