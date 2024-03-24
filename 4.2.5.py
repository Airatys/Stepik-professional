import csv
n = int(input())
with open('deniro.csv', encoding='utf-8') as file:
        tabl = list(csv.reader(file, delimiter=','))
        for i in sorted(tabl, key=lambda x: int(x[n-1]) if x[n-1].isdigit() else x[n-1]):
                print(','.join(i))




