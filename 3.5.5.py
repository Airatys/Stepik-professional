from datetime import *
a = int(input())
mydict = {}
for i in range(a):
    *n, m = input().split()
    mydict.setdefault(datetime.strptime(m, '%d.%m.%Y'), n)
if len(mydict) == a:
    print((min(mydict).strftime('%d.%m.%Y')), *mydict[min(mydict)])
else:
    print((min(mydict).strftime('%d.%m.%Y')), a - len(mydict)+1)
    
    




