# Реализуйте класс Alphabet, порождающий итераторы, конструктор которого принимает один аргумент:
#     language — код языка: ru — русский, en — английский
# Итератор класса Alphabet() должен циклично генерировать последовательность строчных букв:
#     русского алфавита, если language имеет значение ru
#     английского алфавита, если language имеет значение en
# Примечание 1. Буква ё в русском алфавите не учитывается.
# Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимый класс Alphabet.

class Alphabet:
    
    def __init__(self, language):
        self.en_ru = {'en': 'abcdefghijklmnopqrstuvwxyz', 'ru': 'абвгдежзийклмнопрстуфхцчшщъыьэюя'}[language]
        self.index = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index == len(self.en_ru):
            self.index = 0
        value = self.en_ru[self.index]
        self.index += 1
        return value

        