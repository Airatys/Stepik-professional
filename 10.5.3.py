# Реализуйте генераторную функцию primes(), которая принимает два аргумента в следующем порядке:
#     left — натуральное число
#     right — натуральное число
# Функция должна возвращать генератор, порождающий последовательность простых чисел от left до right включительно, а затем возбуждающий исключение StopIteration.
# Примечание 1. Гарантируется, что left <= right.
# Примечание 2. Простое число — натуральное число, имеющее ровно два различных натуральных делителя — единицу и самого себя. Единица простым числом не является. 
# Примечание 3. В тестирующую систему сдайте программу, содержащую только необходимую генераторную функцию primes(), но не код, вызывающий ее.

def primes(left, right):
    for i in range(left, right+1):
        counter = 0
        if i != 1:
            for j in range(2, i):
                if i%j == 0:
                    counter += 1
            if counter == 0:
                yield i
