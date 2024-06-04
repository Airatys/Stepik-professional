# Напишите программу, которая в заданном тексте находит все телефонные номера, соответствующие следующим форматам:
# 7-ddd-ddd-dd-dd
# 8-ddd-dddd-dddd
# где d — цифра от 00 до 99.
# Формат входных данных
# На вход программе подается строка произвольного содержания.
# Формат выходных данных
# Программа должна в введенном тексте найти все телефонные номера, соответствующие форматам, указанным в условии задачи, и вывести их в том порядке, в котором они были найдены, каждый на отдельной строке.

def is_phone_number(phone): 
    groups = phone.split('-')
    if len(groups) == 5:
        a, b, c, d, e = groups
        if len(a) == 1 and len(b) == 3 and len(c) == 3 and len(d) == 2 and len(e) == 2:
            chr = ''.join(groups)
            if chr.find('7') == 0 and len(chr) == 11:
                return all(i.isdigit() for i in chr for j in i)   
    if len(groups) == 4:
        a, b, c, d = groups
        if len(a) == 1 and len(b) == 3 and len(c) == 4 and len(d) == 4:
            chr = ''.join(groups)
            if chr.find('8') == 0 and len(chr) == 12:
                return all(i.isdigit() for i in chr for j in i)
            
def all_numer(text):
    for i in range(len(text)-14):
        num = text[i:i+15]
        if is_phone_number(num):
            yield num
t = input()
print(*all_numer(t), sep='\n')