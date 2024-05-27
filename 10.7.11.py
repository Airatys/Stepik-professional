# Реализуйте генераторную функцию, которая принимает один аргумент:
#     iterable — итерируемый объект
# Функция должна возвращать генератор, порождающий последовательность кортежей, каждый из которых содержит очередной элемент итерируемого объекта iterable, а также следующий за ним элемент:
# (<очередной элемент>, <следующий элемент>)
# Для последнего элемента следующим считается значение None.
# Примечание 1. Элементы итерируемого объекта в возвращаемом функцией генераторе должны располагаться в своем исходном порядке.
# Примечание 2. Гарантируется, что итерируемый объект, передаваемый в функцию, не является множеством.
# Примечание 3. В тестирующую систему сдайте программу, содержащую только необходимую функцию pairwise(), но не код, вызывающий ее.

def pairwise(iterable):
    if not iterable:
        return []
    iterator = iter(iterable)
    f1 = next(iterator)
    while not f1 is None:
        try:
            f2 = next(iterator, None)
            yield (f1, f2)
            f1 = f2
        except:
            pass