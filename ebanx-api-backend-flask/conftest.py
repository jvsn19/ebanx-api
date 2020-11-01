import pytest

from app import create_app
from app.db import CustomDatabase
from app.models import Account

def mock_database():
    # Mock database with previous values
    CustomDatabase._accounts['123'] = Account(123, 200)
    CustomDatabase._accounts['456'] = Account(456, 100)

@pytest.fixture
def app():
    return create_app().test_client()

@pytest.fixture
def db():
    mock_database()

    return CustomDatabase
