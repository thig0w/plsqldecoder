# -*- coding: utf-8 -*-
"""Global pytest fixtures."""
import pytest
from fastapi.testclient import TestClient
from plsqldecoder import create_app


@pytest.fixture
def app():
    app = create_app("testing")
    return app


@pytest.fixture
def client(app):
    client = TestClient(app)
    return client
