from datetime import date, time
def print_good_dates(dates):
    mylist = [i for i in dates if i.year == 1992 and (i.month + i.day) == 29]
    for i in sorted(mylist):
        print(i.strftime('%B %d, %Y'))




