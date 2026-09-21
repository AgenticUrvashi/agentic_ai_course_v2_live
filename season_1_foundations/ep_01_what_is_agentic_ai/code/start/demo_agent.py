"""
Ep 01 DEMO — watch a real AI AGENT (not a chatbot) work.

We are NOT explaining how to build this yet (that's Ep 02-07). For now, just
RUN it and watch the loop: the agent decides on its own whether to calculate
or search, runs the tool, reads the result, and answers.

Official docs (verify before teaching — June 2026):
  - create_agent:  https://docs.langchain.com/oss/python/langchain/agents
  - tools (@tool): https://docs.langchain.com/oss/python/langchain/tools

Run:
    python demo_agent.py

Model: defaults to OpenAI. For a FREE local run, install Ollama
(`ollama pull llama3.2`) and set DEMO_MODEL=ollama:llama3.2 in your .env.

The code is split into numbered STEPS that match the README walkthrough.
"""

from __future__ import annotations

import os
from dotenv import load_dotenv
from rich import print
import time
from langchain_core.tools import tool
from langchain.agents import create_agent   # v1 API (replaces create_react_agent)

# STEP 1 — Load secrets from .env (never hardcode/log API keys).
# TODO — build this in the video (README walkthrough STEP 1)
...


# STEP 2 — Give the agent its first "hand": a calculator tool.
# The function name + docstring + type hints become the tool's description,
# which the model reads to decide WHEN to use it.
@tool
def calculator(expression: str) -> str:
    """Do basic math. Example: '23 * 19 + 7'."""
    # TODO — build this in the video (README walkthrough STEP 2)
    ...


# STEP 3 — Give it a second hand: a (mock) search tool, so the demo needs no key.
@tool
def search(query: str) -> str:
    """Look up a simple fact on the web."""
    # TODO — build this in the video (README walkthrough STEP 3)
    ...


def main() -> None:
    # STEP 4 — Create the agent: a model + its tools. That's it.
    # We tell it to ALWAYS use the tools so the loop is visible in the demo.
    # TODO — build this in the video (README walkthrough STEP 4)
    ...

    # STEP 5 — Ask one question that needs BOTH tools.
    # TODO — build this in the video (README walkthrough STEP 5)
    ...

    # STEP 6 — Stream each step so students SEE the loop (not just the final answer).
    # TODO — build this in the video (README walkthrough STEP 6)
    ...


if __name__ == "__main__":
    main()