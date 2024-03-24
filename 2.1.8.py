def index_of_nearest(numbers, number):
    if not numbers:
        return -1
    elif len(numbers) > 0:
        n = min(numbers, key=lambda x: abs(x-number))
        return numbers.index(n)