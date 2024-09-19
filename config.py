import json
import os


class Config:
    @staticmethod
    def load_token():
        """Reads the API token from the config.json file."""
        # Use the absolute path relative to the config.py file location
        config_file = os.path.join(os.path.dirname(__file__), "config.json")

        if os.path.exists(config_file):
            with open(config_file, "r") as file:
                config = json.load(file)
                return config.get("test_token", None)
        else:
            raise FileNotFoundError(
                f"{config_file} not found. Please add your token to this file and ensure it's ignored by git.")