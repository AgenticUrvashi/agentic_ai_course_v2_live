# Ep 03 — Exercises

1. Add a `current_role: str | None` field to `Resume` and re-run. Did it extract correctly?
2. Add a validator: `years_experience` must be `>= 0`. Feed text implying negative/garbage and watch validation catch it.
3. Create an `Invoice` model (`invoice_number`, `total_amount: float`, `due_date`, `line_items: list[str]`) and extract from a sample invoice you write.
4. Set `temperature=1.0` and run extraction 3 times. Note inconsistency — explain why low temperature is correct here.
5. Print the cost in ₹: multiply tokens by a rough per-token price and show it.
6. **Interview:** "How do you make an LLM return reliable structured data?" — write a 3-sentence answer mentioning Pydantic, `with_structured_output`, validation, and handling failures.

## Solution hints
- Use `from pydantic import field_validator`.
- Reliability answer: define schema with Pydantic → `with_structured_output` forces the shape → validate types → on `parsing_error`, retry or fail safely (never trust raw text).