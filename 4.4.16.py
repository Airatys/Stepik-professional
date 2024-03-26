import json

with open('food_services.json', 'r', encoding='UTF-8') as file1:
    data = json.load(file1)
    mydict = {}
    for i in data:
        mydict.setdefault(i['TypeObject'], []).append([i['Name'], i['SeatsCount']])
    for k, v in sorted(mydict.items()):
        a, b = max(v, key=lambda x: x[1])
        print(f'{k}: {a}, {b}')
        
    
   