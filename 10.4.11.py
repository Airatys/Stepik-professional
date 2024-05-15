# Реализуйте класс Xrange, порождающий итераторы, конструктор которого принимает три аргумента в следующем порядке:
#     start — целое или вещественное число
#     end — целое или вещественное число
#     step — целое или вещественное число, по умолчанию имеет значение 11
# Итератор класса Xrange должен генерировать последовательность членов арифметической прогрессии от start до end, включая start и не включая end, с шагом step, а затем возбуждать исключение StopIteration.
# Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимый класс Xrange.

class Xrange:
    def __init__(self, start, end, step=1):
        self.start = start - step
        self.end = end
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        self.start += self.step
        if self.start * self.step >= self.end * self.step:
            raise StopIteration
        return self.start