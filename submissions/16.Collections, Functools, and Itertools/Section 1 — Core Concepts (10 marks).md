
## Section 1 — Core Concepts (10 marks)

Q1. (2 marks) You need to count HTTP status codes from a list of thousands of log entries and find the two most frequent codes. Which `collections` tool would you use, and which method finds the top two?

# Ans : To count the HTTP STATUS Codes from the list ill use counter where it counts the frequnecy of each code and then to find the two most frequent count ill use the most_common() method from the collections module.

Q2. (2 marks) What is the key difference between `defaultdict(list)` and `itertools.groupby()` when grouping records by role?

# Ans:  The defaultdict(list) builds completly new dictionary containing all groups in memory simultaneously, while itertools.groupby() is ietartor that processes data sequentially and only groups consecutive records

Q3. (2 marks) Match each task to the most appropriate tool.

- A. Fix a function argument to create a specialized function.
- B. Preserve a decorated function's name and docstring.
- C. Combine multiple iterables for sequential processing.
- D. Cache repeated function calls.

Choose from: `partial`, `wraps`, `chain`, `lru_cache`.

# Ans:

A: partial
B: wraps
C: chain
D: lru_cache

Q4. (2 marks) What is the difference between `product()` and `permutations()`? Give one practical example of each.

# Ans: The core diff is that the product() allows items to repeat and can combine multiple diffrent lists,while permutations() rearranges unique items from a single list without repetition.

Q5. (2 marks) Why might `lru_cache(maxsize=None)` be a risky choice in a long-running backend service?

# Ans: Using lru_cache(maxsize=None) means the cache has no size limit.
In a long-running backend, this is dangerous because:

The server will remember every single request it ever receives and will never throw old data away.
Over time, the cache will eat up all the server's RAM. This causes the server to run out of memory and completely crash (OOM error).


