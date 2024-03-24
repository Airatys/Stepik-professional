# put your python code here
import sys
from datetime import*

counter_a = 0
counter_g = 0
mylist = [int(i) for i in sys.stdin]
for i in range(1, len(mylist)-1):
    if 2*mylist[i] == mylist[i-1] + mylist[i+1]:
        counter_a += 1    
    elif mylist[i]**2 == mylist[i-1]*mylist[i+1]:
        counter_g += 1
       
if counter_a == len(mylist)-2:
            print('Арифметическая прогрессия')
elif counter_g == len(mylist)-2:
            print('Геометрическая прогрессия')
else:
        print('Не прогрессия')



