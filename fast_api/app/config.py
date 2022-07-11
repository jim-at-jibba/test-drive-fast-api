# File where all configuration variables are stored
# https://fastapi.tiangolo.com/advanced/settings/

import logging
import os
from functools import lru_cache

from pydantic import BaseSettings


log = logging.getLogger("uvicorn")

class Settings(BaseSettings):
    environment: str = os.getenv("ENVIRONMENT", "dev")
    testing: bool = os.getenv("TESTING", False)


@lru_cache()
def get_settings() -> BaseSettings:
    log.info("loading config settings from the environment...")
    return Settings()

