# Реализуйте recursive_sum() с использованием рекурсии, которая принимает один аргумент:
#     nested_lists — список, элементами которого являются целые числа или списки, элементами которых, в свою очередь, также являются либо целые числа, либо списки; вложенность может быть произвольной
# Функция должна вычислять сумму всех чисел во всех списках и возвращать полученный результат. Если список nested_lists пуст, функция должна вернуть число 00.
# Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимую функцию recursive_sum(), но не код, вызывающий ее.

counter = 0
def recursive_sum(nested_lists):
    global counter
    if  nested_lists == []:
        return 0
    if type(nested_lists) == int:
        counter += nested_lists
    if type(nested_lists) == list:
        for i in nested_lists:
           recursive_sum(i)
    return counter
