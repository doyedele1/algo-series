def maxPresentations(scheduleStart, scheduleEnd):
    res = 0
        
    startArr = sorted(scheduleStart)
    endArr = sorted(scheduleEnd)
    
    start, end = 0, 0
    
    while start < len(scheduleStart):
        if startArr[start] >= endArr[end]:
            res -= 1
            end += 1
        
        res += 1
        start += 1
        
    return res

print(maxPresentations([1,1,2], [3,2,4]))