import openai
import gradio
from config import apikey

openai.api_key = apikey

messages=[]

system_msg = input("What Type of chatbot would you like to create?\n")
messages.append({"role" : "system", "content" : system_msg})

print(f"Your {system_msg} type chatbot is ready.\n")

def chatbot(user_input):
    messages.append({"role" : "user", "content" : user_input})

    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role" : "system", "content" : ChatGPT_reply})
    return ChatGPT_reply


demo = gradio.Interface(fn=chatbot, inputs="text",outputs="text",title=system_msg.capitalize(),
                        thumbnail="All rights are reserved \n@love_your_self_first.")

demo.launch(share=True)
