# Section 4 — Backend Engineering Scenarios (10 marks)

Q14. (3 marks) — Choosing a collection

An API receives 50,000 event records. You need to count event types and retrieve the five most frequent types.

Which `collections` tool would you use? Write the key line of code to obtain the top five.

Q15. (3 marks) — Choosing an iterator

A service processes three large data sources sequentially. You don't want to create another list containing every record before processing.

Would you choose `chain()` or `product()`? Explain why, and write a short code example.

Q16. (4 marks) — Grouping correctly

A database returns these records:

```
records = [    ("admin", "Mahesh"),    ("user", "Rahul"),    ("admin", "Amit"),    ("user", "Sneha")]
```

You need one complete group for each role.

1. Why might `groupby()` alone give the wrong result?
2. What must you do before grouping with `groupby()`?
3. When might `defaultdict(list)` be a simpler alternative?

## Submission instructions

Answer Q11–Q16 in your own words and code. No hints or solutions during the assessment.

I'll grade these 20 marks, explain any mistakes, and then give you Sections 5 & 6, the final part of the assessment.