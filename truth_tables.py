booleans = [False, True]
for x in booleans:
    for y in booleans:
        print(int(x), int(y), "=>", int(x or y))

for x in booleans:
    for y in booleans:
        print(int(x), int(y), "=>", int(not x and y or x and not y))
