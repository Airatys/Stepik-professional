# Напишите программу, которая принимает на вход название JSON файла, десериализует содержащийся в этом файле объект и выводит его.
#     если файла с данным названием нет в папке с программой, программа должна вывести текст:
#     Файл не найден
#     если файл с данным названием содержит некорректные данные (то есть не удовлетворяющие формату JSON), программа должна вывести текст:
#     Ошибка при десериализации
# Формат входных данных
# На вход программе подается название JSON файла.
# Формат выходных данных
# Программа должна десериализовать объект, содержащийся в файле с введенным названием, и вывести его.
# Если при поиске файла или десериализации его содержимого произошла ошибка, программа должна вывести соответствующий текст.
# Примечание 1. Название подаваемого файла уже содержит расширение.
# Примечание 2. В первом тесте файл numbers.json имеет следующее содержание
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Файл countries.json, представленный во втором тесте, отсутствует в папке с программой.
# В третьем тесте файл stores.json имеет следующее содержание:
# [}{}D}A{Sd]as][d]as[d][A}SD[as]d[][1111111111111[{}0002

import json
try:
    with open(input(), encoding='u8') as file:
        jfile = json.load(file)
        print(jfile)
except FileNotFoundError:
    print('Файл не найден')
except:
    print('Ошибка при десериализации')