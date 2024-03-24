# put your python code here
from datetime import date, time
def is_correct(day, month, year):
    try:
        date(year, month, day)
        return True
        
    except:
        return False

counter = 0
while (n:= input()) != 'end':
    day, month, year = n.split('.')
    if is_correct(int(day), int(month), int(year)):
        counter += 1
        print('Корректная')
    else:
        print('Некорректная')
print(counter)
    





