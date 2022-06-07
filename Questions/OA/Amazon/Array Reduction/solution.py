import heapq

def reductionCost(num):
    heapq.heapify(num)

    minTotalCost = 0
    while len(num) > 1:
        i = heapq.heappop(num)
        j = heapq.heappop(num)
        minTotalCost += i + j
        heapq.heappush(num, i + j)

    return minTotalCost

print(reductionCost([1,2,3])) # return 9
print(reductionCost([5, 5, 5, 5])) # return 40