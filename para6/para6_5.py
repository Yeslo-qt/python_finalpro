try:
    try:
        print("start code")
        print(error_test)
        print("no error")
    except SyntaxError:
        print("Wrong Syntax!")
except NameError as error:
    print(error)


print("Code after capsule")