import unittest
from src.lottery import lottery

class TestLotteryFunction(unittest.TestCase):
    def test_lottery(self):
        a = [1, 1, 3, 2, 2, 2, 4, 5]
        self.assertEqual(lottery(a, 2), [1])
    def test_lottery_v2(self):
        a = [1, 1, 3, 2, 2, 2, 4, 5]
        self.assertEqual(lottery(a, 3), [2])
    def test_lottery_v3(self):
        a = [1, 1, 3, 2, 2, 2, 4, 5]
        self.assertEqual(lottery([], 1), [])
    def test_lottery_v4(self):
        b = [1, 1, 2, 2, 3, 3, 4, 4]
        self.assertEqual(lottery(b, 2), [1, 2, 3, 4])
    def test_lottery_v5(self):
        c = [5, 3, 2, 1, 7]
        self.assertEqual(lottery(c, 1), [5, 3, 2, 1, 7])

if __name__ == '__main__':
    unittest.main()
