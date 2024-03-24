# put your python code here
import sys

for i in sys.stdin:
    if i.lstrip(' ')[0] !='#':
        print(i.rstrip())



