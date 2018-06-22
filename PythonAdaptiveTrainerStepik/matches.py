# Напишите программу, которая принимает на стандартный вход список игр футбольных команд
# с результатом матча и выводит на стандартный вывод сводную таблицу результатов всех матчей.
# За победу команде начисляется 3 очка, за поражение — 0, за ничью — 1.
# Формат ввода следующий:
# В первой строке указано целое число n
# — количество завершенных игр.
# После этого идет n строк, в которых записаны результаты игры в следующем формате:
# Первая_команда;Забито_первой_командой;Вторая_команда;Забито_второй_командой
# Вывод программы необходимо оформить следующим образом:
# Команда:Всего_игр Побед Ничьих Поражений Всего_очков
#
# Конкретный пример ввода-вывода приведён ниже. Порядок вывода команд произвольный.
# Sample Input:
# 3
# Зенит;3;Спартак;1
# Спартак;1;ЦСКА;1
# ЦСКА;0;Зенит;2
#
# Sample Output:
# Зенит:2 2 0 0 6
# ЦСКА:2 0 1 1 1
# Спартак:2 0 1 1 1

n = int(input())
# Словарь команд {team_name: [games, wins, draws, lose, points]}
table = {}
games = 0
wins = 1
draws = 2
loses = 3
points = 4

while n > 0:
    team_1, goals_1, team_2, goals_2 = input().split(";")
    if team_1 not in table:
        table[team_1] = [0, 0, 0, 0, 0]
    if team_2 not in table:
        table[team_2] = [0, 0, 0, 0, 0]
    table[team_1][games] += 1
    table[team_2][games] += 1
    if goals_1 > goals_2:
        table[team_1][wins] += 1
        table[team_1][points] += 3
        table[team_2][loses] += 1
    elif goals_2 > goals_1:
        table[team_2][wins] += 1
        table[team_2][points] += 3
        table[team_1][loses] += 1
    else:
        table[team_1][draws] += 1
        table[team_1][points] += 1
        table[team_2][draws] += 1
        table[team_2][points] += 1
    n -= 1

for team, values in table.items():
    print(team, end=":")
    [print(i, end=' ') for i in values]
    print()
