text = input()
s = [i for i, j in enumerate(text) if j in 'а, у, о, ы, и, э, я, ю, ё, е']
count = len(s)
n = int(input())
for i in range(n):
    value = input()
    v = [i for i, j in enumerate(value) if j in 'а, у, о, ы, и, э, я, ю, ё, е']
    if s == v:
        print(value)
    
            
        





