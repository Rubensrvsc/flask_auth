import os
from distutils.util import strtobool
from typing import Optional

def get_env(key: str) -> Optional[str]:
    try:
        return os.environ[key]
    except KeyError:
        return None

JWT_SECRET_KEY = get_env("JWT_SECRET_KEY")
DB_PATH = get_env("DB_PATH")