def officeDesign(arr, budget):
    windowStart = len = sum = 0

    for windowEnd in range(0, len(arr) - 1):
        sum += arr[windowEnd]

        if sum > budget:
            sum -= arr[windowStart]
            windowStart += 1
        
        len = max(len, windowEnd - windowStart + 1)
    
    return len