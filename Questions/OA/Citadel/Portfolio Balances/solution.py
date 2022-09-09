def maxValue(n, rounds):
    investmentArr = [0] * n
    
    for round in rounds:
        investmentArr[round[0] - 1] += round[2]

        if round[1] < n:
            investmentArr[round[1]] -= round[2]
    
    curr, res = 0, 0
    for val in investmentArr:
        curr += val
        res = max(res, curr)
    return res

maxValue(5, ([1,2,10], [2,4,5], [3,5,12]))