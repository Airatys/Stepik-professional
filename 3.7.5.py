# Напишите программу, которая определяет количество дней в заданном месяце.
# Формат входных данных
# На вход программе подаются год и полное название месяца на английском, разделенные пробелом.
# Формат выходных данных
# Программа должна вывести единственное число — количество дней в введенном месяце.

import calendar

mon = list(calendar.month_name)
mylist = mon[1:]
mydict = {}
y, m = [int(i) if i.isdigit() else i for i in input().split()]
for k, v in enumerate(mylist):
    mydict[v] = k+1
print(calendar.monthrange(y, mydict[m])[1])


