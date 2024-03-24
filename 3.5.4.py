from datetime import *
date1 = datetime.strptime(input(), '%d.%m.%Y')
date2 = datetime.strptime(input(), '%d.%m.%Y')

if (date1.day + date1.month) %2 != 0:
    for i in range(date1.toordinal(), date2.toordinal()+1, 3):
        if date.fromordinal(i).weekday() != 0 and date.fromordinal(i).weekday() != 3:
            print(date.fromordinal(i).strftime('%d.%m.%Y'))
elif date1 != date2:
    date1 += timedelta(days=1)
    if (date1.day + date1.month) %2 != 0:
        for i in range(date1.toordinal(), date2.toordinal()+1, 3):
            if date.fromordinal(i).weekday() != 0 and date.fromordinal(i).weekday() != 3:
                print(date.fromordinal(i).strftime('%d.%m.%Y'))
    else:
        date1 += timedelta(days=1)
        for i in range(date1.toordinal(), date2.toordinal()+1, 3):
            if date.fromordinal(i).weekday() != 0 and date.fromordinal(i).weekday() != 3:
                print(date.fromordinal(i).strftime('%d.%m.%Y'))



