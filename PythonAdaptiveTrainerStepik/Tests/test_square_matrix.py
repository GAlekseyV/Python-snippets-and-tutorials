import unittest
from square_matrix import mut_matrix

square_matrix = [[9, 5, 3], [0, 7, -1], [-5, 2, 9]]
one_number = [[1]]
column = [[1], [1], [1], [1]]
row = [[1, 1, 1, 1, 1]]

square_matrix_out = [[3, 21, 22], [10, 6, 19], [20, 16, -1]]
one_number_out = [[4]]
column_out = [[4], [4], [4], [4]]
row_out = [[4, 4, 4, 4, 4]]


class TestMethods(unittest.TestCase):

    def test_square(self):
        self.assertEqual(mut_matrix(square_matrix), square_matrix_out)

    def test_one(self):
        self.assertEqual(mut_matrix(one_number), one_number_out)

    def test_column(self):
        self.assertEqual(mut_matrix(column), column_out)

    def test_row(self):
        self.assertEqual(mut_matrix(row), row_out)


if __name__ == '__main__':
    unittest.main()
