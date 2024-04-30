# Реализуйте функцию polynom(), которая принимает один аргумент:
#     x — вещественное число
# Функция должна возвращать значение выражения x2+1.
# Также функция должна иметь атрибут values, представляющий собой множество (тип set) всех значений функции, которые уже были вычислены.
# Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимую функцию polynom(), но не код, вызывающий ее. 

def polynom(x):
    res = x**2 + 1
    polynom.__dict__.setdefault('values', set()).add(res)
    return res



