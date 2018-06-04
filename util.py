def with_prev(lst):
    return zip([None] + lst[:-1], lst)

def with_prev_and_next(lst, make_default=lambda: None):
    return zip([make_default()] + lst[:-1], lst, lst[1:] + [make_default()])

def dedupe(lst):
    """Removes consecutive duplicates from a list, returning a new list"""
    ret = []
    for x in lst:
        if ret and ret[-1] == x:
            continue
        ret.append(x)
    return ret
