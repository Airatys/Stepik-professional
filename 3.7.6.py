# Реализуйте функцию get_days_in_month(), которая принимает два аргумента в следующем порядке:
#     year — натуральное число
#     month — полное название месяца на английском
# Функция должна возвращать отсортированный по возрастанию список всех дат (тип date) месяца month и года year.
# Примечание 1. Например, вызов:
# get_days_in_month(2021, 'December')
# должен вернуть список:
# [datetime.date(2021, 12, 1), datetime.date(2021, 12, 2), ..., datetime.date(2021, 12, 30), datetime.date(2021, 12, 31)]
# Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимую функцию get_days_in_month(), но не код, вызывающий ее.

import calendar
from datetime import *

def get_days_in_month(year, month):
    mydict = {}
    callist = []
    mon = list(calendar.month_name)
    mylist = mon[1:]
    for k, v in enumerate(mylist):
        mydict[v] = k+1
    n = calendar.monthrange(year, mydict[month])[1]
    
    a = date(year, mydict[month], 1)
    for i in range(a.toordinal(), a.toordinal() + n):
        callist.append(date.fromordinal(i))
    return callist
    
    
    
    
    




