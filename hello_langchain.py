#!/usr/bin/env python
# coding: utf-8

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()  # load environmental variable "GOOGLE_API_KEY" from .env


prompt = "what is your name? And what can you do?"

llm = ChatGoogleGenerativeAI(model="gemini-pro")
result = llm.invoke(prompt)
print(result.content)
