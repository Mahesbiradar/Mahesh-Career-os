Q17. (2 marks) What does namedtuple provide that an ordinary tuple doesn't? Give one reason you might choose a dataclass instead.

# Ans: Named tuple allows us to access the elements using named attributes instead of just numerical indices. this makes code more readable and,maintainable.

# I would choose dataclass if i need mutability Tuples are immutable once created.whereas dataclass fields can be easily modified.
Q18. (3 marks) Consider:
```python
from itertools import chain
result = chain([1, 2], [3, 4])
```
Is result a list or an iterator? What happens if you iterate over it twice? Explain briefly.

# Ans:

The result is an iterator.

First iteration: It successfully yields all elements (1, 2, 3, 4)

1. Second iteration: It will be completely empty and yield nothing. This is because iterators are lazy evaluation streams that get entirely consumed upon the first pass.
