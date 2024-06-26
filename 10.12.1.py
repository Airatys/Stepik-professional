# Напишите программу, которая выводит все перестановки символов строки без дубликатов.
# Формат входных данных
# На вход программе подается произвольная строка из строчных латинских букв, длина которой не превышает 1010 символов.
# Формат выходных данных
# Программа должна вывести все перестановки символов данной строки без дубликатов в алфавитном порядке, каждую на отдельной строке.

import itertools as it

n = input()
for i, _ in it.groupby(sorted(set(it.permutations(n)))):
    print(*i, sep='')