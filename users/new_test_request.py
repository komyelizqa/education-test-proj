import pytest

from src.baseclasses.base_response_second import Response_two
from jsonschemas.users import User


def test_getting_users_list(get_users, get_number,make_number):
    Response_two(get_users).assert_status_code(200).validate(User)
    # print(get_number)
    # print(make_number)

@pytest.mark.skip('[ISSUE-2314] Issue with network connection')
def test_another():
    assert 1==1

def test_calculation_both(calculate):
    print(calculate(-1, -2))

def test_calculation_one(calculate):
    print(calculate(-1, 2))

def test_calculation(calculate):
        print(calculate(1, 2))

def test_calculation(calculate):
    print(calculate('a', 2))

def test_calculation(calculate):
        print(calculate(1, 'b'))

@pytest.mark.development
@pytest.mark.parametrize('first_value, second_value, result', [
    (1,2,3)
])
def test_calculation(first_value, second_value, result, calculate):
    assert calculate(first_value,second_value) == result