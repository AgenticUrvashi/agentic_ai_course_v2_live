# Ep 02 — Exercises

## A. Setup (do it)
1. Create a fresh project with the structure shown (`src/`, `.env`, `.env.example`, `.gitignore`).
2. Create a venv with `uv venv` and activate it.
3. Install deps and run `hello_llm.py` successfully.

## B. Get a key (do it)
4. Create **one** API key — either a paid OpenAI key **or** a free Gemini/Groq key (follow README §3 Step 7). Paste it into `.env` as the right variable name.
5. In one sentence, explain what an API key *is* and why it must stay secret.

## C. Git & GitHub (do it)
6. Run `git init`, then `git add .`, then `git commit -m "first commit"` inside your project.
7. Run `git status` and confirm `.env` does **not** appear (it's git-ignored). If it does, fix `.gitignore` and commit again.
8. Create an empty repo on github.com and `git push` your project to it. (This is your portfolio starting point.)

## D. Secrets safety (prove it)
9. Explain in one line why printing `os.getenv("OPENAI_API_KEY")` to logs is dangerous.

## E. Provider swapping
10. Make the same prompt work on **two** different providers (e.g. one cloud + Ollama). Note the difference in answer quality/speed.
11. Add a `MODEL` value read from `.env` so you can switch providers without editing code.

## F. Interview prep
12. Q: "How do you manage API keys in a project?" — write a 2-sentence answer.

---

## Solutions (key points)
5. An API key is a secret password that authorizes your code to use a provider's service (and bills your account); if leaked, anyone can spend your money, so it's stored in `.env` and never committed.
7. `.env` must be listed in `.gitignore`; `.env.example` (no real values) is the one you commit. `git status` should never show `.env`.
9. Logs are often stored/shared/searchable; a logged key can be stolen → bills + data breach. Never log secret values.
12. "Keys live in environment variables loaded from a `.env` file that's git-ignored; code reads them via `os.getenv`/dotenv. Nothing secret is hardcoded or logged; in production we use a secrets manager."