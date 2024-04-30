# Напишите программу, которая определяет минимальное и максимальное значения функции на отрезке в целых точках.
# Формат входных данных
# На вход программе в первой строке подается корректная функция f(x), в следующей строке вводятся два целых числа a и b, разделенные пробелом, которые представляют границы отрезка [a;b].
# Формат выходных данных
# Программа должна определить минимальное и максимальное значения функции f(x) на отрезке [a;b] в целых точках и вывести полученный результат в следующем формате:
# Минимальное значение функции <функция f(x)> на отрезке <отрезок> равно <мин. значение>
# Максимальное значение функции <функция f(x)> на отрезке <отрезок> равно <макс. значение>
# Примечание 1. Под корректной функцией подразумевается выражение, полностью соответствующее синтаксису языка Python.

func = input()
a, b = map(int, input().split())
code = [eval(func) for x in range(a, b+1)]
print(f'Минимальное значение функции {func} на отрезке [{a}; {b}] равно {min(code)}')
print(f'Максимальное значение функции {func} на отрезке [{a}; {b}] равно {max(code)}')