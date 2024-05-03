# Реализуйте функцию sort_priority(), которая принимает два аргумента в следующем порядке:
#     values — список чисел
#     group — список, кортеж или множество чисел
# Функция должна сортировать по неубыванию список чисел values, делая при этом приоритетной группу чисел из group, которая должна следовать первой.
# Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимую функцию sort_priority(), но не код, вызывающий ее.

def sort_priority(values, group):
    values.sort()
    for i in sorted(group, reverse=True):
        if i in values:
            del values[values.index(i)]
            values.insert(0, i)