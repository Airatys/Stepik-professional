from datetime import *
h, m, s = map(int, input().split(':'))
sec = int(input())
dat = datetime(1, 1, 1, hour=h, minute=m, second=s) + timedelta(seconds=sec)
print(dat.time())





