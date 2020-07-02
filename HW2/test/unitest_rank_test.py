import unittest

from ..test import Rank

class RankTest(unittest.TestCase):
    def test_rank(self):
        n = int(input())
        test_var = ([165, 163, 160, 160, 157, 157, 155, 154], n)
        test_result = test_var[n]

        self.assertEqual(test_result, Rank.MyClass.rank(test_var))


