# Вам доступен файл data.json, содержащий список различных объектов:
# [
#    "nwkWXma",
#    null,
#    {
#       "ISgHT": "dIUbf"
#    },
#    "Pzt",
#    "BXcbGVTE",
#    ...
# ]
# Напишите программу, которая создает список, элементами которого являются объекты из списка, содержащегося в файле data.json, измененные по следующим правилам:
#     если объект является строкой, в его конец добавляется восклицательный знак
#     если объект является числом, он увеличивается на единицу
#     если объект является логическим значением, он инвертируется
#     если объект является списком, он удваивается
#     если объект является JSON-объектом (словарем), в него добавляется новая пара "newkey": null
#     если объект является пустым значением (null), он не добавляется
# Полученный список программа должна записать в файл updated_data.json.
# Примечание 1. Например, если бы файл data.json имел вид:
# ["Hello", 179, true, null, [1, 2, 3], {"key": "value"}]
# то программа должна была бы создать файл updated_data.json со следующим содержанием:
# ["Hello!", 180, false, [1, 2, 3, 1, 2, 3], {"key": "value", "newkey": null}]

import json

mylist = []
with open('data.json', encoding='utf8') as file_1, open('updated_data.json', 'w', encoding='utf8') as file_2:
    dat = json.load(file_1)
    for i in dat:
        if type(i) == str:
            mylist.append(i + '!')
        elif type(i) == int:
            mylist.append(i + 1)
        elif type(i) == bool:
            mylist.append(not i)
        elif type(i) == list:
            mylist.append(i * 2)
        elif type(i) == dict:
            mylist.append(i | {"newkey": None})       
            print()
    json.dump(mylist, file_2, indent=3) 




