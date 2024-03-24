# put your python code here
import sys
from datetime import*

mylist = []
for i in sys.stdin:
    mylist.append(datetime.strptime(i.strip(), '%Y-%m-%d'))
mint = min(mylist) 
maxt = max(mylist)
days = maxt - mint

print(days.days)
    
    



