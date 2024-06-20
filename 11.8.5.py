# Назовем умножением строки на число запись в формате n(string), где n — неотрицательное целое число, а string — строка, которая должна быть записана n раз.
# Раскрытием умножения будем считать развернутый вариант данной записи, например, строка ti2(Be)3(Ge) после раскрытия в ней всех умножений будет иметь вид tiBeBeGeGeGe.
# Напишите программу, которая раскрывает все умножения в тексте и выводит полученный результат.
# Формат входных данных
# На вход программе подается одна строка, содержащая строчные латинские буквы, числа и скобки.
# Формат выходных данных
# Программа должна вывести строку, в которой раскрыты все умножения с учетом приоритетности операций.
# Примечание 1. Гарантируется, что умножение в подаваемой строке всегда записано корректно, то есть строго в формате n(string). Записи вида 4(2), 3q, (fg)7 не корректны.
# Примечание 2. Рассмотрим третий тест. С учетом приоритетности операций сначала раскрываем умножение 2(a) и получаем промежуточную строку bbbb10(aa)bbb, далее раскрываем умножение 10(aa) и получаем конечный результат в виде строки bbbbaaaaaaaaaaaaaaaaaaaabbb.
# Примечание 3. Строка, в которой раскрыты все умножения, всегда содержит исключительно строчные латинские буквы.
# Примечание 4. Максимальная длина результирующей строки не превосходит 450000450000 символов.

import re

def recursive(regex: str) -> str:
    res = re.sub(r'(\d+)\((\w*)\)', lambda x: int(x.group(1)) * x.group(2), regex) 
    if '(' in res:
        return recursive(res)
    else:
        return res 
text = input()
print(recursive(text))
