# TODO Why do not work test? It do not start.
import unittest
from fraction_of_maximum_score import calc_part


scores_with_a = "FBAABCAD"
result_with_a = 0.375

scores_without_a = "BCB"
result_without_a = 0.00


class TestCalcMethod(unittest.TestCase):
    def test_with_a(self):
        self.assertEqual(calc_part(scores_with_a), result_with_a)

    def test_without_a(self):
        self.assertEqual(calc_part(scores_without_a), result_without_a)


if __name__ == '__main__':
    unittest.main()
