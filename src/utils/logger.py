import logging
import os
from datetime import datetime
from typing import Optional, Dict, Any


class Logger:
    _instance: Optional['Logger'] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Logger, cls).__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self):
        if self._initialized:
            return

        self._initialized = True
        self._setup_logging()

    def _setup_logging(self):
        """Set up the logging configuration with default settings."""
        # Create logs directory if it doesn't exist
        log_dir = 'logs'
        os.makedirs(log_dir, exist_ok=True)

        # Generate log filename with timestamp
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        log_file = os.path.join(log_dir, f'game_{timestamp}.log')

        # Configure logging with default settings
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(log_file),
                logging.StreamHandler()
            ]
        )

        self.logger = logging.getLogger('GameEngine')
        self.logger.info(f"Logging system initialized. Log file: {log_file}")

    def configure(self, config: Dict[str, Any]) -> None:
        """Configure the logger with settings from config."""
        log_dir = config.get('logging.directory', 'logs')
        os.makedirs(log_dir, exist_ok=True)

        # Generate log filename with timestamp
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        log_file = os.path.join(log_dir, f'game_{timestamp}.log')

        # Get log level from config or default to INFO
        log_level = config.get('logging.level', 'INFO').upper()
        numeric_level = getattr(logging, log_level, logging.INFO)

        # Remove existing handlers
        for handler in self.logger.handlers[:]:
            self.logger.removeHandler(handler)

        # Add new handlers with updated configuration
        self.logger.addHandler(logging.FileHandler(log_file))
        self.logger.addHandler(logging.StreamHandler())
        self.logger.setLevel(numeric_level)

        self.logger.info(f"Logger reconfigured. Log file: {log_file}")

    def debug(self, message: str):
        """Log a debug message."""
        self.logger.debug(message)

    def info(self, message: str):
        """Log an info message."""
        self.logger.info(message)

    def warning(self, message: str):
        """Log a warning message."""
        self.logger.warning(message)

    def error(self, message: str):
        """Log an error message."""
        self.logger.error(message)

    def critical(self, message: str):
        """Log a critical message."""
        self.logger.critical(message)


# Create global logger instance
logger = Logger()
