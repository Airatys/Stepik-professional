def convert(string):
    count1 = 0
    count2 = 0
    for i in string:
        if i.isupper():
            count1 += 1
        if i.islower():
            count2 += 1
    if count1 < count2 or count1 == count2:
        return string.lower()
    else:
        return string.upper()