import unittest
from playground import test_function

list_1 = [5, 8, 2, 7, 8, 8, 2, 4]
n_1 = 8
n_2 = 10


class TestMethods(unittest.TestCase):

    def test_in(self):
        self.assertEqual(test_function(list_1, n_1), [1, 4, 5])

    def test_not_in(self):
        self.assertEqual(test_function(list_1, n_2), "Отсутствует")


if __name__ == '__main__':
    unittest.main()
