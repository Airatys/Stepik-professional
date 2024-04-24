# Реализуйте функцию is_power() с использованием рекурсии, которая принимает один аргумент:
#     number — натуральное число
# Функция должна возвращать значение True, если number является степенью числа 22, или False в противном случае.
# Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимую функцию is_power(), но не код, вызывающий ее.

def is_power(number: int, ch = 2):
    if number == 1 or number == ch:
        return True
    else:
        if ch <= number:
            return is_power(number, ch*2)
        else: 
            return False