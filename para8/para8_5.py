def adder(*args, **kwargs):
    result = 0
    for i in args:
        result += i
    for j in kwargs.values():
        result += j
    return result
