# Команда BEEGEEK планирует выпустить свой новый курс 08.11.2022 ровно в 12:00.
# Напишите программу, которая принимает на вход текущие дату и время и определяет, сколько времени осталось до выхода курса.
# Формат входных данных
# На вход программе подаются текущие дата и время в формате DD.MM.YYYY HH:MM.
# Формат выходных данных
# Программа должна вывести текст с указанием количества дней и часов, оставшихся до выхода курса, в следующем формате:
# До выхода курса осталось: <кол-во дней> дней и <кол-во часов> часов
# Если в данном случае количество часов равно нулю, то вывести нужно только дни.
# Если количество дней равно нулю, то вывести нужно только часы и минуты в следующем формате:
# До выхода курса осталось: <кол-во часов> часов и <кол-во минут> минут
# Если в данном случае количество минут равно нулю, то вывести нужно только часы.
# Аналогично, если количество часов равно нулю, то вывести нужно только минуты.
# Если введенные дата и время больше либо равны 08.11.2022 12:00, программа должна вывести текст: 
# Курс уже вышел!
# Примечание 1. Программа должна подбирать правильную форму для существительных «день» и «минута».
# Для этого можете смело взять свою функцию choose_plural() из этой задачи.

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





