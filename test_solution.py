import pytest
from solution import Solution


@pytest.fixture
def failing_test_one():
    return [[1, 2, 3], 2, 2]


class TestSolution:
    def test__too_short_array_fails(self, failing_test_one):
        assert Solution(*failing_test_one).solution() == -1
