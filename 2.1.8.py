# Реализуйте функцию index_of_nearest(), которая принимает два аргумента в следующем порядке:
#     numbers — список целых чисел
#     number — целое число
# Функция должна находить в списке numbers ближайшее по значению число к числу number и возвращать его индекс.
# Если список numbers пуст, функция должна вернуть число −1−1.
# Примечание 1. Если в функцию передается список, содержащий несколько чисел, одновременно являющихся ближайшими к искомому числу, функция должна возвращать наименьший из индексов ближайших чисел.
# Примечание 2. Рассмотрим третий тест. Ближайшими числами к числу 44 являются 55 и 33, имеющие индексы 11 и 22 соответственно. Наименьший из индексов равен 11.
# Примечание 3. В тестирующую систему сдайте программу, содержащую только необходимую функцию index_of_nearest(), но не код, вызывающий ее.

def index_of_nearest(numbers, number):
    if not numbers:
        return -1
    elif len(numbers) > 0:
        n = min(numbers, key=lambda x: abs(x-number))
        return numbers.index(n)