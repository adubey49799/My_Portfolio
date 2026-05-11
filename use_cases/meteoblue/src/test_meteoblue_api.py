from pathlib import Path
import os
import requests
from dotenv import load_dotenv


PROJECT_ROOT = Path(__file__).resolve().parents[1]


def load_api_key() -> str:
    load_dotenv(PROJECT_ROOT / ".env")
    api_key = os.getenv("METEOBLUE_API_KEY")

    if not api_key:
        raise ValueError("METEOBLUE_API_KEY was not found.")

    return api_key


if __name__ == "__main__":
    api_key = load_api_key()

    url = "https://my.meteoblue.com/packages/basic-day"

    params = {
        "apikey": api_key,
        "lat": 34.12345,
        "lon": -78.23456,
        "asl": 0,
        "format": "json",
    }

    response = requests.get(url, params=params, timeout=60)

    print("Status code:", response.status_code)
    print("Content type:", response.headers.get("Content-Type"))
    print("First 500 characters of response:")
    print(response.text[:500])
