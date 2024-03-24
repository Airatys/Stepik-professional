from datetime import date,timedelta,datetime

n=int(input())
birthday={}
for i in range(n):
    name, dat = input().rsplit(' ', 1)
    date = datetime.strptime(dat, '%d.%m.%Y')
    birthday.setdefault(date, []).append(name)
max_workers=0
for value in birthday.values():
    if len(value)>max_workers:
        max_workers=len(value)
result=[]
for keys,values in birthday.items():
    if len(values)==max_workers:
        result.append(keys)
for dates in sorted(result):
    print(dates.strftime('%d.%m.%Y'))




