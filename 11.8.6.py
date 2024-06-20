# Напишите программу, которая заменяет все повторяющиеся рядом стоящие слова на одно слово.
# Формат входных данных
# На вход программе подается строка, содержащая слова.
# Формат выходных данных
# Программа должна в введенной строке заменить все повторяющиеся рядом стоящие слова на одно слово и вывести полученный результат.
# Примечание 1. Программа должна быть чувствительной к регистру, то есть, например, слова python и Python считаются различными.
# Примечание 2. Словом будем считать последовательность символов, соответствующих \w, окруженную символами, соответствующими \W.

import re

print(re.sub(r'(\b\w+\b)(\W+\1\b)+',r'\1',input()))