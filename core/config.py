# core/config.py
# configurations.

import logging.config
import sys
from pathlib import Path

from rich.logging import RichHandler

# Constants
FILE_NAME = "credit_card_transactions.csv"
FILE_SOURCE = "https://web.cs.dal.ca/~kalisamy/Dataset/credit_card_transactions.csv"
MODEL_NAME = "model.joblib"
REGISTERED_MODEL_NAME = "FradulantCreditTransactions"
BEST_MODEL_PARAM = "best_model_param.json"
OPTUNA_TRIALS_COUNT = 1

# Directories
BASE_DIR = Path(__file__).parent.parent.absolute()
CONFIG_DIR = Path(BASE_DIR, "config")
LOGS_DIR = Path(BASE_DIR, "logs")
DATA_DIR = Path(BASE_DIR, "data")
MODEL_DIR = Path(BASE_DIR, "model")
STORES_DIR = Path(BASE_DIR, "stores")
ARTIFACTS_DIR = Path(BASE_DIR, "artifacts")
SERVING_MODEL_DIR = Path(BASE_DIR, "serving")


# Local stores
BLOB_STORE = Path(STORES_DIR, "blob")
FEATURE_STORE = Path(STORES_DIR, "feature")
MODEL_REGISTRY = Path(STORES_DIR, "model")

# Create dirs
CONFIG_DIR.mkdir(parents=True, exist_ok=True)
LOGS_DIR.mkdir(parents=True, exist_ok=True)
DATA_DIR.mkdir(parents=True, exist_ok=True)
MODEL_DIR.mkdir(parents=True, exist_ok=True)
STORES_DIR.mkdir(parents=True, exist_ok=True)
ARTIFACTS_DIR.mkdir(parents=True, exist_ok=True)
BLOB_STORE.mkdir(parents=True, exist_ok=True)
FEATURE_STORE.mkdir(parents=True, exist_ok=True)
MODEL_REGISTRY.mkdir(parents=True, exist_ok=True)
SERVING_MODEL_DIR.mkdir(parents=True, exist_ok=True)

# Logger
logging_config = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "minimal": {"format": "%(message)s"},
        "detailed": {
            "format": "%(levelname)s %(asctime)s [%(filename)s:%(funcName)s:%(lineno)d]\n%(message)s\n"
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "stream": sys.stdout,
            "formatter": "minimal",
            "level": logging.DEBUG,
        },
        "info": {
            "class": "logging.handlers.RotatingFileHandler",
            "filename": Path(LOGS_DIR, "info.log"),
            "maxBytes": 10485760,  # 1 MB
            "backupCount": 10,
            "formatter": "detailed",
            "level": logging.INFO,
        },
        "error": {
            "class": "logging.handlers.RotatingFileHandler",
            "filename": Path(LOGS_DIR, "error.log"),
            "maxBytes": 10485760,  # 1 MB
            "backupCount": 10,
            "formatter": "detailed",
            "level": logging.ERROR,
        },
    },
    "loggers": {
        "root": {
            "handlers": ["console", "info", "error"],
            "level": logging.INFO,
            "propagate": True,
        },
    },
}
logging.config.dictConfig(logging_config)
logger = logging.getLogger("root")
logger.handlers[0] = RichHandler(markup=True)
