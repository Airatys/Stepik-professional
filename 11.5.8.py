# Дополните приведенный ниже код, чтобы переменная regex содержала регулярное выражение, которому соответствуют последовательности из 88 цифр.
# Причем последовательность может содержать символы дефиса - в качестве разделителей, только если они делят ее на группы по 22 цифры.

regex = r'(\d{2}(-)\d{2}\2\d{2}\2\d{2})|(\d{8})'

regex = r'\d{2}(-?)(\d{2}\1){2}\d{2}'