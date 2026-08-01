## TODAY'S ASSIGNMENT

# Goal: Build a `BankAccount` class that uses `@property`, `@setter`, and `@deleter` to control access to the account balance with validation and logging.

# - [ ] Create a `BankAccount` class with a private-by-convention attribute `_balance` initialized in `__init__` (default 0)

class BankAccount():

    def __init__(self,balance=0):
        self._balance = balance

# - [ ] Define a `@property` named `balance` that returns the current `_balance` value

    @property
    def balance(self):
        return self._balance

# - [ ] Define a `@balance.setter` that only allows setting `_balance` to a non-negative number; if a negative value is passed, raise a `ValueError` with the exact message: `Balance cannot be negative`

    @balance.setter
    def balance(self,value):
       
        if value < 0:
            raise ValueError ("Balance cannot be negative")
        self._balance = value      


# - [ ] Define a `@balance.deleter` that prints the exact line: `Balance deleted for account`

    @balance.deleter
    def balance(self):
        print("Balance deleted for account")


# - [ ] After creating an account, set the balance to `500`, then print the exact line: `Current balance: 500`

account = BankAccount()

account.balance = 500

print(f"Current balance: {account.balance}")

# - [ ] (Stretch) Try to set the balance to `-100`, catch the `ValueError`, and print the exact line: `Error: Balance cannot be negative`

try:
    account.balance = -100
except ValueError as e:
    print(f"Error: {e}")

## REVISION CHECK (answer without looking — 2 min)


# 1. In inheritance, what does `super().__init__(...)` do inside a child class's `__init__` method?

"""
In inheritance the super().__init__(...) allow the child class to inherit the attributes and the methods of the parent class.

"""
# 2. Why is exact output label matching important? (Think back to Day 14's `Raise amount:` gap.)

"""
The exact output matching is improtant meet the give specs in the assignment if we dont keep the exact output maching labels it may considered as wrong assignment.

"""



     



