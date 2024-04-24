# Реализуйте функцию to_binary() с использованием рекурсии, которая принимает один аргумент:
#     number — неотрицательное целое число
# Функция должна возвращать строковое представление числа number в двоичной системе счисления.

def to_binary(number):
    if number == 1:
        return 1
    elif number == 0:
        return 0
    return str(to_binary(number // 2)) + str(number % 2)
    