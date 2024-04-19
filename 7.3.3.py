# Напишите программу с использованием конструкции try-except, которая принимает на вход название текстового файла и выводит его содержимое.
# Если файла с данным названием нет в папке с программой, программа должна вывести текст:
# ​Файл не найден
# Формат входных данных
# На вход программе подается название текстового файла.
# Формат выходных данных
# Программа должна вывести содержимое файла с введенным названием или соответствующий текст, если файла с данным названием нет в папке с программой.
# Примечание 1. Название подаваемого файла уже содержит расширение.
# Примечание 2. При открытии файла используйте явное указание кодировки UTF-8.

try:
    with open(input(), encoding='u8') as file:
        data = file.read()
        print(data)
except FileNotFoundError:
    print('Файл не найден')