import csv

mydict = {}
with open(r'titanic.csv', encoding='utf-8') as file:
    ad = list(csv.reader(file, delimiter=';'))
    for i in ad[1:]:
        if int(i[0]) == 1 and i[2] == 'male' and float(i[3]) < 18:
            print(i[1])
    for i in ad[1:]:
        if int(i[0]) == 1 and i[2] == 'female' and float(i[3]) < 18:
            print(i[1])




