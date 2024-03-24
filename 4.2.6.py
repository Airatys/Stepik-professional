import csv

def csv_columns(filename):
        mydict = {}
        with open(filename, encoding='utf-8') as file:
                func = csv.DictReader(file, delimiter=',')
                for dic in func:
                        for k, v in dic.items():
                                mydict.setdefault(k, []).append(v)
                return mydict
        
    





