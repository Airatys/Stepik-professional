# Как известно, во время итерации по словарю мы получаем ключи, а не значения или пары ключ-значение.
# Приведенный ниже код:
# info = {'name': 'Timur', 'age': 29, 'gender': 'Male'}
# print(*info)
# выводит:
# name age gender
# Реализуйте класс DictItemsIterator, порождающий итераторы, конструктор которого принимает один аргумент:
#     data — словарь
# Итератор класса DictItemsIterator должен генерировать последовательность кортежей, представляющих собой пары ключ-значение словаря data, а затем возбуждать исключение StopIteration.
# Примечание 1. При решении задачи не используйте словарные методы keys(), values() и items().
# Примечание 2. Пары ключ-значение в возвращаемом функцией итераторе должны располагаться в своем изначальном порядке.
# Примечание 3. В тестирующую систему сдайте программу, содержащую только необходимый класс DictItemsIterator.

class DictItemsIterator:
    
    def __init__(self, data):
        self.data = data
        self.index = -1
        
    def __iter__(self):
        return self
    
    def __next__(self):
        self.index += 1
        dict_keys = [*self.data]
        if self.index >= len(dict_keys):
            raise StopIteration
        return dict_keys[self.index], self.data[dict_keys[self.index]]
    
# Можно было применить другое решение, сразу получить итератор из ключей словаря, а дальше получать с помощью next() и уже формировать кортеж

class DictItemsIterator:
    
    def __init__(self, data):
        self.data = data
        self.dict_keys = iter(self.data)
        
    def __iter__(self):
        return self
    
    def __next__(self):
        key = next(self.dict_keys)
        return key, self.data[key]
        
        
        
        