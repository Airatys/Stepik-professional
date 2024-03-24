from datetime import datetime,timedelta
def choose_plural(amount, variants):
    variant = 2
    if amount % 10 == 1 and amount % 100 != 11:
        variant = 0
    elif amount % 10 >= 2 and amount % 10 <= 4 and (amount % 100 < 10 or amount % 100 >= 20):
        variant = 1
    return '{} {}'.format(amount, variants[variant])
nowdate=datetime.strptime(input(),'%d.%m.%Y %H:%M')
datek=datetime(2022,11,8,12)
ostalos=datek-nowdate
if ostalos.days<0:
    print('Курс уже вышел!')
else:
    if ostalos.days > 0:
        if ostalos.seconds//3600 > 0:
            if ostalos.seconds//60-ostalos.seconds//3600*60 > 0:
                print('До выхода курса осталось:',choose_plural(ostalos.days, ['день','дня','дней']),'и', choose_plural(ostalos.seconds//3600, ['час','часа','часов']))            
            else:
                            print('До выхода курса осталось:',choose_plural(ostalos.days, ['день','дня','дней']),'и',choose_plural(ostalos.seconds//3600, ['час','часа','часов']))
        else:
            if ostalos.seconds//60-ostalos.seconds//3600*60 > 0:
                print('До выхода курса осталось:',choose_plural(ostalos.days, ['день','дня','дней']))
            else:
                print('До выхода курса осталось:',choose_plural(ostalos.days, ['день','дня','дней']))
                
        
    else: 
        if ostalos.seconds//3600 > 0:
            if ostalos.seconds//60-ostalos.seconds//3600*60 > 0:
                print('До выхода курса осталось:',choose_plural(ostalos.seconds//3600, ['час','часа','часов']),'и',choose_plural(ostalos.seconds//60-ostalos.seconds//3600*60, ['минута','минуты','минут']))
            else:
                print('До выхода курса осталось:',choose_plural(ostalos.seconds//3600, ['час','часа','часов']))
            
        else:
            if ostalos.seconds//60-ostalos.seconds//3600*60 > 0:
                print('До выхода курса осталось:',choose_plural(ostalos.seconds//60-ostalos.seconds//3600*60, ['минута','минуты','минут']))
                
            else:
                print('Курс уже вышел!')





