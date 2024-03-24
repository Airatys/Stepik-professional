def is_valid(string):
    return True if string.isdigit() and 3 < len(string) < 7 and not string.isspace() else False