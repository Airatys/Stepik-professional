# put your python code here
import sys

for i in sys.stdin.readlines():
    print(i.rstrip('\n')[::-1])




