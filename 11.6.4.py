# Напишите программу, определяющую:
#     количество строк, в которых bee встречается в качестве подстроки не менее двух раз
#     количество строк, в которых geek встречается в качестве слова хотя бы один раз
# Формат входных данных
# На вход программе произвольное количество строк, каждая из которых содержит набор произвольных символов.
# Формат выходных данных
# Программа должна вывести два числа:
#     первое — количество строк, в которых bee встречается в качестве подстроки не менее двух раз
#     второе — количество строк, в которых geek встречается в качестве слова хотя бы один раз
# каждое на отдельной строке.
# Примечание 1. Словом будем считать любую непрерывную последовательность из одного или нескольких символов, соответствующих \w.
# Примечание 2. Строка может одновременно удовлетворять обоим условиям.
# Примечание 3. В первой строке первого теста bee встречается в качестве подстроки 3 раза:
# beebee bee
# Во второй строке bee встречается в качестве подстроки лишь один раз, а слово geek отсутствует.
# В третьей строке bee встречается в качестве подстроки 22 раза, geek в качестве слова — 1 раз:
# bee geek bee

import sys
import re
counter_1 = counter_2 = 0
regex_1 = r'(bee).*\1'
regex_2 = r'(\bgeek\b)'
for i in sys.stdin:
    if re.search(regex_1, i.strip()):
        counter_1 += 1
    if re.search(regex_2, i.strip()):
        counter_2 += 1
print(counter_1, counter_2, sep='\n')
        
    
    

