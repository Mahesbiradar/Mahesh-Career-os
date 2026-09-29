# Section 6 — Final Interview Round

**15 marks — 5 × 3 marks**

Answer these as if you're sitting in a Python/backend interview. Keep each answer reasonably concise but technically accurate.

### Q1 — Core Understanding

An interviewer asks:

> **"What is the difference between an iterable, an iterator, and a generator?"**

Explain it in your own words and give a simple example.

---

### Q2 — Backend Application

> **"You have to process 20 million database records. Why might you choose a generator instead of loading all records into a Python list?"**

Give a practical backend explanation.

---

### Q3 — `yield`

> **"What exactly happens when Python encounters `yield` inside a generator?"**

Explain what happens to the function's execution state and what happens when `next()` is called again.

---

### Q4 — Custom Iterator

An interviewer asks:

> **"Why would you ever create a custom iterator when Python generators are much easier to write?"**

Give at least **two situations/reasons** where a custom iterator can make sense.

---

### Q5 — Engineering Judgment

You are reviewing this code:

```python
def get_active_users(users):
    return [user for user in users if user["active"]]
```

A developer says:

> "Let's change every list comprehension into a generator because generators use less memory."

Would you agree with that approach?

Explain your answer and when you would choose a list versus a generator.

---
