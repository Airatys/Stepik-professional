from datetime import date
def get_min_max(args):
    if not args:
        return ()
    else:
        return tuple((min(args), max(args)))




