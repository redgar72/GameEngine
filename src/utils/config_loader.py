import json
import os
from typing import Dict, Any
from .logger import logger


class ConfigLoader:
    def __init__(self, config_path: str = "config/settings.json"):
        self.config_path = config_path
        self.config: Dict[str, Any] = {}
        logger.debug(
            f"Initializing ConfigLoader with path: {config_path}"
        )
        self.load_config()

    def load_config(self) -> None:
        """Load configuration from JSON file."""
        try:
            logger.debug(f"Loading config from {self.config_path}")
            with open(self.config_path, 'r') as f:
                self.config = json.load(f)
            logger.info("Configuration loaded successfully")
        except FileNotFoundError:
            logger.warning(f"Config file not found at {self.config_path}")
            self.config = {}
        except json.JSONDecodeError:
            logger.error(
                f"Invalid JSON in config file {self.config_path}"
            )
            self.config = {}

    def get(self, key: str, default: Any = None) -> Any:
        """Get a configuration value using dot notation."""
        keys = key.split('.')
        value = self.config

        for k in keys:
            if isinstance(value, dict) and k in value:
                value = value[k]
            else:
                logger.debug(
                    f"Config key '{key}' not found, "
                    f"using default: {default}"
                )
                return default

        return value

    def save_config(self) -> None:
        """Save current configuration to file."""
        try:
            os.makedirs(os.path.dirname(self.config_path), exist_ok=True)
            with open(self.config_path, 'w') as f:
                json.dump(self.config, f, indent=4)
            logger.info(f"Configuration saved to {self.config_path}")
        except Exception as e:
            logger.error(f"Error saving config: {e}")
