# Требовалось написать программу, которая принимает на вход два целых числа aa и bb, каждое на отдельной строке, и выводит список всех целых чисел от aa до bb включительно, которые делятся на 77 без остатка.
# Программист торопился и написал программу неправильно.
# Найдите и исправьте все ошибки, допущенные в этой программе (их ровно 55).
# Примечание. Известно, что каждая ошибка затрагивает только одну строку и может быть исправлена без изменения других строк.

a = int(input())
b = int(input())
numbers = []

for i in range(a, b+1):
    if i % 7 == 0:
        numbers.append(i)

print(numbers)