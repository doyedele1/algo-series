def minimizeMemory(processes, m):
    windowStart = prefSum = maxSum = 0
    totalSum = sum(processes)

    for i in range(len(processes)):
        windowSize = (i - windowStart) + 1
        prefSum += processes[i]
        if windowSize == m:
            maxSum= max(maxSum, prefSum)
            prefSum -= processes[windowStart]
            windowStart += 1

    res = totalSum - maxSum
    return res

print(minimizeMemory([10, 4, 8, 13, 20], 2))