from datetime import*
import calendar
def get_all_mondays(year): 
    callist = []
    a = date(year, 1, 1)
    if calendar.isleap(year):
        for i in range(a.toordinal(), a.toordinal() + 366):
            if date.fromordinal(i).weekday() == 0:
                callist.append(date.fromordinal(i))
        return callist
    else:
        for i in range(a.toordinal(), a.toordinal() + 365):
            if date.fromordinal(i).weekday() == 0:
                callist.append(date.fromordinal(i))
        return callist
        
    
        
    




