import json
from pathlib import Path

import requests

from load_config import get_project_root, load_api_key, load_location_master, load_yaml_config


def build_meteoblue_params(location_row, api_key):
    """
    Builds the request parameters for the Meteoblue basic-day API.
    """

    params = {
        "lat": float(location_row["latitude"]),
        "lon": float(location_row["longitude"]),
        "apikey": api_key,
        "format": "json",
    }

    return params


def call_meteoblue_api(base_url, params):
    """
    Calls the Meteoblue API and returns the JSON response.
    The API key is masked before printing the URL.
    """

    response = requests.get(base_url, params=params, timeout=60)

    print("API Status Code:", response.status_code)

    safe_url = response.url.replace(params["apikey"], "****")
    print("API URL:", safe_url)

    response.raise_for_status()

    return response.json()


def save_raw_response(response_json, location_id):
    """
    Saves the raw Meteoblue API response as a JSON file.
    """

    project_root = get_project_root()
    raw_dir = project_root / "data" / "raw"
    raw_dir.mkdir(parents=True, exist_ok=True)

    output_file = raw_dir / f"meteoblue_basic_day_{location_id}.json"

    with open(output_file, "w", encoding="utf-8") as file:
        json.dump(response_json, file, indent=4)

    return output_file


def extract_weather_for_first_location():
    """
    Extracts weather data for the first location in location_master.csv.
    """

    config = load_yaml_config()
    locations = load_location_master()
    api_key = load_api_key()

    base_url = config["meteoblue"]["base_url"]

    location_row = locations.iloc[0]
    location_id = location_row["location_id"]

    print("Starting Meteoblue extraction")
    print("Location ID:", location_id)
    print("Location Name:", location_row["location_name"])
    print("Latitude:", location_row["latitude"])
    print("Longitude:", location_row["longitude"])
    print("Base URL:", base_url)

    params = build_meteoblue_params(location_row, api_key)
    response_json = call_meteoblue_api(base_url, params)

    output_file = save_raw_response(response_json, location_id)

    print("\nRaw API response saved successfully:")
    print(output_file)

    return response_json, output_file


if __name__ == "__main__":
    extract_weather_for_first_location()