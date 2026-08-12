from app.users.service import create_user

from app.products.service import create_product

import requests


response = requests.get("https://github.com")

if response.status_code == 200:
    print("✅ Success! Your virtual environment and requests package are working perfectly.")
else:
    print(f"❌ Connection made, but server returned status code: {response.status_code}")




if __name__ == "__main__":

    user = create_user("Mahesh","Maheshbiradar@example.com")

    product = create_product("Laptop",55000)

    print(f"User: {user}")

    print(f"Product: {product}")





"""
Explanation:

Part D — Main Guard

to execute the application.
Explain why this is useful.

the main guard  is useful for code that should run only when the file is executed directly.

Part F — Environment

What remains after deactivation?

All the files remains same just the virtual environment gets deactivated.

Part G — Architecture Explanation
What is:

app?
users?
products?
service.py?
__init__.py?

the app is main package contains all the nested packages which contains all related modules.
users also is packages contains the module service.py
service.py is single file consist of reusable code and its called the module.
__init__.py file contains the initialization code for the package and marks a directory as a Python package


"""