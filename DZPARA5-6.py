result = []


def divider(a, b):
    if a < b:
        raise ValueError

    if b > 100:
        raise IndexError
    return a / b


data = [(10, 2), (2, 5), ("123", 4), (18, 0), ([], 15), (10, 101), (8, 4)]


for a, b in data:
    try:
        result.append(divider(a, b))

    except ValueError:
        print("Помилка ValueError")

    except IndexError:
        print("Помилка IndexError")

    except TypeError:
        print("Помилка TypeError")

    except ZeroDivisionError:
        print("Помилка ZeroDivisionError")


print(result)
