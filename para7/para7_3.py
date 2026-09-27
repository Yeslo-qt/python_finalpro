def  raise_to_the_degrees(number, max_degrees):
    i = 0
    for j in range(max_degrees):
        yield number ** i
        i += 1

res = raise_to_the_degrees(1234, 200)

for el in res:
    print(el)
    print()
print("new")
for el in res:
    print(el)
    print()


