# Реализуйте функцию verification(), которая проверяет правильность введенного пароля. Она должна принимать четыре аргумента в следующем порядке:
#     login — логин пользователя
#     password — пароль пользователя
#     success — некоторая функция
#     failure — некоторая функция
# Пароль считается правильным, если в нем присутствует, хотя бы одна заглавная латинская буква, хотя бы одна строчная латинская буква и хотя бы одна цифра.
# Функция verification() должна вызывать функцию success() с аргументом login, если переданный пароль является правильным, иначе — функцию failure() с аргументами login и строкой-сообщением об ошибке:
#     в пароле нет ни одной буквы, если в пароле отсутствуют латинские буквы
#     в пароле нет ни одной заглавной буквы, если в пароле отсутствуют заглавные латинские буквы
#     в пароле нет ни одной строчной буквы, если в пароле отсутствуют строчные латинские буквы
#     в пароле нет ни одной цифры, если в пароле отсутствуют цифры
# Примечание 1. Если пароль не удовлетворяет нескольким условиям, то приоритеты выбора строки-сообщения об ошибке являются следующими:
#     в пароле нет ни одной буквы
#     в пароле нет ни одной заглавной буквы
#     в пароле нет ни одной строчной буквы
#     в пароле нет ни одной цифры
# Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимую функцию verification(), но не код, вызывающий ее.

class ErrorPossword_1(Exception):
    pass

class ErrorPossword_2(Exception):
    pass

class ErrorPossword_3(Exception):
    pass

class ErrorPossword_4(Exception):
    pass

def verification(login, password, success, failure):
    try:
        if not any(True if i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz' else False for i in password):
            raise ErrorPossword_1
        if not any(True if i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' else False for i in password):
            raise ErrorPossword_2
        if not any(True if i in 'abcdefghijklmnopqrstuvwxyz' else False for i in password):
            raise ErrorPossword_3
        if not any(i.isdigit() for i in password):
            raise ErrorPossword_4
        return success(login)
    except ErrorPossword_1:
        failure(login, 'в пароле нет ни одной буквы')
    except ErrorPossword_2:
        failure(login, 'в пароле нет ни одной заглавной буквы')
    except ErrorPossword_3:
        failure(login, 'в пароле нет ни одной строчной буквы')
    except ErrorPossword_4:
        failure(login, 'в пароле нет ни одной цифры')
        
        