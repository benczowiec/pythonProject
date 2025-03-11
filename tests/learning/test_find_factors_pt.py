from learning.find_factors import AlgorithmCalculator
import pytest

class TestAlgorithmCalculator:

    @pytest.fixture
    def entry_list(self):
        print("ENTRY LIST SETUP \n")
        return [1, 2, 3, 3, 4, 5, 6, 7, 8, 9, 10, 11]

    @pytest.fixture
    def algorithm(self, entry_list):
        print("BEFORE YIELD \n")
        algorithm = AlgorithmCalculator(entry_list)
        yield algorithm
        print("AFTER YIELD \n")
        algorithm.clean_up()

    def test_find_pair_of_factors(self, algorithm):
        print("TEST \n")
        assert algorithm.find_pair_of_factors(6) == [(3, 3), (4, 2), (5, 1)]

