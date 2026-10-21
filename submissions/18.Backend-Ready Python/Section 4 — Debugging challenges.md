## Section 4 — Debugging challenges

## Find and fix the bugs

15 marks

Each problem is worth 3 marks. For each snippet, identify the bug, explain why it occurs, and provide a correction.

### 4.1 — JSON validation

```python
import json
payload = '{"amount": -25, "status": "completed"}'
order = json.loads(payload)
if order["amount"] < 0:    
    print("Rejected: negative amount")
accepted_orders = []
accepted_orders.append(order)
```

Explain why the invalid order still enters the accepted list.

# Ans:

In conditional block the if statement just validates the if the amount is negative then it prints but in above program the else block is not used instead the orders were appended in list without validation. we shoud append the valid orders in else block so if block will skips appending the negative amount orders in accepetd orders list.

# Corrected code:

```python
import json
payload = '{"amount": -25, "status": "completed"}'
order = json.loads(payload)

accepted_orders = []
if order["amount"] < 0:    
    print("Rejected: negative amount")
else:
    accepted_orders.append(order)
```


### 4.2 — Timezone comparison

```python
from datetime import datetime, timezone
deadline = datetime(2026, 10, 20, 12, 0)
now = datetime.now(timezone.utc)
if now < deadline:    
    print("Deadline is in the future")

```
Identify the runtime problem and correct the code.

# Ans: Here in  code the deadline is the naive datetime and the now is aware datetime during the comparison python raises typeerror bcz python forbids comparizeon b/ naive and aware datetimes.

To make this code working either we have to add timze zone to the deadline or we shour remove time zone from the now.

```python
from datetime import datetime, timezone
deadline = datetime(2026, 10, 20, 12, 0, tzinfo=timezone.utc)
now = datetime.now(timezone.utc)
if now < deadline:    
    print("Deadline is in the future")

```

### 4.3 — Regular expression validation

```python
import re
order_id = "ORD-123-invalid"
pattern = r"ORD-\d+"
if re.search(pattern, order_id):    
    print("Valid order ID")

```
Explain why the validation can accept an invalid ID and correct it.

# Ans:

# During the search first it finds the ORD- and it found in the order id and then it accepted any digits followd by ORD- due to \d+ and this ignores anything after this becouse the pattern is found in the string. 

# Corrected code:

```python
import re
order_id = "ORD-123-invalid"
pattern = r"^ORD-\d+$"
if re.search(pattern, order_id):    
    print("Valid order ID")

```

### 4.4 — CSV numeric validation

```python
import math
amount = float("nan")
if amount < 0:    
    print("Invalid amount")
else:    
    print("Accepted")
```

Explain why the output is misleading and correct the validation.

# Ans:• Here the float accepts the Nan and inf values and during the the if condition it fails and the else block executes and this is misleading beacuse the the Nan is not a number. To make this correct we shoud validate the amount with isfinite() method to know wherther its finite or not and then we can compare the amount with negtive conitions."

# Corrected fix

```python
import math
amount = float("nan")
if not math.isfinite(amount) or amount < 0:    
    print("Invalid amount")
else:    
    print("Accepted")
```


### 4.5 — Random reproducibility

```python
import random
random.Random(42)
print(random.randint(1, 100))
```

Explain why the output is not controlled by the newly created seeded generator. Correct it.

# Ans:

The output is not controlled by the seeded generator because random.Random(42) creates an entirely new, independent generator instance but does not assign it to a variable.
When you call random.randint(1, 100) on the next line, Python falls back to using the global, default system generator module, which remains unseeded by your value of 42. This causes the script to print a completely random, unpredictable number every time it runs.

To fix this, we must store the newly created instance in a variable (e.g., rng) and call the .randint() method directly from that seeded instance.

```python 

import random

# Fix: Assign the seeded instance to a variable
rng = random.Random(42)

# Call the method on your specific instance, not the global module
print(rng.randint(1, 100))  # Will always output 82

```

we can also use the global module function random.seed(42) to seed the default system generator directl


```python
import random

random.seed(42)
print(random.randint(1, 100))  # Will always output 82

```


