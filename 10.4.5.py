# Реализуйте класс PowerOf, порождающий итераторы, конструктор которого принимает один аргумент:
#     number — ненулевое число
# Итератор класса PowerOf должен генерировать бесконечную последовательность целых неотрицательных степеней числа number в порядке возрастания, начиная с нулевой степени.
# Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимый класс PowerOf.

class PowerOf:

    def __init__(self, number) -> None:
        self.number = number
        self.count = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        volum = self.number** self.count
        self.count += 1 
        return volum