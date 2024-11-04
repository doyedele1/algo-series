def chooseFleets(wheels):
    res = []

    for n in wheels:
        if n % 2 != 0:
            res.append(0)
        else:
            res.append(n // 4 + 1)
    return res

print(chooseFleets([4, 5, 6]))
print(chooseFleets([6, 3, 2]))