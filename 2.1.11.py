def get_biggest(numbers):
    if len(numbers) == 0:
        return -1
    elif len(numbers) > 0:
        numbers = list(map(str, numbers))
        m = len(max(numbers, key=len))
        mystr = sorted(numbers, key=lambda x: x * m, reverse=True)
        return  int(''.join(mystr))