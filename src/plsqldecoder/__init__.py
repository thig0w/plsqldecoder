# -*- coding: utf-8 -*-
"""fastAPI app initialization via factory pattern."""
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from plsqldecoder.api import decoder
from plsqldecoder.config import get_config

# TODO: use versioneer
__version__ = "0.1.1"


def create_app(config_name):
    config = get_config(config_name)
    app = FastAPI(
        title=config.project_name,
        docs_url=config.openapi_url,
        redoc_url=config.redoc_url,
        openapi_tags=[],
        debug=config.debug,
        version=__version__,
    )

    @app.get("/", include_in_schema=False)
    def redirect_to_docs() -> RedirectResponse:
        return RedirectResponse("/docs")

    app.include_router(decoder.endpoints.router, prefix=config.api_v1_route)
    app.openapi_tags += decoder.endpoints.tags_metadata

    return app
