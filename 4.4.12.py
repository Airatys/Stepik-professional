import json
import csv

with open('students.json', encoding='utf8') as file_1, open('data.csv', 'w', encoding='utf8', newline='') as file_2:
    dat = list(json.load(file_1))
    stud = list(filter(lambda x: x["age"] >= 18 and x['progress'] >= 75, dat))
    zapis = csv.writer(file_2, delimiter=',')
    zapis.writerow(['name', 'phone'])
    for i in sorted(stud, key=lambda x: x['name']):
        zapis.writerow([i['name'], i['phone']])