# Напишите программу, которая принимает на вход время и выводит целое количество секунд, прошедшее с начала суток.
# Формат входных данных
# На вход программе подается время в формате HH:MM:SS.
# Формат выходных данных
# Программа должна вывести целое количество секунд, прошедшее с начала суток.
# Примечание 1. Началом суток считается момент времени, соответствующий 00:00:00.

from datetime import*
a, b, c = list(map(int, input().split(':')))
dat = timedelta(hours=a, minutes=b, seconds=c)
print(int(dat.total_seconds()))





