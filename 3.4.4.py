from datetime import*
a, b, c = list(map(int, input().split(':')))
dat = timedelta(hours=a, minutes=b, seconds=c)
print(int(dat.total_seconds()))





