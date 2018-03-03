import pytest


# -----------------------------------------------------------------------------
def test_dummy_ok():
    assert 1 == 1


# -----------------------------------------------------------------------------
def test_dummy_fails():
    example_dict = {}
    with pytest.raises(KeyError):
        print(example_dict['blub'])
