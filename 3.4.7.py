from datetime import *
d, m, y = map(int, input().split('.'))
dat = date(y, m, d)
print(dat.strftime('%d.%m.%Y'))
for i in range(2, 11):
    dat += timedelta(days=i)
    print(dat.strftime('%d.%m.%Y'))





