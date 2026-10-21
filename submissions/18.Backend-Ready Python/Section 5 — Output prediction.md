## Section 5 — Output prediction

## Predict before running

10 marks

Each question is worth 2 marks. Write the exact output or describe the exception and explain your reasoning. Do not execute the snippets before attempting them.

### 5.1 — `collections.Counter`

```python
from collections import Counter
counts = Counter(["a", "b", "a", "c", "b", "a"])
print(counts["a"])
print(counts["z"])
print(counts.most_common(2))
```

# Ans: O/P

3
0
[('a', 3), ('b', 2)]


### 5.2 — `defaultdict`

```python
from collections import defaultdict
groups = defaultdict(list)
groups["A"].append(10)
groups["A"].append(20)
print(groups["A"])
print(groups["B"])
print(dict(groups))
```

# Ans:

{'A': [10,20]}
[]
{'A': [10,20],'B':[]}

### 5.3 — `deque`

```PYTHON
from collections import deque
history = deque(maxlen=3)
for value in [10, 20, 30, 40]:    
    history.append(value)

print(list(history))
```

# Ans:

[20, 30, 40]


### 5.4 — `math`

```python
import math
print(math.ceil(20 / 6))
print(math.floor(-3.2))
print(math.isfinite(float("inf")))
```

# ANs:

4
-4
False


### 5.5 — `ChainMap`

```python
from collections import ChainMap
defaults = {"timeout": 30, "debug": False}
environment = {"timeout": 15}
runtime = {"debug": True}
config = ChainMap(runtime, environment, defaults)
print(config["timeout"])
print(config["debug"])
defaults["timeout"] = 60
print(config["timeout"])
```
# Ans:

15
True
15


