# Реализуйте функцию ncycles(), которая принимает два аргумента в следующем порядке:
#     iterable — итерируемый объект
#     times — натуральное число
# Функция должна возвращать итератор, генерирующий последовательность элементов итерируемого объекта iterable, зацикленных times раз.
# Примечание 1. Элементы итерируемого объекта в возвращаемом функцией итераторе должны располагаться в своем исходном порядке.
# Примечание 2. Гарантируется, что итерируемый объект, передаваемый в функцию, не является множеством.
# Примечание 3. В тестирующую систему сдайте программу, содержащую только необходимую функцию ncycles(), но не код, вызывающий ее.

import itertools as it 

def ncycles(iterable, times):
    return (j for i in it.tee(iterable, times) for j in i)
         