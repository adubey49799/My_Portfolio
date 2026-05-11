from pathlib import Path
import os

import pandas as pd
import yaml
from dotenv import load_dotenv


PROJECT_ROOT = Path(__file__).resolve().parents[1]


def load_api_key() -> str:
    env_path = PROJECT_ROOT / ".env"
    load_dotenv(env_path)

    api_key = os.getenv("METEOBLUE_API_KEY")

    if not api_key:
        raise ValueError("METEOBLUE_API_KEY was not found. Please check your .env file.")

    return api_key


def load_config() -> dict:
    config_path = PROJECT_ROOT / "config" / "meteoblue_config.yaml"

    if not config_path.exists():
        raise FileNotFoundError(f"Config file not found: {config_path}")

    with open(config_path, "r", encoding="utf-8") as file:
        config = yaml.safe_load(file)

    return config


def load_locations(config: dict) -> pd.DataFrame:
    input_file = PROJECT_ROOT / config["input"]["file_path"]

    if not input_file.exists():
        raise FileNotFoundError(f"Input file not found: {input_file}")

    df = pd.read_csv(input_file)

    required_columns = [
        "location_id",
        "latitude",
        "longitude",
        "country_code",
        "start_date",
        "end_date",
    ]

    missing_columns = [col for col in required_columns if col not in df.columns]

    if missing_columns:
        raise ValueError(f"Missing required input columns: {missing_columns}")

    df["latitude"] = pd.to_numeric(df["latitude"], errors="coerce")
    df["longitude"] = pd.to_numeric(df["longitude"], errors="coerce")
    df["start_date"] = pd.to_datetime(df["start_date"], errors="coerce")
    df["end_date"] = pd.to_datetime(df["end_date"], errors="coerce")

    df = df.dropna(subset=["latitude", "longitude", "start_date", "end_date"])

    return df


if __name__ == "__main__":
    api_key = load_api_key()
    config = load_config()
    locations_df = load_locations(config)

    print("API key loaded successfully.")
    print("API key length:", len(api_key))
    print()
    print("Config loaded successfully:")
    print(config)
    print()
    print("Locations loaded successfully:")
    print(locations_df)
