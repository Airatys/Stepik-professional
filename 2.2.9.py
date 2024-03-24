file_name: str = 'files.txt'

with open (file_name,'r',encoding='utf8') as file_open:
    load_list = [i.strip() for i in file_open.readlines()]

file_name: dict = dict()

total_size: dict = dict()

#функция перевода размеров в байты
def size_to_bite (dig: str,s: str):
    size_file = {'B': 1, 'KB': 1024, 'MB': 1048576, 'GB': 1073741824}
    return size_file.get(s) * int(dig)
    
#функция перевода в укрупненные еденицы измерения
def up_to_size(dig: int):
        if dig<1024:
            return f'{round(dig/1024)} B'
        elif dig//1024<1024:
            return f'{round(dig/1024)} KB'
        elif dig//1048576<1024:
            return f'{round(dig/1048576)} MB'
        elif dig//1073741824<1024:
            return f'{round(dig/1073741824)} GB'    
        
 

for file_info in load_list:
    file,size,unit = file_info.split()
    _,ex = file.split('.')
    
    total_size[ex] = total_size.get(ex,0)+size_to_bite(size,unit.strip())

    file_name[ex] = file_name.get(ex,[])+[file]
    
for key in sorted(total_size):
    print(*sorted(file_name.get(key)),sep='\n')
    print('----------')
    print('Summary:',up_to_size(total_size.get(key)))
    print()




