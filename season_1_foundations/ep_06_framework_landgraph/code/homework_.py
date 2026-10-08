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
    summary: str
    style: str

llm = init_chat_model(MODEL)

def answer_node(state:State)-> dict:
    response = llm.invoke(
        f"{state['style']}\n\nQuestion: {state['question']}"
        )
    return {"answer": response.content}

def summarize(state:State)->dict:
    answer = state["answer"]

    summary = llm.invoke(
        f"Summarize this answer briefly:\n {answer}"
    )

    return {"summary": summary.content}

def build_graph():
    graph = StateGraph(State)

    graph.add_node("answer", answer_node)
    graph.add_node("summary", summarize)

    graph.add_edge(START, "answer")
    graph.add_edge("answer", "summary")
    graph.add_edge("summary", END)

    return graph.compile()

def main():
    agent_app = build_graph()
    agent_result = agent_app.invoke({
        "question": "what is python, explain in single sentence?",
        "style": "Explain like I'm 10 years old."
        })

    print(f"[bold cyan]Que:[/bold cyan] {agent_result['question']}")
    print(f"[bold magenta]Ans:[/bold magenta] {agent_result['answer']}")
    print(f"[bold yellow]Summary:[/bold yellow] {agent_result['summary']}")

if __name__ == "__main__":
    main()

"que no. 4: "
# I used langchain for quick prototype because it is useful for llm applications.
# I used langgraph for production support agents.
# I used deepagent for multi-hour autonomous research task.
