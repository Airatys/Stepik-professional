import json
from collections import ChainMap

counter = 0
with open('zoo.json', encoding='u8') as file:
    jsonfile = json.load(file)
    dat = ChainMap(*jsonfile)
    # print(dat)
    for k in dat:
        counter += dat[k]
    print(counter)
    