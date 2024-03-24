import csv

with open('name_log.csv') as file, open('new_name_log.csv', 'w') as out:
    data = sorted(csv.DictReader(file), key=lambda x: (x['email'], x['dtime']))
    d = {'columns': ['username', 'email', 'dtime']}
    for i in data:
        d[i['email']] = [i['username'], i['email'], i['dtime']]   
    new_data = csv.writer(out)
    new_data.writerows(d.values())




