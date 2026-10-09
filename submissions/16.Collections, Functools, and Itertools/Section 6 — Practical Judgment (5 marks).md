
## Section 6 — Practical Judgment (5 marks)

Q19. (2 marks) You need to group unsorted records by role and accumulate usernames. Would you normally choose `defaultdict(list)` or sort the data and use `groupby()`? Explain your choice.

# Ans: I would choose defaultdict(list). defaultdict(list) handles the grouping in a single pass with O(N) time complexity, because it reads each record once and appends it to a hash map.Sorting the data first to use groupby() requires \(O(N \log N)\) time complexity, which is significantly slower for large datasets.defaultdict(list) completely bypasses the requirement to sort the data beforehand. It automatically initializes an empty list for any new key encountered, making the logic much cleaner and less error-prone.


Q20. (3 marks) A backend function performs an expensive calculation repeatedly for the same integer inputs. Explain how `lru_cache` helps, name one limitation, and recommend whether to use a bounded or unbounded cache in a long-running service.

# Ans: lru_cache saves execution time by storing the results of expensive calculations. If the function is called again with the same integer inputs, it returns the cached result instantly instead of recalculating it.All function arguments must be hashable (immutable). It will crash with a TypeError if we pass mutable types like lists or dictionaries.




