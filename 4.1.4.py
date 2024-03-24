# put your python code here
import sys

mylist = [int(i.strip())for i in sys.stdin]
if len(mylist) > 0:
    print('Рост самого низкого ученика:', min(mylist))
    print('Рост самого высокого ученика:', max(mylist))
    print('Средний рост:', sum(mylist)/len(mylist))
else:
    print('нет учеников')



