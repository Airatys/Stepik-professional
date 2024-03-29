# Вам доступен текстовый файл files.txt, содержащий информацию о файлах.
# Каждая строка файла содержит три значения, разделенные символом пробела — имя файла, его размер (целое число) и единицы измерения:
# cant-help-myself.mp3 7 MB
# keep-yourself-alive.mp3 6 MB
# bones.mp3 5 MB
# ...
# Напишите программу, которая группирует данные файлы по расширению, определяя общий объем файлов каждой группы, и выводит полученные группы файлов, указывая для каждой ее общий объем.
# Группы должны быть расположены в лексикографическом порядке названий расширений, файлы в группах — в лексикографическом порядке их имен.
# Примечание 1. Например, если бы файл files.txt имел вид:
# input.txt 3000 B
# scratch.zip 300 MB
# output.txt 1 KB
# temp.txt 4 KB
# boy.bmp 2000 KB
# mario.bmp 1 MB
# data.zip 900 MB
# то программа должна была бы вывести:
# boy.bmp
# mario.bmp
# ----------
# Summary: 3 MB
# input.txt
# output.txt
# temp.txt
# ----------
# Summary: 8 KB
# data.zip
# scratch.zip
# ----------
# Summary: 1 GB
# где Summary — общий объем файлов группы.
# Примечание 2. Гарантируется, что все имена файлов содержат расширение.
# Примечание 3. Общий объем файлов группы записывается в самых крупных (максимально возможных) единицах измерения с округлением до целых.
# Другими словами, сначала следует определить суммарный объем всех файлов группы, скажем, в байтах, а затем перевести полученное значение в самые крупные (максимально возможные) единицы измерения. Примеры перевода:
#     1023 B -> 1023 B
#     1300 B -> 1 KB
#     1900 B -> 2 KB
# Примечание 4. Значения единиц измерения такие же, какие приняты в информатике:
#     1 KB = 1024 B
#     1 MB = 1024 KB
#     1 GB = 1024 MB

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




