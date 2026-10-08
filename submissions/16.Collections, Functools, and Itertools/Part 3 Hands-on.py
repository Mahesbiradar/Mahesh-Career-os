# 🧪 Part 3 Hands-on

# Exercise 9 — product()

"""
Create combinations for an API testing system:
methods = ["GET", "POST"]environments = ["dev", "prod"]


Use product() to generate every possible combination.
Expected result:
('GET', 'dev')
('GET', 'prod')
('POST', 'dev')
('POST', 'prod')

Also print the total number of combinations.

"""

from itertools import product


methods = ["GET", "POST"]
environments = ["dev", "prod"]

result = list(product(methods,environments))

print(result)


# Exercise 10 — permutations()

"""
You have three servers:
servers = ["server1", "server2", "server3"]


Generate all possible full-length deployment orders.
Expected:
('server1', 'server2', 'server3')
...

Then print the total number of possible deployment orders.

"""

from itertools import permutations

list_of = ('server1', 'server2', 'server3')

result = list(permutations(list_of))

print(result)


# Exercise 11 — groupby()

"""
You receive these already sorted records:
records = [    ("admin", "Mahesh"),    ("admin", "Rahul"),    ("user", "Amit"),    ("user", "Sneha"),    ("manager", "Priya"),    ("manager", "Arjun")]


Use groupby() to produce:
admin -> ['Mahesh', 'Rahul']
user -> ['Amit', 'Sneha']
manager -> ['Priya', 'Arjun']

Important: Don't use defaultdict here. The purpose is specifically to practice groupby().

"""

records = [
    ("admin", "Mahesh"),
    ("admin", "Rahul"),
    ("user", "Amit"),
    ("user", "Sneha"),
    ("manager", "Priya"),
    ("manager", "Arjun")
]


from itertools import groupby

result = []

for role, user in groupby(records,key=lambda x:x[0]):

    print(role,list(user))

   
# Exercise 12 — chain()

db_records = ["DB1", "DB2", "DB3"]
cache_records = ["CACHE1", "CACHE2"]
api_records = ["API1", "API2", "API3"]



from itertools import chain


result = list(chain(db_records,cache_records,api_records))


print(result)



# itertools.chain() is preferable because it does not create a new list in memory.


# Manual combining (list1 + list2) copies all elements into a brand-new list, doubling your memory usage and causing noticeable lag or crashes with large datasets.
# itertools.chain() creates an iterator that streams items one by one directly from the original lists. It uses zero extra memory and starts up instantly.


    
