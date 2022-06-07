import heapq

def reductionCost(num):
    heapq.heapify(num)

    minTotalCost = 0
    while len(num) > 1:
        first = heapq.heappop(num)
        second = heapq.heappop(num)
        minTotalCost += first + second
        heapq.heappush(num, first + second)
    return minTotalCost

print(reductionCost([1,2,3])) # return 9
print(reductionCost([5, 5, 5, 5])) # return 40