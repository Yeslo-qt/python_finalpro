def adder(*args, **kwargs):
    result = 0
    for a in args:
        if type(a) == int or type(a) == bool or type(a) == float():
            result += a
        else:
            try:
                result += float(a)
                continue
            except (ValueError, TypeError):
                pass

    for a in kwargs.values():
        if type(a) == int or type(a) == bool or type(a) == float():
            result += a
        else:
            try:
                result += float(a)
                continue
            except (ValueError, TypeError):
                pass
    return result
