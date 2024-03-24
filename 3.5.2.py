from datetime import date, time, datetime
data1 = date(1, 1, 1)
data2 = date(9999, 12, 31)
d = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
for i in range(data1.toordinal(), data2.toordinal()+1):
    if date.fromordinal(i).day == 13:
        d[date.fromordinal(i).weekday()] = d.get(date.fromordinal(i).weekday(), 0)+1

for k, v in d.items():
    print(v)



