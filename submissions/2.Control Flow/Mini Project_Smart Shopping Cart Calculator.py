"""
## Section 3: Mini Project

This combines **Control Flow** with your previous topics: **Variables, Data Types, and Operators**.

---

### 🏗️ Mini Project: Smart Shopping Cart Calculator

Build a command-line shopping cart system. The user enters items one by one. Each item has a **name** (string), **price** (float), and **quantity** (int).

**Requirements:**

1. **Input Loop:** Use a `while` loop to keep asking the user for items. Stop when the user enters `"done"` as the item name.
2. **Validation:** 
   - If price is negative or quantity is negative, print `"Invalid input. Skipping item."` and use `continue`.
   - If price is `0`, print `"Free item added!"`.
3. **Data Storage:** Store each valid item as a tuple `(name, price, quantity)` in a list.
4. **Discount Logic (if/elif/else):**
   - If total cart value (price × quantity, summed) is > $100: apply **10% discount**.
   - If total cart value is > $50: apply **5% discount**.
   - Otherwise: **no discount**.
5. **Receipt Display:** Use a `for` loop with `enumerate()` to print a numbered receipt showing each item's line total.
6. **Final Output:** Print the subtotal, discount amount, and final total. Format all currency to 2 decimal places.

**Example Run:**
```
Enter item name (or 'done'): Apple
Enter price: 2.50
Enter quantity: 4
Enter item name (or 'done'): Milk
Enter price: 3.00
Enter quantity: 2
Enter item name (or 'done'): done

--- RECEIPT ---
1. Apple x 4 @ $2.50 = $10.00
2. Milk x 2 @ $3.00 = $6.00
Subtotal: $16.00
Discount: $0.00
Total: $16.00
```

**Bonus:** Add a `break` feature — if the user enters `"cancel"` at any item name prompt, clear the entire cart and exit the loop immediately.

---

**Write the full program and share it. Once you're done, we'll move to the debugging and output prediction sections.**

"""

data = []

while True:


   name = input("Enter item name (or 'done'): ").strip()

   if name.lower() == "cancel":
      data = []
      break

   if name.lower() == "done":

      break

   price = float(input("Enter price: "))


   quantity = int(input("Enter quantity: "))

   if price < 0 or quantity < 0:
      print("Invalid input. Skipping item.")
      continue

   if price == 0:
      print("Free item added!")

   data.append((name,price,quantity))


if data:
   subtotal = 0
   discount = 0

   print("--- RECEIPT ---")

   for index,(name,price,quantity) in enumerate(data):

      subtotal += price * quantity

      print(f"{index+1}. {name} x {quantity} @ ${price:.2f} = ${price*quantity:.2f}")

   if subtotal > 100:
      discount = subtotal * 0.10
   elif subtotal > 50:
      discount = subtotal * 0.05

   total = subtotal - discount

   print(f"Subtotal: ${subtotal:.2f}")
   print(f"Discount: ${discount:.2f}")
   print(f"Total: ${total:.2f}")


"""

✅ What's Working Well
The while True + break/continue pattern is used correctly.
"cancel" clears the cart and exits immediately — bonus requirement met.
enumerate() is used properly for numbered receipt lines.
Discount tier logic (> 100 then > 50) is correct and ordered properly.
The if data: guard prevents printing an empty receipt.
⚠️ Issues to Fix
1. int() for price — Significant Bug
Python
price = int(input("Enter price: "))      # ❌
Price should accept decimals like 2.50. int() will crash on 2.50 with a ValueError. Use float() instead:
Python
price = float(input("Enter price: "))      # ✅
2. Missing $ in receipt line
Python
print(f"{index+1}. {name} x {quantity} @ ${price:.2f} = {price*quantity:.2f}")
#                                                             ↑
# Missing $ before the total. Should be: = ${price*quantity:.2f}
3. Variable naming convention
Subtotal, Discount, Total use PascalCase. In Python, regular variables should be snake_case:
Python
subtotal = 0
discount = 0
total = subtotal - discount
4. Minor: quantity as int is fine, but what about 0?
If quantity is 0, the item gets added but contributes nothing. Not a bug, but you might want to skip it or warn the user.

"""





