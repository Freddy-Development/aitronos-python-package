import json
import os


class Config:
    """Handles loading configuration data from a JSON file."""

    @staticmethod
    def _get_config_file() -> str:
        """Returns the path to the config.json file."""
        return os.path.join(os.path.dirname(__file__), "config.json")

    @staticmethod
    def _load_config() -> dict:
        """Loads the configuration from the config.json file."""
        config_file = Config._get_config_file()

        if os.path.exists(config_file):
            with open(config_file, "r") as file:
                return json.load(file)
        else:
            raise FileNotFoundError(
                f"{config_file} not found. Please add your configuration to this file and ensure it's ignored by git."
            )

    @staticmethod
    def test_key() -> str:
        """Returns the test API key."""
        config = Config._load_config()
        if "test_key" not in config:
            raise KeyError(
                "Couldn't find key 'test_key' in 'config.json'. Please ensure the file contains this key."
            )
        return config["test_key"]

    @staticmethod
    def test_email() -> str:
        """Returns the test email."""
        config = Config._load_config()
        if "test_email" not in config:
            raise KeyError(
                "Couldn't find key 'test_email' in 'config.json'. Please ensure the file contains this key."
            )
        return config["test_email"]

    @staticmethod
    def test_password() -> str:
        """Returns the test password."""
        config = Config._load_config()
        if "test_password" not in config:
            raise KeyError(
                "Couldn't find key 'test_password' in 'config.json'. Please ensure the file contains this key."
            )
        return config["test_password"]

    @staticmethod
    def load_token() -> str:
        """Returns the test API token."""
        config = Config._load_config()
        if "test_token" not in config:
            raise KeyError(
                "Couldn't find key 'test_token' in 'config.json'. Please ensure the file contains this key."
            )
        return config["test_token"]

    @staticmethod
    def user_token() -> str:
        """Returns the user token."""
        config = Config._load_config()
        if "user_token" not in config:
            raise KeyError(
                "Couldn't find key 'user_token' in 'config.json'. Please ensure the file contains this key."
            )
        return config["user_token"]

    @staticmethod
    def test_user_id() -> int:
        """Returns the test user ID."""
        config = Config._load_config()
        if "test_user_id" not in config:
            raise KeyError(
                "Couldn't find key 'test_user_id' in 'config.json'. Please ensure the file contains this key."
            )
        return config["test_user_id"]

    @staticmethod
    def test_username() -> str:
        """Returns the test username."""
        config = Config._load_config()
        if "test_username" not in config:
            raise KeyError(
                "Couldn't find key 'test_username' in 'config.json'. Please ensure the file contains this key."
            )
        return config["test_username"]

    @staticmethod
    def test_email() -> str:
        """Returns the test email."""
        config = Config._load_config()
        if "test_email" not in config:
            raise KeyError(
                "Couldn't find key 'test_email' in 'config.json'. Please ensure the file contains this key."
            )
        return config["test_email"]

    @staticmethod
    def test_full_name() -> str:
        """Returns the test full name."""
        config = Config._load_config()
        if "test_full_name" not in config:
            raise KeyError(
                "Couldn't find key 'test_full_name' in 'config.json'. Please ensure the file contains this key."
            )
        return config["test_full_name"]
