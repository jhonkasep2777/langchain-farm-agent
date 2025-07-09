import os
from langchain.chat_models import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()  # Load API keys from .env

llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.5)

response = llm.predict("Halo, ini bot farming LangChain sedang aktif!")

print(response)
