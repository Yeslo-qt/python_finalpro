try:
    print("start code")
    print(10/0)
    print("no error")
except NameError:
    print("We have an Name error!")
except ZeroDivisionError:
    print("We have an ZeroDivision error!")
    

print("Code after capsule")