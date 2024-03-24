# put your python code here
import sys

data = [int(line) for line in sys.stdin]
print('Анри' if data[-1]%2==0 and len(data)%2!=0 or (data[-1]%2!=0 and len(data)%2==0) else 'Дима')



