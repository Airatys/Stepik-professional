from datetime import date
def saturdays_between_two_dates(start, end):
    if start < end:
        return len([i for i in range(start.toordinal(), end.toordinal()+1) if date.fromordinal(i).isoweekday()==6])
    else:
        return len([i for i in range(end.toordinal(), start.toordinal()+1) if date.fromordinal(i).isoweekday()==6])
    




