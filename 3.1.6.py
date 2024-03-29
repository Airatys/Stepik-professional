# Реализуйте функцию get_date_range(), которая принимает два аргумента в следующем порядке:
#     start — начальная дата, тип date
#     end — конечная дата, тип date
# Функция get_date_range() должна возвращать список, состоящий из дат (тип date) от start до end включительно.
# Если start > end, функция должна вернуть пустой список.
# Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимую функцию get_date_range(), но не код, вызывающий ее.

from datetime import date
def get_date_range(start, end):
    if start > end:
        return []
    else:
        return [date.fromordinal(i) for i in range(start.toordinal(), end.toordinal()+1)]
    




