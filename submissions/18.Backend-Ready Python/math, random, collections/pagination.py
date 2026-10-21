"""
Exercise M1 — API Pagination Calculator
Build pagination.py.

Requirements:
- Create calculate_pages(total_records, page_size).
- Return the number of pages using math.ceil().
- Reject negative record counts.
- Reject zero or negative page sizes.
- Test 0 records, 100 records with page size 10, and 101 records with page size 10.
- Also test invalid inputs.
Expected behaviour: 0 records should require 0 pages; 101 records at 10 per page should require 11 pages.

"""

import math


def calculate_pages(total_records, page_size):


    if isinstance(total_records,str):

        raise ValueError("The records cannot be string object")

    if isinstance(total_records,float):

        raise ValueError("The records cannot be float object")

    if isinstance(page_size,str):
    
        raise ValueError("The size cannot be string object")
    
    if isinstance(page_size,float):

        raise ValueError("The size cannot be float object")
    
    if total_records < 0:

        raise ValueError("total_records cannot be nagative")

    if page_size <= 0 :

        raise ValueError("Page size cannot be zero or negative")


    return math.ceil((total_records + page_size - 1) // page_size)


print(calculate_pages(100,10))
print(calculate_pages(101,10))
print(calculate_pages(0,10))


try :

    calculate_pages(0,0)

except ValueError as e:

    print(f"Rejected (0, 0)   -> Error: {e}")


