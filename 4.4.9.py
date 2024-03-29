# Вам доступен файл people.json, содержащий список JSON-объектов. Причем у различных объектов может быть различное количество ключей:
# [
#    {
#       "age": 33,
#       "country": "Lesotho",
#       "phone": "(927) 316-2249",
#       "family_status": "married",
#       "email": "neonatus@outlook.com"
#    },
#    {
#       "age": 25,
#       "country": "Guinea",
#       "name": "Dorey",
#       "children": "yes",
#       "email": "ismail@gmail.com",
#       "university": "Khalifa University",
#       "family_status": "married"
#    },
#    ...
# ]
# Напишите программу, которая добавляет в каждый JSON-объект из данного списка все недостающие ключи, присваивая этим ключам значение null.
# Ключ считается недостающим, если он присутствует в каком-либо другом объекте, но отсутствует в данном.
# Программа должна создать список с обновленными JSON-объектами и записать его в файл updated_people.json.
# Примечание 1. JSON-объекты в создаваемом программой списке должны располагаться в своем исходном порядке. Порядок ключей в JSON-объектах не важен.
# Примечание 2. Например, если бы файл people.json имел вид:
# [
#    {
#       "age": 33,
#       "country": "Lesotho"
#    },
#    {
#       "age": 25,
#       "country": "Guinea",
#       "name": "Dorey"
#    }
# ]
# то программа должна была создать файла updated_people.json со следующим содержанием:
# [
#    {   
#       "age": 33,
#       "country": "Lesotho"
#       "name": null
#    },
#    {
#       "age": 25,
#       "country": "Guinea",
#       "name": "Dorey"
#    }
# ]

import json
mydict_1 = {}
mylist = []
with open('people.json', encoding='utf8') as file_1, open('updated_people.json', 'w', encoding='utf8') as file_2:
    dat = json.load(file_1)
    for i in dat:
        mydict_1.update(i)
    mydict_2 = {k : None for k in mydict_1}
    for i in dat:
        mylist.append(mydict_2 | i)
    json.dump(mylist, file_2, indent=3)




