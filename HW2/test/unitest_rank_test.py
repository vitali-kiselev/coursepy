import unittest

from ..test import Rank

class RankTest(unittest.TestCase):
    def test_rank(self):
        lst = int(input())
        test_var = ([165, 163, 160, 160, 157, 157, 155, 154], lst)
        test_result = test_var[lst]

        self.assertEqual(test_result, Rank.MyClass.rank(test_var))


