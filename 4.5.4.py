# Вам доступен архив workbook.zip, содержащий различные папки и файлы.
# Напишите программу, которая выводит названия файлов из этого архива, которые были созданы или изменены позднее 2021-11-30 14:22:00.
# Названия файлов должны быть расположены в лексикографическом порядке, каждое на отдельной строке.
# Примечание 1. Если файл находится в папке, вывести следует только название без пути.
# Примечание 2. Начальная часть ответа выглядит так:
# countries.json
# data_sample.csv

from zipfile import ZipFile
from datetime import datetime

mylist = []
with ZipFile('workbook.zip') as file:
    info = file.infolist()
    for i in info:
        a, b, c, h, m, s = i.date_time
        if datetime(a, b, c, h, m, s) > datetime(2021, 11, 30, 14, 22) and not i.is_dir():
            mylist.append(i.filename.split('/')[-1])
    print(*sorted(mylist), sep='\n')
    