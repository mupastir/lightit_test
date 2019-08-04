import os
import logging

from core.constants import APP_ENV_DEV, APP_ENV_PROD


class Config:

    DEBUG = False
    HOST = '127.0.0.1'
    LOG_LEVEL = logging.INFO
    TOKEN = os.environ.get('TOKEN', None)


class ProdConfig(Config):
    LOG_LEVEL = logging.ERROR


class DevConfig(Config):
    DEBUG = True


def runtime_config():
    env = os.environ.get("APP_ENV", APP_ENV_DEV).strip().lower()
    if env == APP_ENV_PROD:
        return ProdConfig

    return DevConfig
