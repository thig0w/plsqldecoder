# -*- coding: utf-8 -*-
"""Config settings for for development, testing and production environments."""
import os
import secrets
from pathlib import Path
from functools import lru_cache

from pydantic import BaseSettings

HERE = Path(__file__).parent


# SQLITE_DEV = "sqlite:///" + str(HERE / "disponible_dev.db")
# SQLITE_TEST = "sqlite:///" + str(HERE / "disponible_test.db")
# SQLITE_PROD = "sqlite:///" + str(HERE / "disponible_prod.db")


class BaseAPISettings(BaseSettings):
    api_v1_route: str = "/api/v1"
    project_name: str = "plsqldecoder"
    openapi_url: str = "/docs"
    redoc_url: str = "/redoc"
    debug: bool = False


class DevAPISettings(BaseAPISettings):
    """Development configuration."""

    debug: bool = True


class TestAPISettings(BaseAPISettings):
    """Test configuration."""

    debug: bool = True


class ProdAPISettings(BaseAPISettings):
    """Production configuration."""

    debug: bool = False


ENV_CONFIG_DICT = dict(
    development=DevAPISettings, testing=TestAPISettings, production=ProdAPISettings
)


@lru_cache()
def get_config(config_name):
    """Retrieve environment configuration settings."""
    return ENV_CONFIG_DICT.get(config_name, ProdAPISettings)()
