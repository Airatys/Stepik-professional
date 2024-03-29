# Дан список сотрудников организации, в котором указаны их фамилии, имена и даты рождения.
# Напишите программу, которая определяет, в какую из дат родилось больше всего сотрудников.
# Формат входных данных
# На вход программе в первой строке подается натуральное число nn — количество сотрудников, работающих в организации.
# В последующих nn строках вводятся данные о каждом сотруднике: имя, фамилия и дата рождения, разделённые пробелом.
# Дата рождения указывается в формате DD.MM.YYYY.
# Формат выходных данных
# Программа должна вывести дату, в которую наибольшее количество сотрудников отмечает день рождения, в формате DD.MM.YYYY.
# Если таких дат несколько, программа должна вывести их все в порядке возрастания, каждую на отдельной строке, в том же формате.

from datetime import date,timedelta,datetime

n=int(input())
birthday={}
for i in range(n):
    name, dat = input().rsplit(' ', 1)
    date = datetime.strptime(dat, '%d.%m.%Y')
    birthday.setdefault(date, []).append(name)
max_workers=0
for value in birthday.values():
    if len(value)>max_workers:
        max_workers=len(value)
result=[]
for keys,values in birthday.items():
    if len(values)==max_workers:
        result.append(keys)
for dates in sorted(result):
    print(dates.strftime('%d.%m.%Y'))




