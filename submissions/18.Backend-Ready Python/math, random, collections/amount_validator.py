"""
Exercise M2 — Safe Amount Validator
Build amount_validator.py.

Requirements:
- Create validate_amount(value).
- Accept ordinary non-negative integers and floats.
- Reject booleans, strings, negative values, NaN, and positive or negative infinity.
- Use math.isfinite() appropriately.
- Write at least eight test cases and print whether each input is accepted or rejected.
Think about the order of checks: a boolean is an instance of int in Python, so a type check alone can be misleading.

"""

import math

def validate_amount(value):

    if isinstance(value,str):

        raise ValueError("The value cannot be string data")
    

    if isinstance(value, bool):

        raise ValueError("The value cannot be boolean")

    if not isinstance(value, (int, float)):

        raise ValueError("The value shoud be int or float")

    if not math.isfinite(value):

        raise ValueError("The value shoud be finit")
    
    if value < 0:
    
        raise ValueError("The value cannot be negative")
  
    return value


test_cases = [
    # Valid Inputs
    100,                  # Ordinary Int
    10.5,                 # Ordinary Float
    0,                    # Zero Boundary
    
    # Sanitisation Cases (Strings that should pass)
    " 42 ",               # String integer with whitespace
    "99.99",              # String float
    
    # Invalid Inputs (Should be rejected)
    True,                 # Boolean
    "one hundred",        # Invalid String text
    "12.34.56",           # Malformed numeric string
    -5.5,                 # Negative value
    float('nan'),         # NaN
    float('inf')          # Infinity
]

print("--- RUNNING SANITISATION & VALIDATION SUITE ---")
for case in test_cases:
    try:
        sanitized_value = validate_amount(case)
        print(f"ACCEPTED: Original: {repr(case)} -> Sanitised Out: {repr(sanitized_value)}")
    except (ValueError, TypeError) as e:
        print(f"REJECTED: Original: {repr(case)} -> Reason: {e}")

