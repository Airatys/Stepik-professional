import json
import sys

text = ''
for i in sys.stdin:
    i.strip()
    text += i

json_text = json.loads(text)
for k, v in json_text.items():
    if type(v) == list:
        
        print(f'{k}: {", ".join(map(str,v))}')  # ", ".join(map(str,v))
    else:
        print(f'{k}: {v}')




