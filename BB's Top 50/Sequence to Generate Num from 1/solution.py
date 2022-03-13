def generateSequence(target):
    visited = set({1})
    outputString = ""
    start = 1

    while start != target:
        if start < target:
            start *= 2
            visited.add(start)
            outputString += "*"
        if start > target:
            potentialStart = start // 3
            if potentialStart in visited:
                start *= 2
                visited.add(start)
                outputString += "*"
            else:
                start = potentialStart
                visited.add(start)
                outputString += "/"

    return outputString

print(generateSequence(12))