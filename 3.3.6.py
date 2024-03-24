from datetime import *
with open('diary.txt', encoding='utf-8') as file:
    mydict = {}
    f = file.read().split('\n\n')
    for i in f:
        d = datetime.strptime(i[:17], '%d.%m.%Y; %H:%M')
        mydict.setdefault(d, i[17:])
    mydict = dict(sorted(mydict.items()))
    
    for i, k in mydict.items():
        print(datetime.strftime(i, '%d.%m.%Y; %H:%M'), k, sep='')
        print()