def checkPermutation(s):
    counts = {}
    for i in s:
        if i == " ":
            continue
        counts[i] = counts.get(i, 0) + 1

    hasOdd = False
    for value in counts.values():
        if value % 2 == 1:
            if hasOdd:
                # there is more than one char that appears an odd number of times
                return False
            hasOdd = True

    return True