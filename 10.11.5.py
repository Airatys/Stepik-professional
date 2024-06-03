# Анаграммы — это слова, которые состоят из одинаковых букв. Например:
#     адаптер — петарда
#     адресочек — середочка
#     азбука — базука
#     аистенок — осетинка
# Реализуйте функцию group_anagrams(), которая принимает один аргумент:
#     words — список слов
# Функция должна группировать в кортежи слова из списка words, являющиеся анаграммами, и возвращать список полученных кортежей.
# Примечание 1. Порядок кортежей в возвращаемом функцией списке, а также порядок элементов в этих кортежах, не важен.
# Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимую функцию group_anagrams(), но не код, вызывающий ее.

import itertools as it

def group_anagrams(words):
    sort_group = sorted(words, key=sorted)
    groups = it.groupby(sort_group, key=sorted)
    for _, j in groups:
        yield tuple(j)