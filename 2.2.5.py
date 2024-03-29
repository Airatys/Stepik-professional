# Назовем набор различных натуральных чисел группой. Например: (13,4,22,40)(13,4,22,40).
# Тогда длиной группы будем считать количество чисел в группе. Например, длина группы (13,4,22,40)(13,4,22,40) равна 44.
# Дана последовательность натуральных чисел от 11 до nn включительно.
# Напишите программу, которая группирует все числа данной последовательности по сумме их цифр и определяет длину группы, содержащей наибольшее количество чисел.
# Формат входных данных
# На вход программе подается натуральное число nn.
# Формат выходных данных
# Программа должна сгруппировать все числа из натуральной последовательности от 11 до nn по сумме их цифр и определить длину группы, содержащей наибольшее количество чисел.
# Примечание 1. Рассмотрим третий тест, в котором n=20n=20. Запишем последовательность чисел от 11 до 2020:
# 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20
# 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20Сгруппируем полученные числа по сумме их цифр:
# (1,10),(2,11,20),(3,12),(4,13),(5,14),(6,15),(7,16),(8,17),(9,18),(19)
# (1,10),(2,11,20),(3,12),(4,13),(5,14),(6,15),(7,16),(8,17),(9,18),(19)
# Итак, длина группы с наибольшим количеством чисел равна 33.

dict = {}

for i in range(1, int(input())+1):
    s = sum(map(int, str(i)))
    dict.setdefault(s, []).append(i)
print(len(max(dict.values(), key=len)))



