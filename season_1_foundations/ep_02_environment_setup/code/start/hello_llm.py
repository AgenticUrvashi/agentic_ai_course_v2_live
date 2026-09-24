import os
from dotenv import load_dotenv
from rich import print
from langchain.chat_models import init_chat_model
from langchain_groq import ChatGroq

load_dotenv()

MODEL_NAME = "qwen/qwen3.8-27b" #"llama3.2"
MODEL_PROVIDER ="groq" #"ollama"
# llm = init_chat_model(model = MODEL_NAME,model_provider=MODEL_PROVIDER)
llm = ChatGroq(model=MODEL_NAME)

response = llm.invoke("Hi there, how are you?")
print(response.content)
