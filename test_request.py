# test_requests.py

import requests

try:
    response = requests.get("https://httpbin.org/get", timeout=10)
    response.raise_for_status()
    print("✅ Request successful!")
    print(response.json())

except requests.exceptions.Timeout:
    print("⏱️ Timeout error")

except requests.exceptions.RequestException as e:
    print("❌ General error:", e)
