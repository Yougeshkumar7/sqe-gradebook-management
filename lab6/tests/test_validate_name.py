import pytest

from gradebook import validate_name


@pytest.mark.parametrize("length, expected_valid", [
    (0, False),
    (1, True),
    (49, True),
    (50, True),
    (51, False),
])
def test_validate_name_length_boundaries(length, expected_valid):

    name = "A" * length

    if expected_valid:
        assert validate_name(name) is True
    else:
        with pytest.raises(ValueError):
            validate_name(name)