from datetime import *


n = datetime.strptime(input(), '%H:%M')
m = datetime.strptime(input(), '%H:%M')

while n+timedelta(minutes=45) <= m:
    print(f'{n.strftime("%H:%M")} - {(n+timedelta(minutes=45)).strftime("%H:%M")}')
    n += timedelta(minutes=55)




