from datetime import *
dat = datetime.strptime(input(), '%d.%m.%Y %H:%M')
mydict = {0: (9, 21), 1: (9, 21), 2: (9, 21), 3: (9, 21), 4: (9, 21), 5: (10, 18), 6: (10, 18)}
h1, h2 = mydict[dat.date().weekday()]
if timedelta(hours=h1) <= timedelta(hours=dat.hour, minutes=dat.minute) < timedelta(hours=h2):
    d = timedelta(hours=h2) - timedelta(hours=dat.hour, minutes=dat.minute)
    print(d.seconds//60)

else:
    print('Магазин не работает')




