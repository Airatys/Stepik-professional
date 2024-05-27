# Реализуйте функцию first_true(), которая принимает два аргумента в следующем порядке:
#     iterable — итерируемый объект
#     predicate — функция-предикат; если имеет значение None, то работает аналогично функции bool()
# Функция first_true() должна возвращать первый по счету элемент итерируемого объекта iterable, для которого функция predicate вернула значение True.
# Если такого элемента нет, функция first_true() должна вернуть значение None.
# Примечание 1. Предикат — это функция, которая возвращает True или False в зависимости от переданного в качестве аргумента значения.
# Примечание 2. Гарантируется, что итерируемый объект, передаваемый в функцию, не является множеством.
# Примечание 3. В тестирующую систему сдайте программу, содержащую только необходимую функцию first_true(), но не код, вызывающий ее.

import itertools as it 

def first_true(iterable, predicate=None):
    for i in it.islice(filter(predicate, iterable), 1):
        return i