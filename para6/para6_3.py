try:
    print("start code")
    print(10 / 0)
    print("no error")
except (NameError, ZeroDivisionError):
    print("We have an error!")


print("Code after capsule")