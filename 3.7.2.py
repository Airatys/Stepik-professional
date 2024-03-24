import calendar
mydict = {}
y, m = input().split()
mylist = list(calendar.month_abbr)
for k, v in enumerate(mylist[1:]):
    mydict[v] = k+1
print(calendar.month(int(y), mydict[m]))




