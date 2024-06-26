# Вам доступен набор телефонных номеров, имеющих следующие форматы:
#     <код страны>-<код города>-<номер>
#     <код страны> <код города> <номер>
# в котором код страны и код города представлены последовательностями от одной до трех цифр включительно, а номер — последовательностью от четырех до десяти цифр включительно.
# Между кодом страны, кодом города и номером используется разделитель, которым служит либо символ дефис, либо пробел, причем одновременно оба вида разделителя в одном номере присутствовать не могут.
# Напишите программу, которая принимает произвольное количество телефонных номеров и для каждого выводит отдельно его код страны, код города и номер.
# Формат входных данных
# На вход программе подается произвольное количество телефонных номеров, удовлетворяющих приведенным выше шаблонам, каждый на отдельной строке.
# Формат выходных данных
# Программа должна для каждого введенного телефонного номера вывести отдельно его код страны, код города и номер в следующем формате:
# Код страны: <код страны>, Код города: <код города>, Номер: <номер>

import sys
import re 

pattern_string = r'(\d{1,3})([-\s])(\d{1,3})\2(\d{4,10})'
for i in sys.stdin:
    regex = re.fullmatch(pattern_string, i.strip())
    print(f'Код страны: {regex.group(1)}, Код города: {regex.group(3)}, Номер: {regex.group(4)}')