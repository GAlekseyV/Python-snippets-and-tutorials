# Напишите программу, на вход которой подаётся прямоугольная матрица в виде последовательности строк,
# заканчивающихся строкой, содержащей только строку "end" (без кавычек). Программа должна вывести
# матрицу того же размера, у которой каждый элемент в позиции i, j равен сумме элементов первой
# матрицы на позициях (i-1, j), (i+1, j), (i, j-1), (i, j+1). У крайних символов соседний элемент
# находится с противоположной стороны матрицы. В случае одной строки/столбца элемент сам себе является
# соседом по соответствующему направлению.
# Sample Input 1:
# 9 5 3
# 0 7 -1
# -5 2 9
# end
# Sample Output 1:
# 3 21 22
# 10 6 19
# 20 16 -1
# Sample Input 2:
# 1
# end
# Sample Output 2:
# 4


def mut_matrix(matrix=[[]]):
    res_matrix = []
    rows = len(matrix)
    cols = len(matrix[0])
    for i in range(rows):
        row = []
        for j in range(cols):
            s = 0
            s += (matrix[(i - 1) % rows][j])
            s += (matrix[(i + 1) % rows][j])
            s += (matrix[i][(j - 1) % cols])
            s += (matrix[i][(j + 1) % cols])
            row.append(s)
        res_matrix.append(row)
    return res_matrix


# test_data_in_1 = [[9, 5, 3], [0, 7, -1], [-5, 2, 9]]
# test_data_in_2 = [[1]]
# test_data_out_1 = [[3, 21, 22], [10, 6, 19], [20, 16, -1]]
# test_data_out_2 = [[4]]
#
# print(mut_matrix(test_data_in_1))
# print(mut_matrix(test_data_in_2))
