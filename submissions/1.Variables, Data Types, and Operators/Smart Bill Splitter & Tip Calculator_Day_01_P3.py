"""
Section 3: Mini Project
🧮 "Smart Bill Splitter & Tip Calculator"
Goal: Combine variables, data types, operators with conditionals, input/output, and string formatting to build a practical calculator.
Requirements:
Create variables (using input()) to capture:
bill_amount (float)
num_people (int)
service_rating (str) — user types: excellent, good, average, or poor
tax_rate (float, e.g., 0.08 for 8%)
Use conditionals + operators to:
Validate: if bill_amount <= 0 or num_people <= 0, print "Invalid input. Bill and people must be positive." and stop.
Determine tip % based on rating:
excellent → 20%
good → 15%
average → 10%
poor → 5%
Anything else → print "Unknown rating. Defaulting to 10%." and use 10%
If num_people == 1, print a message: "Dining solo! Treat yourself."
If per-person amount > $50, print: "⚠️ Premium dining alert!"
Use operators to calculate:
tax_amount = bill_amount * tax_rate
tip_amount = bill_amount * tip_rate
total_bill = bill_amount + tax_amount + tip_amount
per_person = total_bill / num_people
Use type conversion/formatting to display:
All currency values rounded to exactly 2 decimal places with a $ prefix.
Tip percentage displayed as an integer with a % sign.
Output a formatted receipt like this:
plain
========== RECEIPT ==========
Original Bill:    $120.00
Tax (8%):         $9.60
Tip (good - 15%): $18.00
-----------------------------
Total:            $147.60
Per Person (3):   $49.20
=============================
Dining solo! Treat yourself.   <-- (if applicable)
⚠️ Premium dining alert!       <-- (if applicable)
Constraints:
❌ No functions (def)
❌ No loops
✅ Only variables, operators, conditionals (if/elif/else), and print()
"""




# Section 3: Mini Project
# 🧮 "Smart Bill Splitter & Tip Calculator"

# 1. Create variables (using input()) to capture:
bill_amount = float(input("Enter the bill amount: "))
num_people = int(input("Enter the number Peoples: "))
service_rating = input("Please rate the service ex: excellent, good, average, or poor: ").strip()
tax_rate = float(input("Enter the Tax rate on bill amount e.g., 0.08 for 8% : "))

# 2. Use conditionals + operators to validate:
if bill_amount <= 0 or num_people <= 0:
    print("Invalid input. Bill and people must be positive.")
else:
    rating_percentile = None
    tip_rate = None
    
    if service_rating.lower() == "excellent":
        rating_percentile = "20%"
        tip_rate = 0.20
    elif service_rating.lower() == "good":
        rating_percentile = "15%"
        tip_rate = 0.15
    elif service_rating.lower() == "average":
        rating_percentile = "10%"
        tip_rate = 0.10
    elif service_rating.lower() == "poor":
        rating_percentile = "5%"
        tip_rate = 0.05
    else:
        print("Unknown rating. Defaulting to 10%.")
        rating_percentile = "10%"
        tip_rate = 0.10

    # Use operators to calculate:
    tax_amount = bill_amount * tax_rate
    tip_amount = bill_amount * tip_rate
    total_bill = bill_amount + tax_amount + tip_amount
    per_person = total_bill / num_people

    # 4. Output a formatted receipt with fixed 2-decimal point precision (:.2f)
    print("========== RECEIPT ==========")
    print(f"Original Bill: ${bill_amount:.2f}")
    print(f"Tax ({tax_rate * 100:.0f}%): ${tax_amount:.2f}")
    print(f"Tip ({service_rating} - {rating_percentile}): ${tip_amount:.2f}")
    print("-----------------------------")
    print(f"Total: ${total_bill:.2f}")
    print(f"Per Person ({num_people}): ${per_person:.2f}")
    print("=============================")

    # 5. Conditional Alerts (Indented inside 'else' to prevent crash)
    if num_people == 1:
        print("Dining solo! Treat yourself.")
        
    if per_person > 50:
        print("⚠️ Premium dining alert!")







    





