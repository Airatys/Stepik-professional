# put your python code here
import sys

counter = 0
for i in sys.stdin:
    if i.strip()[0] =='#':
        counter += 1
print(counter)
    



