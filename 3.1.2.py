# импортируем тип date из модуля datetime
from datetime import date

# создаем объект, соответсвующий дате урагана
hurricane_andrew = date(year=1992, month=8, day=24)

# выводим день недели
print(hurricane_andrew.weekday())