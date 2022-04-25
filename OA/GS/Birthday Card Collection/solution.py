def solution(collection, d):
    seenCard = set(collection) 
    res = [] 
    currentSum = 0 
    
    for i in range(1, d + 1): 
        if i in seenCard: continue 
        if currentSum + i > d: break 
        currentSum += i 
        res.append(i) 
    
    return res