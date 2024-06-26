# Напишите программу, которая принимает на вход дату и выводит предыдущую и следующую даты.
# Формат входных данных
# На вход программе подается дата в формате DD.MM.YYYY.
# Формат выходных данных
# Программа должна вывести предыдущую и следующую даты относительно введенной даты, каждую на отдельной строке, в формате DD.MM.YYYY.
# Примечание 1. Гарантируется, что у подаваемой даты есть предыдущая и следующая даты.

from datetime import *
a, b, c = list(map(int, input().split('.')))

d1 = date(c, b, a) - timedelta(days=1)
d2 = date(c, b, a) + timedelta(days=1)
print(d1.strftime('%d.%m.%Y'))
print(d2.strftime('%d.%m.%Y'))