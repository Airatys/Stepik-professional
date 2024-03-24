import calendar

mon = list(calendar.month_name)
mylist = mon[1:]
mydict = {}
y, m = [int(i) if i.isdigit() else i for i in input().split()]
for k, v in enumerate(mylist):
    mydict[v] = k+1
print(calendar.monthrange(y, mydict[m])[1])


