import json
with open('data1.json', encoding='utf8') as file_1, open('data2.json', encoding='utf8') as file_2:
    dat_1 = json.load(file_1)
    dat_2 = json.load(file_2)
    dat_1.update(dat_2)
        
    with open('data_merge.json', 'w', encoding='utf8') as file_3:
        json.dump(dat_1, file_3, indent=3)
            
        
        




