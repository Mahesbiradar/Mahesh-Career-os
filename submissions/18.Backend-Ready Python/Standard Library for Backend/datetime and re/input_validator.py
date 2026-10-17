"""
[ ] 3. Exercise 3 — Employee ID and mobile validator

Easy–Medium
10 marks

Create `input_validator.py`. Write separate functions that validate IDs in the format `EMP-1234` and Indian mobile numbers in the simplified format of 10 digits beginning with 6–9. 
Test valid, invalid, too-short, and extra-character inputs. Use `re.fullmatch()`.

"""

import re

def validate_employee_id(input_string):


    pattern = r"EMP-\d{4}"
    if re.fullmatch(pattern, input_string):
        return True
    return False


def validate_mobile_number(input_string):

    pattern = r"[6-9]\d{9}"

    if re.fullmatch(pattern, input_string):
        return True
    return False

if __name__ == "__main__":

    emp_tests = {
        "EMP-1234": "Valid",
        "EMP-ABCD": "Invalid characters",
        "EMP-12":   "Too short",
        "EMP-12345": "Extra characters (Too long)",
        "abc EMP-1234": "Extra characters at start"
    }


    print("--- Testing Employee ID Validator ---")
    for test_input, expected in emp_tests.items():
        is_valid = validate_employee_id(test_input)
        result_status = "PASS" if (is_valid == (expected == "Valid")) else "FAIL"
        print(r"Input: '{:<14}' -> Result: {:<5} | Expected: {} [{}]".format(
            test_input, str(is_valid), expected, result_status
        ))

    print("\n" + "="*50 + "\n")


    mobile_tests = {
        "9876543210": "Valid",
        "5555555555": "Invalid (Starts with 5)",
        "987654321":  "Too short (9 digits)",
        "98765432101": "Extra characters (11 digits)",
        "987654321a": "Invalid characters"
    }


    print("--- Testing Indian Mobile Validator ---")
    for test_input, expected in mobile_tests.items():
        is_valid = validate_mobile_number(test_input)
        result_status = "PASS" if (is_valid == (expected == "Valid")) else "FAIL"
        print(r"Input: '{:<14}' -> Result: {:<5} | Expected: {} [{}]".format(
            test_input, str(is_valid), expected, result_status
        ))

        




