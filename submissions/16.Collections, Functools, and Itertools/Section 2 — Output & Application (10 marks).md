## Section 2 — Output & Application (10 marks)

Q6. (2 marks) What does this print?

```Python
from collections import Counter

counts = Counter(["200", "404", "200", "500", "404", "200"])

print(counts["200"])
print(counts.most_common(1))
print(counts["301"])

```

Give all three outputs.

# Ans: 
3
[('200' , 3)]
0

Q7. (2 marks) What is the output?

```python
from itertools import product

result = list(product(["GET", "POST"], ["dev", "prod"]))

print(len(result))
print(result[0])
print(result[-1])

```

# Ans:

4
('GET', 'dev')
('POST', 'prod')


Q8. (2 marks) Identify the issue in this code and explain how to fix it.

```python

from itertools import groupby

records = [
    ("admin", "A"),
    ("user", "B"),
    ("admin", "C")
]

for role, group in groupby(records, key=lambda x: x[0]):
    print(role, list(group))

```
# Ans: We shoud sort the records first before using the groupby on the input data.

In the provided code, the output would incorrectly split "admin" into two separate groups because "user" sits between them. Sorting the data by the key first ensures all identical roles are adjacent and grouped together correctly.

To fix this, sort the list using the same key function before passing it into groupby().

``` python
from itertools import groupby

records = [
    ("admin", "A"),
    ("user", "B"),
    ("admin", "C")
]

# FIX: Sort the records by the role (index 0) first
records.sort(key=lambda x: x[0])

# Now groupby will work flawlessly
for role, group in groupby(records, key=lambda x: x[0]):
    print(role, list(group))

```


Q9. (2 marks) Given:

```python

from functools import reduce

numbers = [2, 3, 4]
result = reduce(lambda a, b: a * b, numbers)

```

What is `result`? Briefly explain how `reduce()` reaches it.

# Ans: 

24

the reduce applies lambda functions on items in the list from left to right, first it takes 2 and multiply with 3 and then takes 4 mutiply with prev result 6 now there are no more items left for mutiplication returns the 24.

Q10. (2 marks) A backend service receives records from a database, cache, and external API. You need to process them in sequence without building a combined list first. Write the import and the `for` loop using `chain()`.

# Ans: 

```python 

from itertools import chain


for item in chain(database,cache,external_api):

    print(item)