# Реализуйте декоратор do_twice, вызывающий декорируемую функцию два раза.
# Примечание 1. Не забывайте про то, что декоратор не должен поглощать возвращаемое значение декорируемой функции, а также должен уметь декорировать функции с произвольным количеством позиционных и именованных аргументов.
# Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимый декоратор do_twice, но не код, вызывающий его. 

def do_twice(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        func(*args, **kwargs)
        return result

    return wrapper