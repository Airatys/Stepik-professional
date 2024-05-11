# Реализуйте функцию get_min_max(), которая принимает один аргумент:
#     iterable — итерируемый объект, элементы которого сравнимы между собой
# Функция должна возвращать кортеж, в котором первым элементом является минимальный элемент итерируемого объекта iterable, вторым — максимальный элемент итерируемого объекта iterable.
# Если итерируемый объект iterable пуст, функция должна вернуть значение None.
# Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимую функцию get_min_max(), но не код, вызывающий ее.

def get_min_max(iterable):
    try:
        min_iter = max_iter = next(iterable)
        for i in iterable:
            if i < min_iter:
                min_iter = i
            if i > max_iter:
                max_iter = i
        return min_iter, max_iter
    except:
        try:
            return min(iterable), max(iterable)
        except:
            return None
 
        

    
data = iter(['bbb'])

print(get_min_max(data))