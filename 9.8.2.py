# Реализуйте декоратор returns_string, который проверяет, что возвращаемое значение декорируемой функции принадлежит типу str.
# Если возвращаемое значение принадлежит какому-либо другому типу, декоратор должен возбуждать исключение TypeError.
# Также декоратор должен сохранять имя и строку документации декорируемой функции.
# Примечание 1. Не забывайте про то, что декоратор не должен поглощать возвращаемое значение декорируемой функции, а также должен уметь декорировать функции с произвольным количеством позиционных и именованных аргументов.
# Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимый декоратор returns_string, но не код, вызывающий его.

import functools
def returns_string(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        values = func(*args, **kwargs)
        if not isinstance(values, str):
            raise TypeError
        else:
            return values       
    return wrapper    
