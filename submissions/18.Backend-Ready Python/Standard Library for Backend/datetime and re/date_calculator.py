
""""
[ ] 1. Exercise 1 — Date and duration calculator

Easy
10 marks

Create `date_calculator.py`. Accept two dates in `YYYY-MM-DD` format. Parse them, print the number of days between them, 
calculate the date 30 days after the first date, and handle invalid dates gracefully. Use `datetime` and `timedelta`.

"""

from datetime import date,time,datetime,timedelta


def calculate_due(start,end):


    try:
        first_date = datetime.strptime(start, "%Y-%m-%d")
        second_date = datetime.strptime(end, "%Y-%m-%d")

        difference = second_date - first_date
        print(f"Days between dates: {difference.days} days")

        new_date  = first_date + timedelta(days=30)

        new_date_str = new_date.strftime("%Y-%m-%d")
        print(f"Date 30 days after first date: {new_date_str}")

        return difference.days, new_date_str


    except ValueError as e:

        print(f"Error: Invalid date format. Please use YYYY-MM-DD. ({e})")
        return None


# Example usage to verify the code works:
if __name__ == "__main__":
    print("--- Test Case 1: Valid Dates ---")
    calculate_due("2026-10-16", "2026-11-20")
    
    print("\n--- Test Case 2: Invalid Date Format ---")
    calculate_due("16-10-2026", "2026-11-20")



    

