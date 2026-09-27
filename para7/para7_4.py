def raise_to_the_degrees(number):
    i = 0
    while True:
        result = number ** i
        yield result
        if result > 200 ** 20:
            return
        i += 1

res = raise_to_the_degrees(1234)
print(res)
for el in res:
    print(el)
    print()
