import time
def get_the_fastest_func(funcs, arg):
    mylist = []
    for func in funcs:
        start = time.monotonic()
        func(arg)
        end = time.monotonic()
        s_end = end - start
        mylist.append(s_end)
    i = mylist.index(min(mylist)) 
    return funcs[i]




