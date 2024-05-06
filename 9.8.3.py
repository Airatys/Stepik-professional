# Реализуйте декоратор trace, который выводит отладочную информацию о декорируемой функции во время ее выполнения, а именно: имя функции, переданные аргументы и возвращаемое значение в следующем формате:
# TRACE: вызов <имя функции>() с аргументами: <кортеж позиционных аргументов>, <словарь именованных аргументов>
# TRACE: возвращаемое значение <имя функции>(): <возвращаемое значение>
# Также декоратор должен сохранять имя и строку документации декорируемой функции.
# Примечание 1. Не забывайте про то, что декоратор не должен поглощать возвращаемое значение декорируемой функции, а также должен уметь декорировать функции с произвольным количеством позиционных и именованных аргументов.
# Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимый декоратор trace, но не код, вызывающий его.

import functools 

def trace(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f'TRACE: вызов {func.__name__}() с аргументами: {args}, {kwargs}')
        print(f'TRACE: возвращаемое значение {func.__name__}(): {repr(func(*args, **kwargs))}')
        return func(*args,**kwargs)
    return wrapper
  
