def same_parity(numbers):
    if not numbers:
        return []
    elif numbers[0]%2 == 0:
        return list(filter(lambda x: x%2 == 0, numbers))
    else:
        return list(filter(lambda x: x%2 != 0, numbers))