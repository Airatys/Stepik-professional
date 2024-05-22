# Реализуйте генераторную функцию filter_names(), которая принимает три аргумента в следующем порядке:
#     names — список имен
#     ignore_char — одиночный символ
#     max_names — натуральное число
# Функция должна возвращать генератор, порождающий max_names имён из списка names, игнорируя имена, которые
#     начинаются на ignore_char (в любом регистре)
#     содержат хотя бы одну цифру
# Если max_names больше количества имен в списке names, то генератор должен породить все возможные имена из данного списка. 
# Примечание 1. Имена в возвращаемом функцией генераторе должны располагаться в своем исходном порядке.
# Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимую функцию filter_names(), но не код, вызывающий ее.

def filter_names(names: list, ignore_char: str, max_names: int):
    ignore_chr = filter(lambda x: not ignore_char.lower() == x[0].lower(), names)
    ignore_ord = filter(lambda x: not any(i.isdigit() for i in x), ignore_chr)
    yield from (v for i, v in enumerate(ignore_ord) if i < max_names) 
