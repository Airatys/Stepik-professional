from datetime import date, time
def is_correct(day, month, year):
    try:
        date(year, month, day)
        return True
        
    except:
        return False




