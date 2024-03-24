import csv
with open('data.csv', encoding='utf-8') as file,  open('domain_usage.csv', 'w', encoding='utf-8', newline='') as file1:
        mydict = {}
        domens = ['domain', 'count']
        names = list(csv.reader(file, delimiter=','))
        names = [i[2].split('@')[1] for i in names[1:]]
        for i in names:
            mydict[i] = mydict.get(i, 0)+1
        text = csv.writer(file1, delimiter=',')
        text.writerow(domens)
        for k in sorted(mydict.items(), key=lambda x: (x[1], x[0])):
            text.writerow(k)
        
        
        




