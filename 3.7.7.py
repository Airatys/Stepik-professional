# Реализуйте функцию get_all_mondays(), которая принимает один аргумент:
#     year — натуральное число
# Функция должна возвращать отсортированный по возрастанию список всех дат (тип date) года year, выпадающих на понедельник.
# Примечание 1. Например, вызов:
# get_all_mondays(2021)
# должен вернуть список:
# [datetime.date(2021, 1, 4), datetime.date(2021, 1, 11), ..., datetime.date(2021, 12, 20), datetime.date(2021, 12, 27)]
# Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимую функцию get_all_mondays(), но не код, вызывающий ее.

from datetime import*
import calendar
def get_all_mondays(year): 
    callist = []
    a = date(year, 1, 1)
    if calendar.isleap(year):
        for i in range(a.toordinal(), a.toordinal() + 366):
            if date.fromordinal(i).weekday() == 0:
                callist.append(date.fromordinal(i))
        return callist
    else:
        for i in range(a.toordinal(), a.toordinal() + 365):
            if date.fromordinal(i).weekday() == 0:
                callist.append(date.fromordinal(i))
        return callist
        
    
        
    




