# Используя синтаксис анонимных функций, реализуйте рекурсивную функцию fib(), которая принимает один аргумент:
#     n — натуральное число
# Функция должна возвращать n-ый член последовательности Фибоначчи.
# Примечание 1. Последовательность Фибоначчи – последовательность натуральных чисел, где каждое последующее число является суммой двух предыдущих: 
# 1,1,2,3,5,8,13,21,34,55,89,144,233,...
# 1,1,2,3,5,8,13,21,34,55,89,144,233,...Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимую функцию fib(), но не код, вызывающий ее.

fib = lambda x: 1 if x <=2 else fib(x-1) + fib(x-2)