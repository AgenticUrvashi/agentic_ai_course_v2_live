# Ep 01 — Exercises

## A. Concept (write your answers, then check)
1. Define an AI agent in one sentence (interview version).
2. List the 4 components of an agent and what each does.
3. Fill the table: who decides the steps in a chatbot / workflow / agent?
4. Give two real company ROI examples and the *outcome* each delivered.

## B. Observation (from the demo)
5. Run `demo_agent.py`. How many tool calls did the agent make? Which tools?
6. Change the question to something that needs **only** the calculator. Does the agent skip the search tool? Why does that show "autonomy"?
7. (Optional, free) Set `DEMO_MODEL=ollama:llama3.2` and re-run. Note any difference in how it uses tools.

## C. Career
8. Write your honest current level (beginner / know Python / working dev) and your target role + salary band from the syllabus.
9. Write the one-line agent definition on a sticky note. You'll repeat it in every interview.

---

## Solutions
1. "An LLM running in a loop, using tools and memory, to autonomously accomplish a goal."
2. Reasoning (LLM) decides next step · Tools do actions · Memory keeps context · Loop repeats until goal met.
3. Chatbot: no (just answers) · Workflow: you hardcode steps · Agent: the model decides at runtime.
4. Klarna: AI assistant handled ⅔ of chats (~700 agents' worth of work), resolution **11 min → under 2 min** (≈ –82%) — note the 2025 hybrid rebalance. C.H. Robinson: ~5,500 orders/day automated in ~90 sec each. (Sources: see README §Sources [S4][S5][S6].)
5. Two tool calls — `search` (capital) and `calculator` (23*19+7 = 444).
6. Yes — it only calls `calculator`. It chose the tool based on the task = autonomy.
7. Smaller local models may need clearer prompts or call tools less reliably — a real trade-off you'll learn to manage.