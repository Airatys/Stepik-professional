# Напишите программу с использованием рекурсии, которая выводит последовательность натуральных чисел от 1 до 100 включительно.
# Формат входных данных
# На вход программе ничего не подается.
# Формат выходных данных
# Программа должны вывести последовательность натуральных чисел от 11 до 100100 включительно, каждое на отдельной строке.
# Примечание. Начальная часть ответа выглядит так:
# 1
# 2
# 3
# 4
# 5
# ...

def rec(n):
    if n <= 100:
        print(n)
        rec(n+1) 
rec(1)