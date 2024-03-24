import csv

mydict = {}
with open('prices.csv', encoding='utf-8') as file:
    dat = list(csv.reader(file, delimiter=';'))
    d = dat[0][1:]
    for i in dat[1:]:
        for j  in range(len(i)-1):
            mydict.setdefault(i[0], []).append((d[j], i[j+1]))
    for k, v  in mydict.items():
        mydict[k] = min(v, key=lambda x: (int(x[1]), x[0]))
    dat_min = min((int(v[1]), v[0], k) for k, v in mydict.items())
    print(f'{dat_min[1]}: {dat_min[2]}')




