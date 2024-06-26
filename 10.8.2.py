# Реализуйте функцию factorials() с использованием функции accumulate(), которая принимает один аргумент:
#     n — натуральное число
# Функция должна возвращать итератор, генерирующий последовательность из n чисел, каждое из которых является факториалом очередного натурального числа.
# Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимую функцию factorials(), но не код, вызывающий ее.

from itertools import accumulate

def factorials(n: int):
    yield from accumulate(range(1, n + 1), lambda x, y: x * y)
