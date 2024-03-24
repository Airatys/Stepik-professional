from datetime import *
a, b, c = list(map(int, input().split('.')))

d1 = date(c, b, a) - timedelta(days=1)
d2 = date(c, b, a) + timedelta(days=1)
print(d1.strftime('%d.%m.%Y'))
print(d2.strftime('%d.%m.%Y'))