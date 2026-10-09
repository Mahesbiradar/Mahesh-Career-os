from collections import defaultdict
users = [    ("Mahesh", "admin"),    ("Rahul", "user"),    ("Amit", "admin")]
# Complete the missing lines

user_dict = defaultdict(list)

for name,role in users:

    user_dict[role].append(name)

print(user_dict)