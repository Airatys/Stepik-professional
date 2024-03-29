# Реализуйте функцию get_the_fastest_func(), которая принимает два аргумента в следующем порядке:
#     funcs — список произвольных функций
#     arg — произвольный объект
# Функция get_the_fastest_func() должна возвращать функцию из списка funcs, которая затратила на вычисление значения при вызове с аргументом arg наименьшее количество времени.
# Примечание. В тестирующую систему сдайте программу, содержащую только необходимую функцию get_the_fastest_func(), но не код, вызывающий ее.

import time
def get_the_fastest_func(funcs, arg):
    mylist = []
    for func in funcs:
        start = time.monotonic()
        func(arg)
        end = time.monotonic()
        s_end = end - start
        mylist.append(s_end)
    i = mylist.index(min(mylist)) 
    return funcs[i]




