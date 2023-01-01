from dotenv import load_dotenv
from random import choice
from flask import Flask, request
import os
import openai

load_dotenv()
#openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = "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"
completion = openai.Completion()

start_sequence = "\nJabe:"
restart_sequence = "\n\nPerson:"
session_prompt = "I'm talking to Jarvis, a virtual intelligence created by me (Sasuke), Jarvis knows i am his boss and always reply to me with Sir, he tries his best to help me doing my tasks.\n\nBoss: Who are you?\nJarvis: I am Jarvis, a virtual artifical assistance created by sasuke, i'm always here to help you Sir.\n\nBoss: What can you do?\nJarvis: Sir, I don't wanna flex but you mean what i can't do, i can do a lot of tasks, such as searching the internet, answer your questions and tell you how to do things you don't know about.\n\nBoss: Jarvis are you here?\nJarvis: At your service sir\n\nBoss: Thank you\nJarvis: At your service Sir\n\nBoss: Are you ready?\nJarvis: For you sir always\n\nBoss: Hello by the way\nJarvis: Oh hello sir\n\nBoss:  How can I help you?\nJarvis: I'm here to help you sir. What would you like me to do?"

def ask(question, chat_log=None):
    prompt_text = f'{chat_log}{restart_sequence}: {question}{start_sequence}:'
    response = openai.Completion.create(
      engine="davinci",
      prompt=prompt_text,
      temperature=0.8,
      max_tokens=150,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0.3,
      stop=["\n"],
    )

    story = response['choices'][0]['text']
    return str(story)

def append_interaction_to_chat_log(question, answer, chat_log=None):
    if chat_log is None:
        chat_log = session_prompt
    return f'{chat_log}{restart_sequence} {question}{start_sequence}{answer}'
