import openai
import gradio
from config import apikey

openai.api_key = apikey


messages =[]

system_msg = input("What type of chatbot would you like to create?\n")
messages.append({"role" : "system", "content" : system_msg})

print(f"Your {system_msg} type bot is ready.\n")

while input != "quit":
    message = input("Enter your query: \n")
    messages.append({"role" : "user", "content" : message})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",messages = messages)
    reply = response["choices"][0]["message"]["content"]
    messages.append({"role" : "assistant", "content" : reply})
    print("\n" + reply + "\n")

    

