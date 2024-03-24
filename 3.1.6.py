from datetime import date
def get_date_range(start, end):
    if start > end:
        return []
    else:
        return [date.fromordinal(i) for i in range(start.toordinal(), end.toordinal()+1)]
    




