import pytest
import requests

from random import randrange
from configurations import REQUEST_URL

@pytest.fixture(scope='function')
def get_users():
    response = requests.get(REQUEST_URL)
    return response

@pytest.fixture
def get_number():
    return randrange(1, 1000, 5)

def _calculate(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return a+b
    else:
        return None

@pytest.fixture
def calculate():
    return _calculate

@pytest.fixture
def make_number():
    print('I am getting number')
    number = randrange(1, 1000, 5)
    yield number
    print(f'number at home {number}')

