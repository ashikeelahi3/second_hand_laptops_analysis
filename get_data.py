import requests
import os
from dotenv import load_dotenv

load_dotenv('.env.local')
CONVEX_URL = os.getenv('CONVEX_URL')

def getPrices(model=None):
  if not CONVEX_URL:
    raise ValueError("CONVEX_URL not found in environment")

  payload = {
    "path": "insertData:getData",
    "args": {},
    "format": "json"
  }
  response = requests.post(f"{CONVEX_URL}/api/query", json=payload)
  if response.status_code == 200:
    data = response.json()
    if model:
      return [item for item in data if item.get('model') == model]
    return data
  else:
    print(f"Error: {response.status_code} - {response.text}")
    return None

result = getPrices()
print("✅ Retrieved from Convex:", result)