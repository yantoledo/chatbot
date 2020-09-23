import pytest
from telebot.__init__ import create_app


@pytest.fixture(scope="module")
def app():
    return create_app()



