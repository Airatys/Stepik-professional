# put your python code here
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
    
    



