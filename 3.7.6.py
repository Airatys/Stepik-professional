import calendar
from datetime import *

def get_days_in_month(year, month):
    mydict = {}
    callist = []
    mon = list(calendar.month_name)
    mylist = mon[1:]
    for k, v in enumerate(mylist):
        mydict[v] = k+1
    n = calendar.monthrange(year, mydict[month])[1]
    
    a = date(year, mydict[month], 1)
    for i in range(a.toordinal(), a.toordinal() + n):
        callist.append(date.fromordinal(i))
    return callist
    
    
    
    
    




