from fastapi import FastAPI
import requests
import time

app = FastAPI()

TARGET_URL = "https://commentchto.onrender.com/ubort/"  # URL bạn muốn fetch đến

@app.get("/")
def fetch_status():
    try:
        response = requests.get(TARGET_URL, timeout=5)
        return {"fetched_url": TARGET_URL, "status_code": response.status_code}
    except requests.RequestException as e:
        return {"fetched_url": TARGET_URL, "error": str(e)}
