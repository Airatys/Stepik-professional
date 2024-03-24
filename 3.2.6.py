from datetime import *
mylist = [date.fromisoformat(input()) for i in range(int(input()))]
mylist = sorted(mylist)
for i in mylist:
    print(i.strftime('%d/%m/%Y'))




