import os
from dotenv import load_dotenv
from typing import TypedDict
from rich import print
from langchain.chat_models import init_chat_model
from langgraph.graph import StateGraph, START, END

load_dotenv()
MODEL = os.getenv("GROQ_MODEL", "groq:qwen/qwen3.8-27b")

class State(TypedDict):
    question: str
    answer: str

llm = init_chat_model(MODEL)

def answer_node(state:State)-> dict:
    response = llm.invoke(state["question"])
    return {"answer": response.content}

def build_graph():
    graph = StateGraph(State)

    graph.add_node("answer", answer_node)
    graph.add_edge(START, "answer")
    graph.add_edge("answer", END)

    return graph.compile()

def main():
    agent_app = build_graph()
    agent_result = agent_app.invoke({"question": "what is python, expain in single sentence?"})

    print(f"[bold cyan]Que:[/bold cyan] {agent_result['question']}")
    print(f"[bold magenta]Ans:[/bold magenta] {agent_result['answer']}")

if __name__ == "__main__":
    main()
