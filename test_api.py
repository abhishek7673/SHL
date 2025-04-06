# import requests

# API_URL = "https://shl-2m13.onrender.com/recommend"

# payload = {
#     "query": "software engineer with strong problem-solving skills"
# }

# response = requests.post(API_URL, json=payload)

# if response.status_code == 200:
#     print("✅ API call succeeded")
#     print(response.json())
# else:
#     print("❌ API call failed")
#     print(response.status_code, response.text)

import requests

url = "https://shl-2m13.onrender.com/recommend"
payload = {"query": "data analyst"}

try:
    res = requests.post(url, json=payload)
    res.raise_for_status()
    print("✅ API Response:")
    print(res.json())
except Exception as e:
    print("❌ API call failed:", e)
    exit(1)
