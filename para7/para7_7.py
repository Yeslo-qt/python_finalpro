def checker(func, *args, **kwargs):
    def checker(*args, **kwargs):
        try:
            result = func(*args, **kwargs)

        except Exception as exc:
            print(f"We have problems {exc}")
        else:
            print(f"No problems. Result - {result}")
    return checker
def calculate(expr):
    return eval(expr)

calc1 = checker(calculate)
calc1("2+2")