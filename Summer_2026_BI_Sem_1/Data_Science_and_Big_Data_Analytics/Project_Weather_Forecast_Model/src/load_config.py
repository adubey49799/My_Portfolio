import os
from pathlib import Path

import pandas as pd
import yaml
from dotenv import load_dotenv


def get_project_root():
    """
    Returns the root folder of the Weather Forecast Model project.
    This file is inside src, so parent.parent gives the project root.
    """
    return Path(__file__).resolve().parent.parent


def load_yaml_config(config_path=None):
    """
    Loads the Meteoblue YAML configuration file.
    """
    project_root = get_project_root()

    if config_path is None:
        config_path = project_root / "config" / "meteoblue_config.yaml"

    with open(config_path, "r", encoding="utf-8") as file:
        config = yaml.safe_load(file)

    return config


def load_location_master(location_path=None):
    """
    Loads the location master input file.
    """
    project_root = get_project_root()

    if location_path is None:
        location_path = project_root / "data" / "input" / "location_master.csv"

    location_df = pd.read_csv(location_path)

    return location_df


def load_api_key():
    """
    Loads the Meteoblue API key from the .env file.

    The .env file should contain:
    METEOBLUE_API_KEY=your_api_key_here
    """
    project_root = get_project_root()
    env_path = project_root / ".env"

    load_dotenv(env_path)

    api_key = os.getenv("METEOBLUE_API_KEY")

    if not api_key:
        raise ValueError(
            "METEOBLUE_API_KEY was not found. "
            "Please create a .env file in the project root."
        )

    return api_key


if __name__ == "__main__":
    config = load_yaml_config()
    locations = load_location_master()

    print("Config loaded successfully.")
    print(config)

    print("\nLocation master loaded successfully.")
    print(locations)

    try:
        api_key = load_api_key()
        print("\nAPI key loaded successfully.")
        print("API key length:", len(api_key))
    except ValueError as error:
        print("\nAPI key check failed:")
        print(error)