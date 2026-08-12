from shop import users
from shop import products


user = users.create_user("Mahesh")
product_id = products.get_product("101")


print(f"User created: {user}")
print(f"Product ID: {product_id}")

