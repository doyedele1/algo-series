def generateSequence(target):
    cache = set({1})
    outputString = ""
    start = 1

    while start != target:
        if start < target:
            start *= 2
            cache.add(start)
            outputString += "*"
        if start > target:
            potentialStart = start // 3
            if potentialStart in cache:
                start *= 2
                cache.add(start)
                outputString += "*"
            else:
                start = potentialStart
                cache.add(start)
                outputString += "/"
    return outputString

# print(generateSequence(12))