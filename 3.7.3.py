import calendar

y, h, d = [int(i) for i in input().split('-')]
i = calendar.weekday(y, h, d)
print(calendar.day_name[i])





