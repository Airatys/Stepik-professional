n = int(input())
mylist = []
for i in range(n):
    myset = set([i.strip() for i in input().split(',')])
    mylist.append(myset)

f = mylist[0]
for i in range(1, len(mylist)):
    f.intersection_update(mylist[i])
if len(f) == 0:
    print('Сериал снять не удастся')
else:
    print(*sorted(list(f)), sep=', ')
    




