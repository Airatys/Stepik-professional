# put your python code here
import sys
from datetime import*

mylist = []
for i in sys.stdin:
    mylist.append(datetime.strptime(i.strip(), '%d.%m.%Y'))
if mylist == sorted(mylist) and len(mylist) == len(set(mylist)):
    print('ASC')
elif mylist == sorted(mylist, reverse=True) and len(mylist) == len(set(mylist)):
    print('DESC')
else:
    print('MIX')
                  
                  
    
    



