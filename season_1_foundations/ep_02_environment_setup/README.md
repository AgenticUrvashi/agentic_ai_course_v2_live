# Ep 02 — AI Engineer Setup (Student Notes)

**Level:** Beginner · **Study time:** 60–75 min · **Code:** your first real LLM call
**Goal:** Set up the *exact* professional environment AI engineers use, understand **API keys** and **Git**, handle secrets safely, and make your first LLM call — both cloud and free local.

> **Before you start (prerequisites):** you only need **basic Python** (variables, functions, lists/dicts) and the ability to **run a `.py` file** in a terminal. No prior AI, Git, or "API" knowledge needed — every new tool and word below is explained from zero. If "terminal" itself is new: it's the black text window where you type commands (called *PowerShell* on Windows, *Terminal* on Mac/Linux; Cursor has one built in under **View → Terminal**).

---

## 1. Why this episode matters (don't skip!)
> "90% beginners yahin galti karte hain." Bad setup = hours of "it works on my machine" pain later. Do it right once, reuse all course.

A clean setup is also a **job signal**: recruiters/seniors can tell in 5 seconds whether you handle secrets and project structure like a pro.

---

## 2. The tools (and why each)
| Tool | What it is | Why we use it |
|---|---|---|
| **Python 3.13+** | The programming language | Fast, latest stable, every AI library supports it |
| **`uv`** | A package + environment manager | Modern and *very* fast (replaces pip+venv pain) |
| **virtual environment** (`venv`) | A private package box per project | Isolates each project's packages (no global mess) |
| **Git** | Version control — saves snapshots of your code | Industry standard; lets you undo, track, and share code |
| **GitHub** | A website that hosts your Git projects online | Where you show projects to recruiters (your portfolio) |
| **`.env` + python-dotenv** | A secrets file + a loader for it | Keep **secrets (API keys) out of code** |
| **API key** | A password that lets your code use an AI provider | Required to call cloud models like OpenAI/Gemini |
| **Cursor / VS Code** | The code editor (IDE) | Where you write code; Cursor adds AI superpowers |
| **Ollama** | Runs LLMs on your own computer | **Free & local** models (no API cost, full privacy) |

> Don't recognize some of these? That's fine — the next sections explain **API keys** and **Git/GitHub** in plain language before you use them.

### Pro workflow: code WITH an AI assistant
Modern AI engineers don't type every line alone — they work *with* an **AI coding assistant** (Cursor's built-in AI, or **Claude Code** in the terminal) that drafts, refactors, and explains code next to them. Job postings asking for AI-coding-tool experience grew **~340% in a year** [S1] — so build the habit from day 1. Two rules while using one:
1. **Understand every line it writes** — this course teaches you exactly that, so the assistant speeds you up instead of replacing your understanding.
2. **Never paste secrets** (your `.env` contents / API keys) into any AI chat.

---

## 3. Step-by-step setup

### Step 1 — Check Python
```bash
python --version   # need 3.13+ (3.14 is latest stable)
```
No Python 3.13+? Install from python.org.

### Step 2 — Install uv
```bash
pip install uv
```
> Recommended (standalone install, not tied to one Python/pip) — Windows PowerShell:
> ```powershell
> powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
> ```

### Step 3 — Create the project + add packages
`uv` manages the project **and** the virtual env for you. Run these 4 simple commands in order:
```bash
uv init                 # 1. create the project (pyproject.toml + .python-version)
uv sync                 # 2. create the virtual env (.venv)
# Activate the venv:
.\.venv\Scripts\activate   # Windows
source .venv/bin/activate  # Mac/Linux
uv add "langgraph~=1.2.11" "langchain~=1.3" "pydantic~=2.13" python-dotenv   # 3. add packages WITH version pins
```
**What each command does:**
| Command | What it does |
|---|---|
| `uv init` | Creates the project files (`pyproject.toml` — the modern replacement for `requirements.txt`) |
| `uv sync` | Creates the `.venv` and installs whatever is listed in the project |
| `.\.venv\Scripts\activate` | Turns the venv "on" so your terminal uses the project's Python |
| `uv add <pkgs>` | Adds packages (space-separated, **NOT** commas) and installs them |

> **Why the version pins (`~=1.2.11`)?** Professionals pin dependency versions so the project installs the *same, tested* versions everywhere (your laptop, a teammate's, the server). `langgraph~=1.2.11` means "1.2.11 or a newer 1.2.x patch" — new enough to get fixes, safe enough not to break. An empty dependency list is a beginner tell.

> **Common beginner mistakes:** `uv inti` (typo for `uv init`) and commas in `uv add langchain, langgraph` — use **spaces**: `uv add langchain langgraph`.

### Step 4 — Professional project structure
```
my-agent-lab/
├── .env              ← secrets (NEVER commit)
├── .env.example      ← template (safe to commit)
├── .gitignore        ← must include .env
├── requirements.txt
├── src/
│   └── hello_llm.py
└── README.md
```
> **Why structure matters:** every job repo looks like this. Random `.py` files in one folder screams "beginner".

### Step 5 — Git & GitHub (your project's "save" system)
You'll see `.gitignore` in the structure above — so first, **what is Git?**

- **Git** is *version control*: it takes snapshots ("commits") of your code so you can undo mistakes, see what changed, and never lose work. Think of it as **"save points" for an entire project** (like checkpoints in a game).
- **GitHub** is a *website* that stores your Git project online. It's where recruiters look — your GitHub is your **portfolio**. (Every project in this course gets pushed here.)
- **`.gitignore`** is a small text file that lists files Git should **ignore** (never save/upload) — this is how we keep `.env` (your secret keys) off GitHub.

**Install Git** from [git-scm.com/downloads](https://git-scm.com/downloads), then check it works:
```bash
git --version    # e.g. git version 2.45.0
```

**First, create the repo on the GitHub website** (do this *before* the push commands):
1. Log in to [github.com](https://github.com) → click the **+** (top-right) → **New repository**.
2. Give it a **name** (e.g. `my-agent-lab`), leave it **empty** (do **NOT** add a README/.gitignore — your local project already has them), then click **Create repository**.
3. Copy the repo URL shown on the next page (looks like `https://github.com/<you>/<repo>.git`).

**Then, the only 5 Git commands you need right now** (run inside your project folder):
```bash
git init                 # 1. start tracking this folder with Git (do this once)
git add .                # 2. stage your changes (mark them to be saved)
git commit -m "first commit"   # 3. save a snapshot with a message
git status               # 4. see what changed / what's staged (use often!)
# To put it online — paste the URL you copied from GitHub above:
git remote add origin https://github.com/<you>/<repo>.git
git push -u origin main  # 5. upload your commits to GitHub
```
> Run `git status` **before every commit** to confirm `.env` is **not** in the list (if `.gitignore` is set up right, it won't be). That one habit prevents the most common beginner security mistake.

### Step 6 — Secrets hygiene (the #1 security habit)
Now that you understand Git, here's *why* `.gitignore` matters so much. In this course we use **3 cloud providers + 1 free local model**, so your `.env` will hold all of these keys (you'll create them in Step 7):
```
OPENAI_API_KEY=sk-...
GOOGLE_API_KEY=...
GROQ_API_KEY=gsk_...
# Ollama runs locally — no key needed
```
1. Put your keys in `.env` (shown above).
2. **Add `.env` to `.gitignore`** so `git` never uploads it to GitHub.
3. Commit a `.env.example` with **empty** values so teammates know which keys are needed (this one is safe to share):
   ```
   OPENAI_API_KEY=
   GOOGLE_API_KEY=
   GROQ_API_KEY=
   ```
4. Load keys with `python-dotenv` — **never** write the key directly in your `.py` file.

> **Security rule (taught from day 1):** Hardcoding a key or printing it in logs is a real, common breach. Leaked keys = surprise bills + data theft. We always load from env and never log secret values.

### Step 7 — What is an API key, and how do I get one?
**First, what's an "API"?** An **API** (Application Programming Interface) is a way for *your program* to ask *another company's service* to do something — here, "OpenAI, please answer this prompt." Your code sends a request over the internet and gets a reply back.

**So what's an API key?** It's a **secret password** that proves *who is making the request* so the provider knows whose account to use (and bill). No key → the request is rejected. Anyone with your key can spend your money, so it's treated like a password (that's why we hid it in `.env`).

We'll set up **all four** so you can compare providers (the same code calls each one — you only change a string). The two free cloud options (Gemini + Groq) mean you can finish the whole course without paying anything.

**1. OpenAI** → `OPENAI_API_KEY` *(pay-as-you-go, cheap)*
1. Go to **platform.openai.com** → **sign up / log in**.
2. Open **Billing** → add a small amount of credit (e.g. $5). Tiny test calls cost **a few cents total**.
3. Open **API keys** → **Create new secret key** → copy it (looks like `sk-...`). **You see it only once.**
4. Paste into `.env` as `OPENAI_API_KEY=sk-...`.

**2. Google Gemini** → `GOOGLE_API_KEY` *(generous **free** tier)*
1. Go to **aistudio.google.com** → log in with your Google account.
2. Click **Get API key** → **Create API key** → copy it.
3. Paste into `.env` as `GOOGLE_API_KEY=...`.

**3. Groq** → `GROQ_API_KEY` *(**free** tier, very fast)*
1. Go to **console.groq.com** → sign up / log in.
2. Open **API Keys** → **Create API Key** → copy it (looks like `gsk_...`).
3. Paste into `.env` as `GROQ_API_KEY=gsk_...`.

**4. Ollama** → *(no key — runs locally, see Step 8)*

> **If a key ever leaks:** go to the provider's dashboard and **revoke/delete** it immediately, then create a new one. Revoked keys stop working instantly.

### Step 8 — Free local model with Ollama (zero cost)
**Ollama** runs an LLM on your own computer — no key, no internet, no cost:
```bash
# Install from ollama.com, then:
ollama pull llama3.2          # download the model once (~2 GB)
ollama run llama3.2 "hello"   # test it works
```
> The course code calls `ollama:llama3.2` — a small model that runs on most laptops. Laptop struggling? Try a tinier one (`ollama pull deepseek-r1:1.5b`, ~1.1 GB) and change the string in the code.

---

## 4. Your first LLM call (cloud + local)
Open `code/final/hello_llm.py` and run it inside your uv project:
```bash
uv run hello_llm.py
# (or, if you activated the venv manually: python hello_llm.py)
```

**Expected output** (verified 30 Aug 2026 · `gpt-5.6-luna` — only the providers whose key is in your `.env` will run; wording varies):
```text
Model: openai:gpt-5.6-luna
Reply: An AI agent is a computer program that can perceive information, make
decisions, and take actions to achieve a goal.

Model: ollama:llama3.2
Could not call ollama:llama3.2: ResponseError — check the provider key in .env (or that the model is pulled in Ollama).
```
If you also set `GOOGLE_API_KEY` / `GROQ_API_KEY`, you'll see a `google_genai:gemini-3.5-flash-lite` and a `groq:openai/gpt-oss-20b` reply too — same code. The Ollama line failing is expected if you haven't installed/started Ollama (you may see `ConnectError` or `ResponseError`) — note it fails **gracefully** (no crash, no leaked key).
It calls a **cloud** model and a **local** model with the *same* code — because LangChain gives one unified interface (`init_chat_model`). Notice you only switch a string to change providers. That portability is a real production advantage (you'll use it for cost optimization in Ep 37).

### Code walkthrough (step by step)
| Step | What it does | Why it matters |
|---|---|---|
| **STEP 1** | `load_dotenv()` reads `.env` | Keys come from env, never the code |
| **STEP 2** | `call_model()` helper | One function works for every provider |
| **STEP 2a** | `init_chat_model("provider:model")` | Universal way to load any model |
| **STEP 2b** | `llm.invoke(prompt)` | Sends the prompt, returns the reply |
| **STEP 2c** | generic `except` | Safe error — never leak keys/internals |
| **STEP 3** | call cloud models if key present | Works with whatever key you have |
| **STEP 4** | call `ollama:llama3.2` | Same code, free + local — just a different string |

---

## 5. What you learned
- Pro environment: Python 3.13+ + `uv` project (`uv init` → `uv add` with **pinned versions** → `uv run`) + clean structure.
- The pro workflow: code **with** an AI assistant (Cursor / Claude Code) — while understanding every line and keeping secrets out of the chat.
- **Git & GitHub**: what they are and the 5 commands (`init`, `add`, `commit`, `status`, `push`).
- **What an API key is** (a secret password for a provider) and **how to create one** (OpenAI + free Gemini/Groq).
- **Secrets hygiene**: `.env`, `.gitignore`, never hardcode/log keys.
- First LLM call, swappable between cloud and free local with one line.

## 6. Self-check
1. What is Git, and what does `.gitignore` do?
2. What is an API key, why does it need to stay secret, and where do you store it?
3. How do you get a **free** API key without paying anything?
4. Why use a virtual environment per project?
5. How do you switch from OpenAI to a free local model in this code?

## 7. Homework
See `exercises.md` — set up your env, create an API key, make a call with 2 different providers, put the project on GitHub, and confirm `.env` is git-ignored.

---

**Next (Ep 03):** We talk to the LLM *like an engineer* — structured output with Pydantic (messy text → perfect JSON), streaming, and cost tracking. *"An LLM that only talks is half a tool — let's make it reliable."*

---

## References & Verify (official docs · verified June 2026)
Master list: [`../../REFERENCES.md`](../../REFERENCES.md). Open them and verify it yourself.
- **Models / `init_chat_model`:** https://docs.langchain.com/oss/python/langchain/models
- **uv (project & package manager):** https://docs.astral.sh/uv/
- **Git — official book (free, beginner-friendly):** https://git-scm.com/book/en/v2/Getting-Started-About-Version-Control
- **OpenAI API keys (create/manage):** https://platform.openai.com/docs/api-reference/authentication
- **Google AI Studio (free Gemini key):** https://aistudio.google.com/
- **Groq Console (free key):** https://console.groq.com/
- **Ollama (free local models):** https://docs.ollama.com/
- **python-dotenv:** https://pypi.org/project/python-dotenv/

> Tested with: Python 3.13, `langchain` 1.3.18, `langgraph` 1.2.11 (run 30 Aug 2026 on `gpt-5.6-luna`; Ollama fallback path exercised).

## Sources
- **[S1]** JDs requiring AI-coding-tool experience grew ~340% (Jan 2025 → Jan 2026): https://www.futureproofing.dev/resources/ai-native-team/claude-code-vs-cursor-for-ai-agents-2026