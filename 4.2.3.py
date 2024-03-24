import csv

with open('sales.csv', 'r', encoding='utf-8') as file:
        prais = csv.reader(file, delimiter=';')
        for i in prais:
                if i[1].isdigit() and int(i[1]) > int(i[2]):
                        print(i[0])




