# Реализуйте функцию count_occurences(), которая принимает два аргумента в следующем порядке:
#     word — слово
#     words — последовательность слов, разделенных пробелом
# Функция должна определять, сколько раз слово word встречается в последовательности words, и возвращать полученный результат.
# Примечание 1. Функция должна игнорировать регистр. То есть, например, слова Python и python считаются одинаковыми.
# Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимую функцию count_occurences(), но не код, вызывающий ее.

from collections import Counter 

def count_occurences(word, words):
    dat = Counter(words.lower().split(' '))
    return dat[word.lower()]
    