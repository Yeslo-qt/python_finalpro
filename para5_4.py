class First_class:
    pass

class Second_class(First_class):
    pass

print(issubclass(First_class, Second_class))
print(issubclass(Second_class, First_class))
