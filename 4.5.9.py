# Вам доступен архив data.zip, содержащий различные папки и файлы.
# Среди них есть несколько JSON файлов, каждый из которых содержит информацию о каком-либо футболисте:
# {
#    "first_name": "Gary",
#    "last_name": "Cahill",
#    "team": "Chelsea",
#    "position": "Defender"
# }
# У футболиста имеются следующие атрибуты: 
#     first_name — имя
#     last_name — фамилия
#     team — название футбольного клуба
#     position — игровая позиция
# Напишите программу, которая обрабатывает только данные JSON файлы и выводит имена и фамилии футболистов, выступающих за футбольный клуб Arsenal.
# Футболисты должны быть расположены в лексикографическом порядке имен, а при совпадении — в лексикографическом порядке фамилий, каждый на отдельной строке.
# Примечание 1. Обратите внимание, что наличие у файла расширения .json не гарантирует, что он является корректным текстовым файлом в формате JSON.
# Для того чтобы определить, является ли файл корректным текстовым файлом в формате JSON, воспользуйтесь конструкцией try-except и функцией is_correct_json() из предыдущего урока.
# Примечание 2. Начальная часть ответа выглядит так:
# Alex Iwobi
# Alexis Sanchez
# ...

from zipfile import ZipFile
import json

mylist = []
with ZipFile('data.zip') as file_1:
    for i in file_1.infolist():
        try:
            with file_1.open(i) as file_2:
                text = file_2.read().decode('utf-8')
                info = json.loads(text)
                if info['team'] == 'Arsenal':
                    mylist.append([info['first_name'], info['last_name']])    
        except:
            continue
    for i in sorted(mylist, key=lambda x: x[0]):
      print(*i)
