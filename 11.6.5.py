# В онлайн-школе BEEGEEK мы всегда следим за тем, насколько растет наша популярность. Для этого мы собираем публикации из различных соцсетей, которые содержат вхождения строки beegeek в нижнем регистре.
# Мы оцениваем публикацию:
#     в 3 балла, если она начинается и заканчивается строкой beegeek
#     в 2 балла, если она только начинается или только заканчивается строкой beegeek
#     в 1 балл, если она содержит строку beegeek только внутри
#     в 0 баллов, если она не содержит строку beegeek
# Напишите программу, которая определяет популярность онлайн-школы BEEGEEK путем суммирования баллов всех публикаций.
# Формат входных данных
# На вход программе подается произвольное число строк, каждая из которых представляет очередную публикацию.
# Формат выходных данных
# Программа должна определить, во сколько баллов оценивается каждая введенная публикация, и вывести сумму всех полученных баллов.
# Примечание 1. Если публикация представляет собой просто строку beegeek, то она оценивается в 2 балла.

import sys
import re

counter = 0
for i in map(str.rstrip, sys.stdin):
    if re.fullmatch(r'beegeek.*beegeek', i):
        counter += 3
    elif re.fullmatch(r'^beegeek.*|.*beegeek$', i):
        counter += 2
    elif re.fullmatch(r'.+beegeek.+', i):
        counter += 1
        
print(counter)