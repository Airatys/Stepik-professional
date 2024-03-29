# Вам доступен архив workbook.zip, содержащий различные папки и файлы.
# Напишите программу, которая выводит единственное число — количество файлов в этом архиве.
# Примечание 1. Обратите внимание, что папка не считается файлом.

from zipfile import ZipFile

with ZipFile('workbook.zip') as file:
    counter = 0
    dat = file.infolist()
    for i in dat:
        if not i.is_dir():
            counter += 1
    print(counter)

