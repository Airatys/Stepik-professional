n = list(map(str, input().split()))
mylist = []
for i in n:
    counter = n.count(i)
    if counter >= 2 and i not in mylist:
        mylist.append(i)
print(*sorted(int(i) for i in mylist))
        




