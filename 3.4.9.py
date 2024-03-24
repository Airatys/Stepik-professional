from datetime import *
def fill_up_missing_dates(dates):
    mylist = []
    n = [datetime.strptime(i, '%d.%m.%Y') for i in dates]
    a = min(n).date()
    b = max(n).date()
    for i in range(a.toordinal(), b.toordinal()+1):
        mylist.append(date.fromordinal(i).strftime('%d.%m.%Y'))
    return mylist
    




