import json

mylist = []
with open('pools.json', encoding='utf8') as filein:
    dat = json.load(filein)
    for i in dat:
        start, end = i['WorkingHoursSummer']['Понедельник'].split('-')
        if int(start.split(':')[0]) == 10 and int(end.split(':')[0]) >= 12:
            adres = i['Address']
            a = int(i['DimensionsSummer']['Length']) 
            b = int(i['DimensionsSummer']['Width'])
            mylist.append([a, b, f'{a}x{b}', adres])
    res = sorted(mylist, key=lambda x: (x[0], x[1]), reverse=True)
    print(*res[0][2:], sep='\n')