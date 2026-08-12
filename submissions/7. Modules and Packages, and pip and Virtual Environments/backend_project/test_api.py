import requests


response = requests.get("https://github.com")


if response.status_code == 200:
    print("✅ Success! Your virtual environment and requests package are working perfectly.")
    print(f"Quote from GitHub API: {response.text.strip()}")

else:
    print(f"❌ Connection made, but server returned status code: {response.status_code}")


