import pytest
from solution import Solution


class TestSolution:

    @pytest.fixture
    def failing_test_one(self):
        return [[1, 2, 3], 2, 2]

    @pytest.fixture
    def passing_test_one(self):
        return [[6, 1, 4, 6, 3, 2, 7, 4], 3, 2]

    def test__too_short_array_fails(self, failing_test_one):
        assert Solution(*failing_test_one).solution() == -1

    def test_total(self, passing_test_one):
        sol = Solution(*passing_test_one)
        assert sol._total(3) == {
            (0, 3): 11,
            (1, 4): 11,
            (2, 5): 13,
            (3, 6): 11,
            (4, 7): 12,
            (5, 8): 13
        }
        assert sol._total(2) == {
            (0, 2): 7,
            (1, 3): 5,
            (2, 4): 10,
            (3, 5): 9,
            (4, 6): 5,
            (5, 7): 9,
            (6, 8): 11
        }

    def test_potential_solutions(self, passing_test_one):
        expected = sorted([
            20, 16, 20, 22,
            16, 20, 22,
            20, 22, 24,
            18, 16, 22,
            19, 17, 22,
            20, 18, 23, 22
        ], reverse=True)
        assert expected == Solution(*passing_test_one)._potential_solutions()

    def test_intersects(self, passing_test_one):
        sol = Solution(*passing_test_one)
        assert False is sol._intersects((0, 3), (3, 5))
        assert True is sol._intersects((0, 3), (0, 2))
        assert True is sol._intersects((0, 3), (2, 4))
        assert True is sol._intersects((3, 5), (2, 4))
        assert True is sol._intersects((3, 5), (4, 6))


        ]
