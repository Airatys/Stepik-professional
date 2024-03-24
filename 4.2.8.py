import csv

mydict = {}
with open(r'wifi.csv', encoding='utf-8') as file:
    ad = list(csv.reader(file, delimiter=';'))
    for i in ad[1:]:
        mydict[i[1]] = mydict.get(i[1], 0) + int(i[-1])
for k, v in sorted(mydict.items(), key=lambda x: ((-x[1],x[0]))):
    print(f'{k}: {v}')



