from datetime import *
n = list(map(lambda x: datetime.strptime(x,'%d.%m.%Y'), input().split()))
mylist = []
if len(n) == 1:
    print([])
elif len(n) > 1:
    for i in range(len(n)-1):
        mylist.append(abs(n[i] - n[i+1]).days)
    print(mylist)

    




