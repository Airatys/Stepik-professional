# Реализуйте класс Square, порождающий итераторы, конструктор которого принимает один аргумент:
#     n — натуральное число,
# Итератор класса Square должен генерировать последовательность из n чисел, каждое из которых является квадратом очередного натурального числа, а затем возбуждать исключение StopIteration.
# Примечание 1. Последовательность квадратов натуральных чисел начинается с квадрата числа 11.
# Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимый класс Square.

class Square:
    def __init__(self, n):
        self.n = n
        self.count = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.count >= self.n:
            raise StopIteration
        self.count += 1
        return self.count**2



        