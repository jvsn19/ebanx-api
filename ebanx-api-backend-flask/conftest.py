import pytest

from app import create_app
from app.db import CustomDatabase
from app.models import Account

@pytest.fixture
def app():
    return create_app().test_client()

@pytest.fixture
def db():
    class DatabaseHandler:
        def __init__(self):
            self.database = CustomDatabase
            self.id = 0

        def create_account(self, balance = 1000):
            last_id = self.id
            self.id += 1
            CustomDatabase._create_account(str(last_id), balance)

            return last_id

        def reset(self):
            self.database.reset()

    return DatabaseHandler()
