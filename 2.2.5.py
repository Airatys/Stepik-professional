dict = {}

for i in range(1, int(input())+1):
    s = sum(map(int, str(i)))
    dict.setdefault(s, []).append(i)
print(len(max(dict.values(), key=len)))



