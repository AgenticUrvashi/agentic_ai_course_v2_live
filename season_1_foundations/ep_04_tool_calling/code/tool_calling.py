import os
from pathlib import Path
from dotenv import load_dotenv
from rich import print
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage, ToolMessage
from langchain.chat_models import init_chat_model

load_dotenv()
MODEL = os.getenv("GROQ_MODEL", "groq:qwen/qwen3.8-27b")

RESUME_DIR = ( Path(__file__).parent.parent / "resumes" )

@tool
def add(a:float,b:float) -> float:
    """Add two number together and return the addition result"""
    return a + b

@tool
def get_weather(city:str) -> str:
    """Get the current weather of given city name"""
    weather = {"mumbai":"32C , humid" , "delhi":"38C , hazy" , "bengaluru":"26C , plesanat"}
    return f"City {city} - {weather.get(city.lower(),f"No weather data for '{city}'")}" 

@tool
def lookup_user(user_id:str) -> str:
    """Look up a user's name and plan by their id(eg.'u1')."""
    users = {"u1":"Aarav (Pro plan)","u2":"Diya (Free plan)"}
    return users.get(user_id, f"No user with id '{user_id}'.")

@tool
def get_resume(name:str) -> str:
    """Read and the return stored resume for candidate name (ramesh, khushi)"""
    first_name = name.lower().strip().split()[0]
    file_path = RESUME_DIR / f"{first_name}.txt"

    if file_path.exists():
        return file_path.read_text(encoding="utf-8")
    return f"No resume found for {name}"

TOOLS = {t.name: t for t in [add, get_weather, lookup_user, get_resume]}

def run_tool_safely(name:str,args:dict)->str:
    tool_fn = TOOLS.get(name,None)

    if tool_fn is None:
        return f"Error:unknown tool {name}"

    try:
        return tool_fn.invoke(args)
    except Exception as e:
        return f"Error running {name}: {e}"

def main()->None:
    llm = init_chat_model(MODEL,temperature=0)
    llm_with_tools = llm.bind_tools(list(TOOLS.values()))

    question = "can we select ramesh for Python developer interview.just tell me yes or no?"
    messages=[HumanMessage(content=question)]
    print(f"[bold cyan] USER: [/bold cyan] {question}\n")

    ai = llm_with_tools.invoke(messages)
    messages.append(ai)
    
    if not ai.tool_calls:
        print(f"[magenta]AI:[/magenta] {ai.content}")
        return None 

    for tc in ai.tool_calls:
        print(f"[yellow]tool call:[/yellow] {tc['name']}({tc['args']})")
        result = run_tool_safely(tc["name"],tc["args"])
        print(f"[yellow]result:[/yellow] {result}")
        messages.append(ToolMessage(content=result, tool_call_id=tc["id"]))

    final = llm_with_tools.invoke(messages)
    print(f"\n[bold magenta]AI:[/bold magenta] {final.content}")

if __name__ == "__main__":
    main()
