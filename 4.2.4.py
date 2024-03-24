import csv

with open('salary_data.csv', encoding='utf-8') as file:
        mydict = {}
        price = csv.reader(file, delimiter=';')
        price = list(price)
        for i in price[1:]:
                mydict.setdefault(i[0], []).append(int(i[1]))
for k in sorted(mydict, key=lambda x: sum(mydict[x])/len(mydict[x])):
        print(k)
    
    




