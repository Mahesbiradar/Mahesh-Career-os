# Section 4 — Backend Engineering Scenarios (10 marks)

Q14. (3 marks) — Choosing a collection

An API receives 50,000 event records. You need to count event types and retrieve the five most frequent types.

Which `collections` tool would you use? Write the key line of code to obtain the top five.

# Ans: First will use a counter to count freq of all the event recorts by types and then i will use the most_common() method.


```python 

from collections import Counter

List_of_events = []

counter = Counter(List_of_events)

print(counter.most_common())

```



Q15. (3 marks) — Choosing an iterator

A service processes three large data sources sequentially. You don't want to create another list containing every record before processing.

Would you choose `chain()` or `product()`? Explain why, and write a short code example.

# Ans:

# chain() is specifically designed to combine multiple iterables into a single stream and process them sequentially (one after the other). It evaluates elements lazily on the fly, meaning it creates an iterator rather than allocating memory for a brand-new combined list.In contrast, product() computes the Cartesian product (all possible pair combinations between the data sources), which changes the data structure entirely and is highly inefficient for sequential processing


``` python
from itertools import chain

list1 = []

list2 = []

list3 = []

combined_data = chain(list1,list2,list3)


for data in combined_data:

    print(data)

```

Q16. (4 marks) — Grouping correctly

A database returns these records:

```
records = [    ("admin", "Mahesh"),    ("user", "Rahul"),    ("admin", "Amit"),    ("user", "Sneha")]
```

You need one complete group for each role.

1. Why might `groupby()` alone give the wrong result?
2. What must you do before grouping with `groupby()`?
3. When might `defaultdict(list)` be a simpler alternative?


# Ans:

# 1 : groupby() only groups consecutive/adjacent matching keys. Because it processes records sequentially in a single pass, an unsorted list will cause it to generate multiple separate, broken up groups for the same key. For the given records, it will mistakenly create two distinct groups for "admin" and two distinct groups for "user".

# 2. You must sort the data by the grouping key first. This guarantees that all matching keys are physically adjacent to one another

# 3. defaultdict(list) is simpler when your data is unsorted and you want to group everything in a single pass without the overhead of sorting (O(N) time complexity instead of \(O(N \log N)\)). It automatically initializes an empty list for any new key it encounters, allowing you to append items directly.

