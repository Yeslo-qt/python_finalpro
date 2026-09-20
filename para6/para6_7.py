def checker(var_1):
    if type(var_1) != str:
        raise TypeError(f"Sorry, we can't work with {type(var_1)}, we need class str")
    else:
        return var_1

f_var = 10
s_var = "dima"

checker(s_var)
checker(f_var)