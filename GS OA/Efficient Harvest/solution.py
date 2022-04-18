def maxProfit(k, profit):
    maximumProfit = float("-inf")
    mid, n = len(profit) // 2, len(profit)

    runningProfit = 0
    for i in range(k):
        runningProfit += profit[i] + profit[(i + mid) % n]

    maximumProfit = max(maximumProfit, runningProfit)

    for i in range(k, k + mid - 1):
        runningProfit += profit[i] + profit[(i + mid) % n]
        runningProfit -= profit[i - k] + profit[(i - k + mid) % n]

        maximumProfit = max(maximumProfit, runningProfit)

    return maximumProfit