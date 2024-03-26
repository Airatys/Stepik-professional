
import json

with open('food_services.json', 'r', encoding='UTF-8') as file1:
    data = json.load(file1)
    d_dist = {}
    d_name = {}
    for row in data:
        d_dist[row['District']] = d_dist.get(row['District'], 0) + 1
        d_name[row['OperatingCompany']] = d_name.get(row['OperatingCompany'], 0) + 1

    print(*list(sorted(d_dist.items(), key=lambda x: -x[1]))[0], sep=': ')
    print(*list(sorted(d_name.items(), key=lambda x: -x[1])[1]), sep=': ')