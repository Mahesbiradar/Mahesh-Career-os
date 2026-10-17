"""
4. Exercise 4 — Extract order IDs from logs

Medium
10 marks

Create `order_extractor.py`. Given a string containing multiple order IDs such as `ORD-100`, `ORD-2048`, and `ORD-77`, 
extract all IDs with `re.findall()`. Also extract the numeric portion using a capturing group and report the number of IDs found.

"""

import re

def order_extractor(string):

    pattern = r"(ORD-(\d+))"

    matches  = re.findall(pattern,string)

    count  = len(matches)

    print(f"Total Order IDs found: {count}")

    full_ids = [match[0] for match in matches]

    numeric_portions = [match[1] for match in matches]

    print("Full IDs extracted:", full_ids)

    print("Numeric portions extracted:", numeric_portions)

    return full_ids, numeric_portions


if __name__ == "__main__":
    print("--- Running Order Extractor Test ---")
    log_data = "Log Entry: User processed ORD-100, then completed ORD-2048. System flagged error on ORD-77."
    
    full, numbers = order_extractor(log_data)

