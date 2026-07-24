import logging
from pathlib import Path

LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)

logger = logging.getLogger("backend")

logger.setLevel(logging.INFO)

file_handler = logging.FileHandler(
    LOG_DIR / "requests.log",
    encoding="utf-8"
)

formatter = logging.Formatter(
    "%(asctime)s | %(levelname)s | %(message)s"
)

file_handler.setFormatter(formatter)

logger.addHandler(file_handler)
if not logger.handlers:
    logger.addHandler(file_handler)
console_handler = logging.StreamHandler()
