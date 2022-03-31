import heapq

def minimumTime(ability, processes):

    maxHeap = []
    for i in ability:
        heapq.heappush(maxHeap, -i)

    step = 0
    while processes > 0:
        maxAbility = -heapq.heappop(maxHeap)

        processes -= maxAbility

        maxAbility //= 2

        heapq.heappush(maxHeap, -maxAbility)

        step += 1
    return step