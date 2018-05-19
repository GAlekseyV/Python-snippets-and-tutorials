# TODO Решить задачу не создавая матрицу выводить результат построчно, вычисляя значение в ячейке по её координатам.

n = int(input())
i = []
j = []
step = 0
matrix = [[0 for row in range(n)] for col in range(n)]

# Matrix elements indexes
for step in range(0, n // 2):
    [i.append(step) for y in range(step, n-step)]
    [j.append(y) for y in range(step, n - step)]

    [i.append(y) for y in range(step+1, n-step)]
    [j.append(n-1-step) for y in range(step+1, n-step)]

    [i.append(n-1-step) for y in range(step+1, n-step)]
    [j.append(n-y-1) for y in range(step+1, n-step)]

    [i.append(n-y-1) for y in range(step+1, n-1-step)]
    [j.append(step) for y in range(step+1, n-1-step)]

if n % 2:
    i.append(n // 2)
    j.append(n // 2)

for num in range(n*n):
    matrix[i[num]][j[num]] = num + 1

for row in range(n):
    for col in range(n):
        print(str(matrix[row][col]) + " ", end="")
    print()
