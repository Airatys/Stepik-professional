import time
def calculate_it(func, *args):
    start = time.monotonic()
    a = func(*args)
    end = time.monotonic()
    start_end = end - start
    return a, start_end


