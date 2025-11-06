import os
import requests
from dotenv import load_dotenv

load_dotenv('.env.local')
CONVEX_URL = os.getenv('CONVEX_URL')

data = {
  "model": "test-model",
  "battery_backup": 10.5,
  "processor_name": "test-processor",
  "processor_generation": "11th",
  "processor_wattage": 35,
  "ram_size": 16,
  "ram_generation": "DDR4",
  "gpu": "NVIDIA GeForce RTX 3060",
  "gpu_vram": 6,
  "ssd_size": 512,
  "hdd_size": 1024,
  "display_size": 15.6,
  "display_resolution": "1920x1080",
  "time_used_in_moths": 12,
  "price": 1200,
  "url": "https://example.com/test-model",
  "image_urls": ["https://example.com/test-model/image1.jpg", "https://example.com/test-model/image2.jpg"],
  "posted_at": "2023-10-01"
}

payload = {
  "path": "insertData:insertBikroyPost",
  "args": data,
  "format": "json"
}

response = requests.post(f"{CONVEX_URL}/api/mutation", json=payload)

if response.status_code == 200:
    print("✅ Sent to Convex:", response.status_code, response.json())
else:
    print("❌ Error:", response.status_code, response.text)