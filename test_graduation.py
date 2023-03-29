import pytest

from graduation_eligibility import Graduation


@pytest.fixture
def test_cases():
    test_cases_mapping = {
        5: "14/29",
        10: "372/773"
    }
    return test_cases_mapping


def test_function(test_cases):
    for test_case in test_cases:
        graduation = Graduation(test_case)
        assert graduation.calculate() == test_cases[test_case]
