# Для дополнительного заработка Тимур решил заняться продажей овощей. У него имеются данные о продажах за год, разделенные на четыре файла по кварталам: quarter1.csv, quarter2.csv, quarter3.csv и quarter4.csv.
# В каждом файле в первом столбце указывается название продукта, а в последующих — количество проданного продукта в килограммах за определенный месяц:
# продукт,январь,февраль,март
# Картофель,39,61,3
# Дайкон,51,96,83
# ...
# Также присутствует файл prices.json, содержащий словарь, в котором ключом является название продукта, а значением — цена за килограмм в рублях:
# {
#    "Картофель": 53,
#    "Дайкон": 55,
# ...
# }
# Напишите программу, которая выводит единственное число — сумму, заработанную Тимуром за год на продаже овощей.
# Примечание 1. Ссылки на указанные файлы: quarter1.csv, quarter2.csv, quarter3.csv, quarter4.csv, prices.json. Ответ на задачу доступен по ссылке.
# Примечание 2. При открытии файла используйте явное указание кодировки UTF-8.

import json
import csv
from collections import Counter

file = ['quarter1.csv', 'quarter2.csv', 'quarter3.csv', 'quarter4.csv']
dat = Counter()
for i in file:
    with open(i, encoding='u8') as csvfile:
        csvdat = list(csv.reader(csvfile, delimiter=','))[1:]
        for i in csvdat:
            dat.update({i[0]:sum([int(i[1]), int(i[2]), int(i[3])])})
counter = 0
with open('prices.json', encoding='u8') as jsonfile:
    jsondat = json.load(jsonfile)
    for k, v in dat.items():
        counter += jsondat[k] * v
    print(counter)
        