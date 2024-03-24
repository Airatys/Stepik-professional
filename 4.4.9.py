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




