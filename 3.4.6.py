# Реализуйте функцию num_of_sundays(), которая принимает на вход один аргумент:
#     year — натуральное число, год
# Функция должна возвращать количество воскресений в году year.
# Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимую функцию num_of_sundays(), но не код, вызывающий ее.

from datetime import date, timedelta,datetime

def num_of_sundays(year):
    """Функция принимает год ,
     и возвращает кол-во ворскресений в году"""
    d = datetime(year, 1, 1)
    counter = 0
    if year%100 ==0 and year%400==0:
        for j in range(366):
            d += timedelta(days=1)
            if d.weekday() == 6:
                counter += 1
    elif year%4!=0:
        for i in range(364):
            d+=timedelta(days=1)
            if d.weekday()== 6:
                counter+=1
    else:
        for k in range(366):
            d+=timedelta(days=1)
            if d.weekday()== 6:
                counter+=1
    return counter
   
    
    




