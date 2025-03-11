import unittest
import learning.find_factors as ff


class TestMain(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.expected = [(3, 3), (4, 2), (5, 1)]

    # def setUp(self):
    #     self.expected = [(3, 3), (4, 2), (5, 1)]

    def test_find_pair_of_factors(self):
        result = ff.find_pair_of_factors(6, [1, 2, 3, 3, 4, 5, 6, 7, 8, 9, 10, 11])
        self.assertCountEqual(result, self.expected)
        self.assertListEqual(result, self.expected)


if __name__ == '__main__':
    unittest.main()
