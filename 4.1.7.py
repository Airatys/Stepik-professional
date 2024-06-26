# По чатам одного немалоизвестного мессенджера начали появляться новости сомнительного содержания. Оказалось, что некий молодежный клуб решил подшутить, распространяя всякие глупости.
# Однако подобное хулиганство мешает доверчивым людям, особенно пенсионного возраста, поэтому группа независимых программистов решила разработать бота, который мог бы оценить степень достоверности новости, а также отнести её к какой-либо категории.
# Напишите программу, которая выводит все новости заданной категории, располагая их по возрастанию степени достоверности.
# Формат входных данных
# На вход программе подается произвольное количество строк, в каждой строке, кроме последней, записана новость, категория, к которой она относится, и ее достоверность в следующем формате:
# <новость> / <категория> / <достоверность>
# В последней строке подается одиночная категория.
# Формат выходных данных
# Программа должна вывести все новости, которые относятся к введенной категории. Новости должны быть расположены в порядке возрастания степени достоверности, а при совпадении степеней достоверности — в лексикографическом порядке самих новостей.

import sys

mydict = {}
for i in sys.stdin:
    try:
        a, b, c = i.rstrip().split(' / ')
        if b == 'Политика':
            mydict.setdefault(a, float(c))
    except:
        for k, v in sorted(mydict.items(), key = lambda x: (x[1], x[0])):
            print(k)
    
    



