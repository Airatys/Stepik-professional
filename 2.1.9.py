def spell(*args):
    mydict = {}
    for i in args:
        m = list(filter(lambda x: x[0].lower()==i[0].lower(), args))
        mydict[i[0].lower()] = mydict.setdefault(i[0].lower(), len(max(m, key=len)))

    return mydict
    