# В онлайн-школе BEEGEEK логин учетной записи определяется следующим образом:
#     первым символом является символ нижнего подчеркивания _
#     затем следуют одна или более цифр
#     после записываются ноль или более латинских букв в произвольном регистре
#     логин может иметь на конце необязательный символ нижнего подчеркивания _
# Напишите программу, которая принимает произвольное количество строк и определяет, какие из них представляют собой корректный логин онлайн-школы BEEGEEK.
# Формат входных данных
# На вход программе подаётся произвольное количество строк, каждая из которых содержит набор произвольных символов.
# Формат выходных данных
# Программа должна для каждой введенной строки вывести True, если она представляет собой корректный логин онлайн-школы BEEGEEK, или False в противном случае.

import sys
import re

pattern = r'_\d{1,}[A-Za-z]*_?'
for i in map(str.strip, sys.stdin):
    if re.fullmatch(pattern, i):
        print(True)
    else:
        print(False)
        
# решение через приведение к bool через функцию

import sys
import re

for i in map(str.strip, sys.stdin):
    print(bool(re.fullmatch(r'_\d{1,}[A-Za-z]*_?', i)))