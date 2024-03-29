# Реализуйте функцию saturdays_between_two_dates(), которая принимает два аргумента в следующем порядке:
#     start — начальная дата, тип date
#     end — конечная дата, тип date
# Функция должна возвращать количество суббот между датами start и end включительно.
# Примечание 1. Даты могут передаваться в любом порядке, то есть не гарантируется, что первая дата меньше второй.
# Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимую функцию saturdays_between_two_dates(), но не код, вызывающий ее.

from datetime import date
def saturdays_between_two_dates(start, end):
    if start < end:
        return len([i for i in range(start.toordinal(), end.toordinal()+1) if date.fromordinal(i).isoweekday()==6])
    else:
        return len([i for i in range(end.toordinal(), start.toordinal()+1) if date.fromordinal(i).isoweekday()==6])
    




