# Реализуйте функцию matrix_to_dict() с использованием аннотаций типов, которая принимает один аргумент:
#     matrix — матрица произвольной размерности, элементами которой являются целые или вещественные числа
# Функция должна возвращать словарь, ключом в котором является номер строки матрицы, а значением — список элементов этой строки.
# Примечание 1. Используйте встроенные типы (list, tuple, ...), а не типы из модуля typing. Также используйте нотацию |, а не тип Union из модуля typing.
# Примечание 2. Под матрицей подразумеваются исключительно вложенные списки.
# Примечание 3. Нумерация строк матрицы в возвращаемом функцией словаре должна начинаться с единицы.
# Примечание 4. Элементы матрицы в списке должны располагаться в своем исходном порядке.
# Примечание 5. В тестирующую систему сдайте программу, содержащую только необходимую функцию matrix_to_dict(), но не код, вызывающий ее.

def matrix_to_dict(matrix: list[list[int | float]]) -> dict[int, list[int | float]]:
    mydict = {}
    for i in range(len(matrix)):
        mydict.setdefault(i+1, matrix[i])
    return mydict
    
    