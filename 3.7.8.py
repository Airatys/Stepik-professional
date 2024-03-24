import calendar
from datetime import *

n = int(input())
for i in range(1, 13):
    counter = 0
    for j in calendar.monthcalendar(n, i):
        if j[3] != 0:
            counter += 1
            if counter == 3:
                print(date(n, i, j[3]).strftime('%d.%m.%Y'))

