# Во время визита очередного гостя сотрудникам отеля приходится проверять, доступна ли та или иная дата для бронирования номера.
# Реализуйте функцию is_available_date(), которая принимает два аргумента в следующем порядке:
#     booked_dates — список строковых дат, недоступных для бронирования. Элементом списка является либо одиночная дата, либо период (две даты через дефис). Например:
#     ['04.11.2021', '05.11.2021-09.11.2021']
#     date_for_booking — одиночная строковая дата или период (две даты через дефис), на которую гость желает забронировать номер. Например:
#     '01.11.2021' или '01.11.2021-04.11.2021'
# Функция is_available_date() должна возвращать True, если дата или период date_for_booking полностью доступна для бронирования. В противном случае функция должна возвращать False.
# Примечание 1. Гарантируется, что в периоде левая дата всегда меньше правой.
# Примечание 2. В периоде (две даты через дефис) граничные даты включены.
# Примечание 3. В тестирующую систему сдайте программу, содержащую только необходимую функцию is_available_date(), но не код, вызывающий ее.

from datetime import *
def is_available_date(booked_dates, date_for_booking):
    myset1 = set()
    for i in booked_dates:
        if len(i) == 10:
            a, b, c = list(map(int, i.split('.')))
            myset1.add(date(c, b, a).toordinal())
        elif len(i) > 10:
            list1, list2 = i.split('-')
            a1, b1, c1 = list(map(int, list1.split('.')))
            a2, b2, c2 = list(map(int, list2.split('.')))
            for d in range(date(c1, b1, a1).toordinal(), date(c2, b2, a2).toordinal()+1):
                myset1.add(d)
            
    myset2 = set()    
    if len(date_for_booking) == 10:
        a, b, c = list(map(int, date_for_booking.split('.')))
        myset2.add(date(c, b, a).toordinal())
    elif len(date_for_booking) > 10:
        list1, list2 = date_for_booking.split('-')
        a1, b1, c1 = list(map(int, list1.split('.')))
        a2, b2, c2 = list(map(int, list2.split('.')))
        for i in range(date(c1, b1, a1).toordinal(), date(c2, b2, a2).toordinal()+1):
            myset2.add(i)
            
    return True if myset1.isdisjoint(myset2) else False




