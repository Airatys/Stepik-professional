mylist_1 = [input() for i in range(int(input()))]
mylist_2 = [input() for i in range(int(input()))]

for i in mylist_2:
    n = 1
    name = i + '@beegeek.bzz'
    while name in mylist_1:
        name = i + str(n) + '@beegeek.bzz'
        n += 1
    print(name)
    mylist_1.append(name)
               





