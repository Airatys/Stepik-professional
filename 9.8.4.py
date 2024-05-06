import functools
import time

def repeater(repeat=1):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(1, repeat + 1):
                print(f'{i}-й запуск функции.')
                value = func(*args, **kwargs)
            return value
        return wrapper
    return decorator

def delayed(delay=2):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print(f'Спим {delay} сек.')
            time.sleep(delay)
            value = func(*args, **kwargs)
            return value
        return wrapper
    return decorator

@repeater(repeat=5)
@delayed(delay=1)
def monitor(url):
    print(f'Проверка {url} на доступность.')
    
monitor('https://stepik.org/')