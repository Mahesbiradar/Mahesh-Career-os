
# 🧠 Section 3 — Type Hints + Dataclasses in Practice
### **15 marks**

### Q10. Typed Data Processing — 4 marks

Consider:

```python
from dataclasses import dataclass

@dataclass
class Product:
    id: int
    name: str
    price: float
    stock: int
```

Write a function:

```python
def get_available_products(products:):

    ...
```

Requirements:

- Accept a list of `Product` objects.
- Return only products where `stock > 0`.
- Properly annotate the parameter and return type.

For example:

```python
products = [
    Product(1, "Laptop", 50000, 5),
    Product(2, "Mouse", 800, 0),
    Product(3, "Keyboard", 1500, 10)
]
```

Expected result should contain Laptop and Keyboard.

---

# Ans: Impementstation

```python
def get_available_products(products: list[Product]) ->list[Product]:

    result = []

    for product in products:

        if product.stock > 0:

            result.append(product)
    
    return result

print(get_available_products(products))

    ...
```

### Q11. Optional Dataclass Field — 3 marks

Consider:

```python
@dataclass
class User:
    id: int
    name: str
    email: str | None = None
```

Answer:

**a)** Why is `email` annotated as `str | None`?

**b)** What does `= None` accomplish?

**c)** Is this valid?

```python
user = User(101, "Mahesh")
```

Explain.

---

# Ans: a:In above code the email is annoted as `str | None` bcz the attributes will be passed as string or Not Therdor when attribute is passed during object instantiation it will use string passed or it will use None as a defualt value.

b: if During object creation if the email argument is not passed then the class will use None as defualt value against the email intance variable.

c: Yes its valid


### Q12. Dataclass Validation — 4 marks

Create:

```python
@dataclass
class BankAccount:
    account_number: str
    holder_name: str
    balance: float
```

Add a `__post_init__()` that ensures:

- `balance` cannot be negative.
- Empty `holder_name` should raise `ValueError`.

Then explain **why `__post_init__()` is a suitable place for these checks**.

---

# Ans:


```python

from dataclasses import dataclass

@dataclass
class BankAccount:
    account_number: str
    holder_name: str
    balance: float

    def __post_init__(self):
        if self.balance < 0:
            raise ValueError("The balance cannot be negative")
        
        if not self.holder_name or not self.holder_name.strip() :
            raise ValueError("The Account Holder Name cannot be empty")



`__post_init__()` is a suitable place for these checks Because during the onject instantiation this methods checks the invalid values and raises the exceptions which prevents the creating object the invalid intance attribute values.

This ensures that all attributes are fully available for validation checks before the object is completely instantiated, preventing the creation of an invalid object.


```

### Q13. `frozen=True` — 4 marks

Consider:

```python
@dataclass(frozen=True)
class Config:
    host: str
    port: int
```

Then:

```python
config = Config("localhost", 8000)
config.port = 9000
```

Answer:

**a)** What happens?

**b)** Why would making a configuration object frozen sometimes be useful?

**c)** Does `frozen=True` mean that every object contained inside the dataclass can never be mutated? Explain carefully.

---

# Ans:

a: Executing config.port = 9000 will raise and error bcz using @dataclass(frozen=True) where the frozen=True makes the intance attributes of this class to immutable means once the state of the attributes are intialized then it cannot be modified.

b: Making a configuration object frozen helps in making object intance state as immutbale this prevents the accidental mutation to object state.

c: No frozen=True only prevents us to assign a new value directly to the dataclass attributes. However, if an attribute holds a mutable object like a list,dict,set the contents inside that object can be still modified.






