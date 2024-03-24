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




