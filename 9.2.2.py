# Напишите программу, которая принимает на вход корректный непустой список, корректный непустой кортеж или корректное множество произвольной длины, и выполняет следующее:
#     если введен список, выводит его последний элемент
#     если введен кортеж, выводит его первый элемент
#     если введено множество, выводит количество его элементов
# Формат входных данных
# На вход программе подается корректный непустой список, кортеж или корректное произвольной длины множество.
# Формат выходных данных
# Программа должна вывести определенное значение, в зависимости от типа введенной коллекции.

code = eval(input())
if isinstance(code, list):
    print(code[-1])
if isinstance(code, tuple):
    print(code[0])
if isinstance(code, set):
    print(len(code))