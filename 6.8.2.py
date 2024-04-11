# Дана последовательность слов. Напишите программу, которая выводит наименее часто встречаемое слово в этой последовательности.
# Если таких слов несколько, программа должна вывести их все.
# Формат входных данных
# На вход программе подается последовательность слов, разделенных пробелом.
# Формат выходных данных
# Программа должна определить наименее часто встречаемое слово в введенной последовательности и вывести его в нижнем регистре.
# Если таких слов несколько, программа должна вывести их все в лексикографическом порядке, в нижнем регистре, разделяя запятой и пробелом.
# Примечание 1. Программа должна игнорировать регистр. То есть, например, слова Python и python считаются одинаковыми.

from collections import Counter

text = Counter(input().lower().split())
text.__dict__['min_value'] = lambda: min(text.items(), key=lambda x: (x[1], x[0]))
dat = sorted(list(filter(lambda x: x[1] == text.min_value()[1], text.items())))
print(*[i[0] for i in dat], sep=', ')
     