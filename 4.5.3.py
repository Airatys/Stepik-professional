# Вам доступен архив workbook.zip, содержащий различные папки и файлы.
# Напишите программу, которая выводит название файла из этого архива, который имеет наилучший показатель степени сжатия.
# Примечание 1. Если файл находится в папке, вывести следует только название без пути.
# Примечание 2. Гарантируется, что в исходном архиве только один файл имеет наилучший показатель степени сжатия.
# Примечание 3. Степень сжатия файла характеризуется коэффициентом K, определяемым как отношение объема сжатого файла Vc
# ​к объему исходного файла Vo​, выраженным в процентах:

from zipfile import ZipFile

k1 = 100
with ZipFile('workbook.zip') as file:
    dat = file.infolist()
    for i in dat:
        if i.file_size != 0:
            k2 = (i.compress_size*100)//i.file_size
            if k2 < k1:
                k1 = k2
                a = i.filename.split('/')[-1]
    print(a)
    
    