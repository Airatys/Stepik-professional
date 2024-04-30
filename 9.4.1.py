# Реализуйте функцию numbers_sum(), которая принимает один аргумент:
#     elems — список произвольных объектов
# Функция должна возвращать сумму чисел (типы int и float), находящихся в списке elems, игнорируя все нечисловые объекты.
# Если в списке elems нет чисел, функция должна вернуть число 00.
# Также функция должна иметь следующую строку документации:
# Принимает список и возвращает сумму его чисел (int, float),
# игнорируя нечисловые объекты. 0 - если в списке чисел нет.
# Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимую функцию numbers_sum(), но не код, вызывающий ее. 

def numbers_sum(elems):
    '''Принимает список и возвращает сумму его чисел (int, float),
игнорируя нечисловые объекты. 0 - если в списке чисел нет.'''
    return sum(filter(lambda x: isinstance(x, (int, float)), elems))
    
