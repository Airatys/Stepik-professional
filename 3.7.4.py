import calendar
y, d = map(int, input().split())
n = calendar.monthrange(y, d)
print(n[1])







