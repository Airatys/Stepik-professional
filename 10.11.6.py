# Будем считать, что последовательность целых неотрицательных чисел можно преобразовать в отрезок, если разница между соседними элементами этой последовательности равна единице.
# Например, числа 3,4,5,6,7,83,4,5,6,7,8 можно преобразовать в отрезок [3;8][3;8]. Числа 1,3,5,11,15,221,3,5,11,15,22 в отрезок преобразовать нельзя.
# Одиночное число преобразуется в отрезок, в котором и правой, и левой границей является оно само. Например, число 11 можно преобразовать в отрезок [1;1][1;1].
# Реализуйте функцию ranges(), которая принимает один аргумент:
#     numbers — список различных натуральных чисел, расположенных в порядке возрастания
# Функция должна преобразовывать числа из списка numbers в отрезки, представляя их в виде кортежей, где первый элемент кортежа является левой границей отрезка, второй элемент — правой границей отрезка.
# Полученные кортежи-отрезки функция должна возвращать в виде списка.
# Примечание 1. Числа в возвращаемом функцией списке должны располагаться в своем исходном порядке.
# Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимую функцию ranges(), но не код, вызывающий ее.

import itertools as it
def ranges(numbers):
    mylist = []
    func = lambda x: numbers.index(x) - x
    group = it.groupby(numbers, func)
    for _, j in group:
        group = tuple(j)
        group = group[0], group[-1]
        mylist.append(group)
    return mylist