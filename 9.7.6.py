# Реализуйте декоратор takes_positive, который проверяет, что все аргументы, передаваемые в декорируемую функцию, являются положительными целыми числами.
# Если хотя бы один аргумент не удовлетворяет данному условию, декоратор должен возбуждать исключение:
#     TypeError, если аргумент не является целым числом
#     ValueError, если аргумент является целым числом, но отрицательным или равным нулю
# Примечание 1. Приоритет возбуждения исключений при несоответствии аргумента обоим условиям или при наличии разных аргументов, несоответствующих разным условиям: TypeError, затем ValueError.
# Примечание 2. Не забывайте про то, что декоратор не должен поглощать возвращаемое значение декорируемой функции, а также должен уметь декорировать функции с произвольным количеством позиционных и именованных аргументов.
# Примечание 3. В тестирующую систему сдайте программу, содержащую только необходимый декоратор takes_positive, но не код, вызывающий его.

def takes_positive(func):
    def wrapper(*args, **kwargs):
        try:
            for i in args:
                if i <= 0 and isinstance(i, int):
                    raise ValueError
                if i < 0 or not isinstance(i, int):
                    raise TypeError
            for i in kwargs.values():
                if i < 0 and not isinstance(i, int):
                    raise TypeError
                if i <= 0 and isinstance(i, int):
                    raise ValueError
            return func(*args, **kwargs)
        except TypeError:
            raise
        except ValueError:
            raise
    return wrapper