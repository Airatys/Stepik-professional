import json

mydict = {}
with open('countries.json', encoding='utf8') as file_1, open('religion.json', 'w', encoding='utf8') as file_2:
    dat = json.load(file_1)
    for i in dat:
        mydict.setdefault(i["religion"], []).append(i["country"])
    json.dump(mydict, file_2, indent=3)
              
        




