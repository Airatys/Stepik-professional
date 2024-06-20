# Дано логическое выражение, состоящее из переменных, а также операторов |, &, and или or. Напишите программу, которая разбивает данную строку по указанным операторам.
# Формат входных данных
# На вход программе подается строка, содержащая логическое выражение, которое состоит из переменных и операторов |, &, and или or, между которыми могут располагаться пробелы.
# Формат  выходных данных
# Программа должна разбить введенную строку по указанным логическим операторам, захватывая вокруг стоящие пробелы, и вывести все значения, полученные при разбиении, через запятую и пробел.

import re

text = input()
regex = re.split(r'\s*(?:[|&]|and|or)\s*', text)
print(*regex, sep=', ')