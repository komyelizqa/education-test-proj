from pytest import fixture

@fixture
def ultimate_answer():
    return 42


def test_get_answer(ultimate_answer):
    assert 42 ==ultimate_answer