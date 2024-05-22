# Реализуйте генераторную функцию years_days(), которая принимает один аргумент:
#     year — натуральное число
# Функция должна возвращать генератор, порождающий последовательность всех дат (тип date) в году year.
# Примечание 1. Возьмем в качестве примера 20222022 год. В январе этого года 3131 день, в феврале — 2828, в марте — 3131, и так далее.
# Тогда генератор, полученный при вызове years_days(2022), должен порождать сначала все даты с 11 по 3131 января, затем с 11 по 2828 февраля, и так далее до 3131 декабря.
# Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимую функцию years_days(), но не код, вызывающий ее.

import calendar
from datetime import *
def years_days(year: int):
    if calendar.isleap(year):
        yield (date.fromordinal(i) for i in range(date(year, 1, 1).toordinal(), date(year, 1, 1).toordinal() + 366))
    else:
        yield (date.fromordinal(j) for j in range(date(year, 1, 1).toordinal(), date(year, 1, 1).toordinal() + 365))
    
# решение через timedelta

from datetime import date, timedelta
from calendar import isleap 

def years_days(year):
    d = 365 + isleap(year)
    yield from (date(year, 1, 1) + timedelta(days=i) for i in range(d))