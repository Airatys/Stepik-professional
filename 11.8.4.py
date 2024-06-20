# Напишите программу, которая меняет местами первые две буквы в каждом слове, состоящем из двух или более букв.
# Формат входных данных
# На вход программе подается строка, содержащая слова.
# Формат выходных данных
# Программа должна в введенной строке заменить первые две буквы в каждом слове, состоящем из двух или более букв, и вывести полученный результат.
# Примечание 1. Словом будем считать последовательность символов, соответствующих \w, окруженную символами, соответствующими \W.

import re

text = input()
res = re.sub(r'\b(\w)(\w)', r'\2\1', text)
print(res)