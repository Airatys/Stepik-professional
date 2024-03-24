import csv

def condense_csv(filename: csv, id_name: str):
    mylist = [id_name] 
    mydict = {}  
    with open(filename, encoding='utf-8') as file_1, open('condensed.csv', 'w', encoding='utf-8', newline='') as file_2:
        red = list(csv.reader(file_1, delimiter=','))
        for i in red:
            if i[1] not in mylist:
                mylist.append(i[1])
            mydict.setdefault(i[0], []).append(i[2])    
        wed = csv.writer(file_2, delimiter=',')
        wed.writerow(mylist)
        for k, v in mydict.items():
            wed.writerow([k, *v])




