try:
    print("start code")
    print(10 / 0)
    print("no error")
except (NameError, ZeroDivisionError) as catch_error:
    print(catch_error)


print("Code after capsule")