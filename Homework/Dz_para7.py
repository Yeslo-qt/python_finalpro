def canny(func):
    def envel(word):
        allowed = "0123456789+-*/().% "

        for symbol in word:
            if symbol not in allowed:
                raise ValueError("Wrong symbol!")

        return func(word)

    return envel


@canny
def calculate(word):
    return eval(word, {"__builtins__": {}})


try:
    x = input("Enter an expression: ")
    print("Result:", calculate(x))

except ValueError as error:
    print("Error:", error)

except ZeroDivisionError:
    print("Error: Division by zero!")

except SyntaxError:
    print("Error: Wrong expression!")
