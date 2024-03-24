import csv
import json

mydict = {}
with open('playgrounds.csv', encoding='utf8') as file_1, open('addresses.json', 'w', encoding='utf8') as file_2:
    addr = list(csv.reader(file_1, delimiter=';'))
    titl = addr[:1]
    for i in addr[1:]:
        mydict.setdefault(i[1], {}).setdefault(i[2], []).append(i[3])
    json.dump(mydict, file_2, indent=3, ensure_ascii=False)