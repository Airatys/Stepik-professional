from datetime import *
mydict = {}
dat = datetime.strptime(input(),'%d.%m.%Y')
y = dat.year
n = int(input())
for i in range(n):
    name, dat1 = input().rsplit(' ', 1)
    date = datetime.strptime(dat1, '%d.%m.%Y')
    if dat < date.replace(year=y) <= (dat + timedelta(days=7)) or dat < date.replace(year=y+1) <= (dat + timedelta(days=7)):
        mydict.setdefault(date, []).append(name)
        
if len(mydict) != 0:
    print(*mydict[max(mydict)])              
else:
    print('Дни рождения не планируются')
