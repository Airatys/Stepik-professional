# Вам доступна функция password_gen(), которая возвращает генератор, порождающий все трехсимвольные строковые пароли в порядке возрастания, составленные из цифр от 00 до 99 включительно.
# Перепишите данную функцию с использованием функции product(), чтобы она выполняла ту же задачу.
# Примечание. В тестирующую систему сдайте программу, содержащую только необходимую функцию password_gen(), но не код, вызывающий ее.

import  itertools as it

def password_gen():
    for i in it.product(range(10), range(10), range(10)):
        yield ''.join(map(str, i))