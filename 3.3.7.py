from datetime import *
def is_available_date(booked_dates, date_for_booking):
    myset1 = set()
    for i in booked_dates:
        if len(i) == 10:
            a, b, c = list(map(int, i.split('.')))
            myset1.add(date(c, b, a).toordinal())
        elif len(i) > 10:
            list1, list2 = i.split('-')
            a1, b1, c1 = list(map(int, list1.split('.')))
            a2, b2, c2 = list(map(int, list2.split('.')))
            for d in range(date(c1, b1, a1).toordinal(), date(c2, b2, a2).toordinal()+1):
                myset1.add(d)
            
    myset2 = set()    
    if len(date_for_booking) == 10:
        a, b, c = list(map(int, date_for_booking.split('.')))
        myset2.add(date(c, b, a).toordinal())
    elif len(date_for_booking) > 10:
        list1, list2 = date_for_booking.split('-')
        a1, b1, c1 = list(map(int, list1.split('.')))
        a2, b2, c2 = list(map(int, list2.split('.')))
        for i in range(date(c1, b1, a1).toordinal(), date(c2, b2, a2).toordinal()+1):
            myset2.add(i)
            
    return True if myset1.isdisjoint(myset2) else False




