# Ep 03 — LLM Structured Output with Pydantic (Student Notes)

**Level:** Beginner → applied · **Study time:** 60–75 min
**Goal:** Make an LLM return **reliable, validated data** (not loose text) using Pydantic — the single most reused skill in this course.

> **Through-line (remember this):** the Pydantic models you learn here come back as **tool schemas (Ep 04)**, **agent state (Ep 09)**, and **guardrails (Ep 35)**. Learn it once, use it the whole course and your whole career.

---

## 1. The problem (why plain text breaks production)
Ask an LLM "extract name, email, skills from this resume" and you get *text* — sometimes JSON, sometimes a paragraph, sometimes "Sure! Here's the info:". Your code can't trust that.

> **New word — JSON:** a simple, universal text format for structured data that code can read, like `{"name": "Aarav", "skills": ["python"]}`. It's how programs pass data around. We want the LLM to return *valid JSON shaped exactly how we asked*, not free-form prose.

**Production needs structured, validated data**: guaranteed fields, correct types, no surprises. That's what **Pydantic** + structured output gives you.

---

## 2. Core concepts

### 2.1 Messages: system vs user
- **System message** = the agent's role/rules ("You are a precise data extractor.").
- **User message** = the actual request/content.
Good system prompts = more reliable output. (We'll harden these as guardrails in Ep 35.)

### 2.2 Temperature / sampling
> **New word — deterministic:** "same input → same output, every time." The opposite is *random/varied*. For data extraction you want deterministic results so the answer doesn't change run to run.

- `temperature=0` → deterministic, focused (use for extraction, tools, code).
- higher (0.7–1) → creative, varied (use for brainstorming, writing).
**Rule:** for structured/data tasks, keep temperature low.

### 2.3 Streaming (preview only — not used in this episode's build)
**Streaming** means the model sends its reply token-by-token as it's generated (the ChatGPT "typing" effect) instead of making you wait for the whole answer — better UX. We *don't* stream in this episode because structured extraction returns one validated object at the end, not a flowing paragraph. Just know the word; we build a real streaming agent UX in Ep 17.

### 2.4 Structured output with Pydantic
> **Two new words:**
> - **Schema:** the "spec sheet" describing your data — which fields exist, their names, and their types (e.g. `name` is text, `years_experience` is a number). A Pydantic model *is* a schema.
> - **Validate / validation:** automatically checking that the data actually matches the schema (right fields, right types) before your code trusts it. If it doesn't match, you get an error instead of bad data sneaking through.

Define the exact shape you want as a Pydantic model; the LLM is forced to fill it:
```python
from pydantic import BaseModel, Field

class Resume(BaseModel):
    name: str = Field(description="Full name of the candidate")
    email: str | None = Field(default=None, description="Email if present")
    years_experience: float = Field(description="Total years of experience")
    skills: list[str] = Field(description="Technical skills")

structured_llm = llm.with_structured_output(Resume)
result = structured_llm.invoke(messy_resume_text)   # -> a validated Resume object
```
If the model returns a bad type, Pydantic raises — you catch it instead of shipping garbage.

### 2.5 Token & cost tracking (₹ awareness)
> **New word — token:** a token is a small chunk of text (roughly ¾ of a word). Models read your prompt and write their reply in tokens, and providers **charge per token**. So "tokens = money."

Every call costs tokens = money. Always be able to answer "what did this cost?" — a real job concern (full optimization in Ep 37). We log token counts (never secrets) per call.

---

## 3. Build: a structured extractor (messy resume → validated JSON)
Open `code/final/structured_extractor.py`:
- Defines a `Resume` Pydantic model (the exact shape we want back).
- Uses `with_structured_output` to force valid data.
- Validates types, handles missing fields.
- Prints token usage so you see the cost.

Run:
```bash
cd code/final
python structured_extractor.py
```

**Expected output** (verified 30 Aug 2026 · `gpt-5.6-luna` — token counts vary run to run):
```text
Extracting structured data from a messy resume...

tokens — in: 246 out: 2363 total: 2609
{
  "name": "Aarav Sharma",
  "email": "aarav.sharma@example.com",
  "years_experience": 4.5,
  "skills": [
    "python",
    "fastapi",
    "postgres",
    "docker",
    "aws",
    "langgraph",
    "ai agents",
    "react"
  ]
}

Validated! 8 skills, 4.5 yrs experience.
```

### Code walkthrough (step by step)
| Step | What it does | Why it matters |
|---|---|---|
| **STEP 1** | Define the `Resume` Pydantic model | The exact shape the LLM must return |
| **STEP 2** | `init_chat_model(..., temperature=0)` | Deterministic output for data tasks |
| **STEP 3** | `with_structured_output(Resume, include_raw=True)` | Forces valid shape + exposes usage/errors |
| **STEP 4** | system + user messages | Role/rules vs the actual content |
| **STEP 5** | log token counts | Cost awareness (never log PII/secrets) |
| **STEP 6** | check `parsing_error` | Never trust unvalidated output |

Sample files live in `code/final/samples/`. **Note (security):** we read only fixed sample files we ship — we never build file paths from untrusted user input (that prevents path-traversal attacks; covered properly when we serve this in Ep 40).

---

## 4. What you learned
- System vs user messages, temperature, streaming.
- **Pydantic structured output** = reliable, validated data from an LLM.
- Token/cost tracking basics.
- The through-line: this model pattern powers tools, state, and guardrails later.

## 5. Self-check
1. Why is `with_structured_output` better than parsing text yourself?
2. What temperature for an extraction task, and why?
3. Where else in the course will these Pydantic models reappear?

## 6. Homework
`exercises.md` — add a new field with validation, make extraction fail on purpose and handle it, and print cost.

---

**Next (Ep 04):** An LLM that only talks is useless. We give it **hands** — tool/function calling — so it can actually *do* things. *"Watch the AI call my Python function and do real work."*

---

## References & Verify (official docs · verified June 2026)
Master list: [`../../REFERENCES.md`](../../REFERENCES.md). Open them and verify it yourself.
- **Structured output / `with_structured_output`:** https://docs.langchain.com/oss/python/langchain/structured-output
- **Models:** https://docs.langchain.com/oss/python/langchain/models
- **Pydantic v2:** https://docs.pydantic.dev/latest/

> Tested with: Python 3.13, `langchain` 1.3.18, Pydantic 2.13.x (run end-to-end 30 Aug 2026 on `gpt-5.6-luna`).