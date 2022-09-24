def maxPresentations(scheduleStart, scheduleEnd):
    intervals = []

    for i in range(len(scheduleStart)):
        intervals.append([scheduleStart[i], scheduleEnd[i]])

    intervals.sort(key = lambda x: x[1])

    prev = float("-inf")
    res = len(scheduleStart)

    for interval in intervals:
        if interval[0] >= prev: prev = interval[1]
        else: res -= 1
    return res

print(maxPresentations([1,1,2,3], [2,3,3,4]))