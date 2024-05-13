# Реализуйте класс BoundedRepeater, порождающий итераторы, конструктор которого принимает два аргумента в следующем порядке:
#     obj — произвольный объект
#     times — натуральное число
# Итератор класса BoundedRepeater должен генерировать значение obj times раз, а затем возбуждать исключение StopIteration.
# Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимый класс BoundedRepeater.

class BoundedRepeater:
    def __init__(self, obj, times):
        self.obj = obj 
        self.times = times
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index > self.times:
            raise StopIteration
        return self.obj
    
