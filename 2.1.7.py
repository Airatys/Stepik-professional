def likes(names):
    a = len(names)
    if a == 0:
        return f'Никто не оценил данную запись'
    if a==1:
        return f'{names[0]} оценил(а) данную запись'
    if a==2:
        return f'{names[0]} и {names[1]} оценили данную запись'
    if a==3:
        return f'{names[0]}, {names[1]} и {names[2]} оценили данную запись'
    else:
        return f'{names[0]}, {names[1]} и {a -2} других оценили данную запись'

        
    
    




