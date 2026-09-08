import pytest
from src.gradebook import validate_name


def test_valid_name():
    assert validate_name("yougesh kumar") is True


def test_empty_name():
    with pytest.raises(ValueError):
        validate_name("")


def test_over_length_name():
    name = "A" * 51

    with pytest.raises(ValueError):
        validate_name(name)


def test_name_with_digits():
    with pytest.raises(ValueError):
        validate_name("yougesh123")


def test_name_with_symbols():
    with pytest.raises(ValueError):
        validate_name("yougesh@kumar")