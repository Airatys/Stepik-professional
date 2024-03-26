import csv
import json
from datetime import *

mylist = []
with open('exam_results.csv', encoding='utf8') as file_1, open('best_scores.json', 'w', encoding='utf8') as file_2:
    dat = list(csv.DictReader(file_1, delimiter=','))
    result = sorted(dat, key=lambda x: (x['email'],  x['score'], datetime.strptime(x['date_and_time'], '%Y-%m-%d %H:%M:%S')), reverse=True)
    mylist.append(result[0])
    for i in range(1, len(result)):
        if result[i]['email'] != result[i-1]['email']:
            mylist.append(result[i])
    mylist = sorted(mylist, key=lambda x: x['email'])
    d = [{'best_score' if k =='score' else k : v for k, v in i.items()} for i in mylist]
    d1 = [{k : v if k != 'best_score' else int(v) for k, v in i.items()} for i in d]
    json.dump(d1, file_2, indent=3)
        
    
    