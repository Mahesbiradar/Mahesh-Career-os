try:
    print("A")

    with open("missing.txt", "r") as file:
        print("B")

except FileNotFoundError:
    print("C")

else:
    print("D")

finally:
    print("E")

print("F")